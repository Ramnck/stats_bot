import json
from logging import getLogger
from pathlib import Path

import aiofiles

logger = getLogger("tools.file_manager")


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
