from __future__ import annotations
import re
from aiohttp import ClientSession
import json
from typing import List
import requests

from ...typing import AsyncResult, Messages
from ..base_provider import AsyncGeneratorProvider, ProviderModelMixin
from ..helper import format_prompt

def clean_response(text: str) -> str:
    """Clean response from unwanted patterns."""
    patterns = [
        r"One message exceeds the \d+chars per message limit\..+https:\/\/discord\.com\/invite\/\S+",
        r"Rate limit \(\d+\/minute\) exceeded\. Join our discord for more: .+https:\/\/discord\.com\/invite\/\S+",
        r"Rate limit \(\d+\/hour\) exceeded\. Join our discord for more: https:\/\/discord\.com\/invite\/\S+",
        r"</s>", # zephyr-7b-beta
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text)
    return text.strip()

def split_message(message: dict, chunk_size: int = 995) -> List[dict]:
    """Split a message into chunks of specified size."""
    content = message.get('content', '')
    if len(content) <= chunk_size:
        return [message]

    chunks = []
    while content:
        chunk = content[:chunk_size]
        content = content[chunk_size:]
        chunks.append({
            'role': message['role'],
            'content': chunk
        })
    return chunks

def split_messages(messages: Messages, chunk_size: int = 995) -> Messages:
    """Split all messages that exceed chunk_size into smaller messages."""
    result = []
    for message in messages:
        result.extend(split_message(message, chunk_size))
    return result

class AirforceChat(AsyncGeneratorProvider, ProviderModelMixin):
    label = "AirForce Chat"
    api_endpoint = "https://api.airforce/chat/completions"
    supports_stream = True
    supports_system_message = True
    supports_message_history = True

    default_model = 'llama-3.1-70b-chat'
    response = requests.get('https://api.airforce/models')
    data = response.json()

    text_models = [model['id'] for model in data['data']]
    
    models = [*text_models]
    
    model_aliases = {
		# openchat
		"openchat-3.5": "openchat-3.5-0106",
		
		# deepseek-ai
		"deepseek-coder": "deepseek-coder-6.7b-instruct",
		
		# NousResearch
		"hermes-2-dpo": "Nous-Hermes-2-Mixtral-8x7B-DPO",
		"hermes-2-pro": "hermes-2-pro-mistral-7b",
		
		# teknium
		"openhermes-2.5": "openhermes-2.5-mistral-7b",
		
		# liquid
		"lfm-40b": "lfm-40b-moe",
		
		# DiscoResearch
		"german-7b": "discolm-german-7b-v1",
			
		# meta-llama
		"llama-2-7b": "llama-2-7b-chat-int8",
		"llama-2-7b": "llama-2-7b-chat-fp16",
		"llama-3.1-70b": "llama-3.1-70b-chat",
		"llama-3.1-8b": "llama-3.1-8b-chat",
		"llama-3.1-70b": "llama-3.1-70b-turbo",
		"llama-3.1-8b": "llama-3.1-8b-turbo",
		
		# inferless
		"neural-7b": "neural-chat-7b-v3-1",
		
		# HuggingFaceH4
		"zephyr-7b": "zephyr-7b-beta",
		
		# llmplayground.net
		#"any-uncensored": "any-uncensored",	
    }

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = False,
        proxy: str = None,
        max_tokens: str = 4096,
        temperature: str = 1,
        top_p: str = 1,
        **kwargs
    ) -> AsyncResult:
        model = cls.get_model(model)

        chunked_messages = split_messages(messages)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer missing api key',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://llmplayground.net',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://llmplayground.net/',
            'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

        data = {
            "messages": chunked_messages,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stream": stream
        }

        async with ClientSession(headers=headers) as session:
            async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
                response.raise_for_status()
                text = ""
                if stream:
                    async for line in response.content:
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            json_str = line[6:]
                            try:
                                chunk = json.loads(json_str)
                                if 'choices' in chunk and chunk['choices']:
                                    content = chunk['choices'][0].get('delta', {}).get('content', '')
                                    text += content
                            except json.JSONDecodeError as e:
                                print(f"Error decoding JSON: {json_str}, Error: {e}")
                        elif line.strip() == "[DONE]":
                            break
                    yield clean_response(text)
                else:
                    response_json = await response.json()
                    text = response_json["choices"][0]["message"]["content"]
                    yield clean_response(text)

