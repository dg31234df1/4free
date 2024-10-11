from __future__ import annotations

from aiohttp import ClientSession
import json

from ...typing import AsyncResult, Messages
from ..base_provider import AsyncGeneratorProvider, ProviderModelMixin
from ...image import ImageResponse


class NexraSDLora(AsyncGeneratorProvider, ProviderModelMixin):
    label = "Nexra Stable Diffusion Lora"
    url = "https://nexra.aryahcr.cc/documentation/stable-diffusion/en"
    api_endpoint = "https://nexra.aryahcr.cc/api/image/complements"
    working = True
    
    default_model = 'sdxl-lora'
    models = [default_model]

    @classmethod
    def get_model(cls, model: str) -> str:
        return cls.default_model

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        response: str = "url", # base64 or url
        guidance: str = 0.3, # Min: 0, Max: 5
        steps: str = 2, # Min: 2, Max: 10
        **kwargs
    ) -> AsyncResult:
        model = cls.get_model(model)
        
        headers = {
            "Content-Type": "application/json"
        }
        async with ClientSession(headers=headers) as session:
            prompt = messages[0]['content']
            data = {
                "prompt": prompt,
                "model": model,
                "response": response,
                "data": {
                    "guidance": guidance,
                    "steps": steps
                }
            }
            async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
                text_data = await response.text()
                
                if response.status == 200:
                    try:
                        json_start = text_data.find('{')
                        json_data = text_data[json_start:]
                        
                        data = json.loads(json_data)
                        if 'images' in data and len(data['images']) > 0:
                            image_url = data['images'][-1]
                            yield ImageResponse(image_url, prompt)
                        else:
                            yield ImageResponse("No images found in the response.", prompt)
                    except json.JSONDecodeError:
                        yield ImageResponse("Failed to parse JSON. Response might not be in JSON format.", prompt)
                else:
                    yield ImageResponse(f"Request failed with status: {response.status}", prompt)
