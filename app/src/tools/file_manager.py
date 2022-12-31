import aiohttp
import aiofiles
import json
from pathlib import Path
from aiogram.types import Downloadable
from ..base import bot_get_file
from ..settings import get_settings

from contextlib import asynccontextmanager

from logging import getLogger
from asyncio import sleep

from os import remove

logger = getLogger('tools.file_manager')

settings = get_settings()


async def _get_bot_data() -> dict:
    path = Path(__file__).parent.parent
    async with aiofiles.open(str(path) + "/bot.json", encoding="utf-8") as f:
        return json.loads(await f.read())


async def _update_bot_data(data: dict) -> dict:
    path = Path(__file__).parent.parent
    async with aiofiles.open(str(path) + "/bot.json", mode="w", encoding="utf-8") as f:
        await f.write(json.dumps(data, indent=4))


async def read_chat(chat_name: str) -> dict | None:
    try:
        bot = await _get_bot_data()
        chat = bot["chats"][chat_name]
        return chat
    except KeyError:
        logger.error(f"KeyError: Chat - {chat_name} not in whitelist!")


async def update_bot_chat(chat_name: str, fields: dict) -> dict | None:
    try:
        bot = await _get_bot_data()
        for key in fields.keys():
            bot["chats"][chat_name][key] = fields[key]
        await _update_bot_data(bot)
        return bot
    except KeyError:
        logger.error(f"KeyError: Chat - {chat_name} not in whitelist!")


async def download(url: str, destination: str | Path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                async with aiofiles.open(destination, mode='wb') as f:
                    await f.write(await resp.read())
            else:
                logger.error(f"{resp.status} status code during downloading file")

@asynccontextmanager
async def remote_open(object: Downloadable):
    try:
        await sleep(.03)
        file = await bot_get_file(object)
        file_path = settings.TMP_DIR / (str(file.file_unique_id) + '.oga') 
        url = f"https://api.telegram.org/file/bot{settings.TOKEN}/{file.file_path}"
        await download(url, file_path)
        yield file_path
    except Exception as ex:
        logger.warning(str(ex))
    finally:
        remove(file_path)
        
