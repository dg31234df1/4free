from __future__ import annotations

import time, json, re
from aiohttp import ClientSession
from typing import AsyncGenerator

from .base_provider import AsyncGeneratorProvider
from .helper import format_prompt

class ChatgptDemo(AsyncGeneratorProvider):
    url = "https://chat.chatgptdemo.net"
    supports_gpt_35_turbo = True
    working = True

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: list[dict[str, str]],
        proxy: str = None,
        timeout: int = 30,
        **kwargs
    ) -> AsyncGenerator:
        headers = {
            "authority": "chat.chatgptdemo.net",
            "accept-language": "de-DE,de;q=0.9,en-DE;q=0.8,en;q=0.7,en-US",
            "origin": "https://chat.chatgptdemo.net",
            "referer": "https://chat.chatgptdemo.net/",
            "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        async with ClientSession(headers=headers, timeout=timeout) as session:
            async with session.get(f"{cls.url}/", proxy=proxy) as response:
                response.raise_for_status()
                response = await response.text()
                result = re.search(r'<div id="USERID" style="display: none">(.*?)<\/div>', response)
                if not result:
                    raise RuntimeError("No user id found")
                user_id = result.group(1)
            async with session.post(f"{cls.url}/new_chat", json={"user_id": user_id}, proxy=proxy) as response:
                response.raise_for_status()
                chat_id = (await response.json())["id_"]
            if not chat_id:
                raise RuntimeError("Could not create new chat")
            data = {
                "question": format_prompt(messages),
                "chat_id": chat_id,
                "timestamp": int(time.time()*1000),
            }
            async with session.post(f"{cls.url}/chat_api_stream", json=data, proxy=proxy) as response:
                response.raise_for_status()
                async for line in response.content:
                    if line.startswith(b"data: "):
                        line = json.loads(line[6:-1])
                        chunk = line["choices"][0]["delta"].get("content")
                        if chunk:
                            yield chunk