import aiohttp
import aiofiles
from pathlib import Path
from aiogram.types import Downloadable
from ..base import bot
from ..settings import get_settings

from contextlib import asynccontextmanager

from logging import getLogger
from asyncio import sleep

from os import remove

logger = getLogger('tools.file_manager')

settings = get_settings()

async def download(url: str, destination: str | Path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(destination, mode='wb')
                await f.write(await resp.read())
                await f.close()
            else:
                logger.error(f"{resp.status} status code during downloading file")

@asynccontextmanager
async def remote_open(object: Downloadable):
    try:
        await sleep(.03)
        file = await bot.get_file(object.file_id)
        file_path = settings.TMP_DIR / (str(file.file_unique_id) + '.oga') 
        url = f"https://api.telegram.org/file/bot{settings.TOKEN}/{file.file_path}"
        await download(url, file_path)
        yield file_path
    except Exception as ex:
        logger.warning(str(ex))
    finally:
        remove(file_path)
        