from asyncio import sleep
from logging import getLogger

import src.handlers.statictics as st
from aiogram import Bot, F, Router
from aiogram.types import Message

from ..settings import get_settings
from ..tools.file_manager import remote_open
from ..tools.recognition import voice_to_text

settings = get_settings()
logger = getLogger("handlers.voice")
router = Router()


@router.message((F.voice) | (F.video_note))
async def speech2text(msg: Message, bot: Bot):
    if not (msg.video_note and msg.chat.id == settings.ANGAR_ID):
        obj = msg.voice if msg.voice else msg.video_note
        async with remote_open(bot, obj) as f:
            text = await voice_to_text(f)
            if text:
                await msg.reply(text)
            else:
                logger.info("Voice is not recognised")
    await st.router.propagate_event("message", msg)
