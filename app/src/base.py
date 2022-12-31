from aiogram.types import Message, Downloadable, File, ChatMember
from aiogram import Bot
from .settings import get_settings

settings = get_settings()

bot = Bot(settings.TOKEN)

def is_based(msg: Message) -> bool:
    return msg.from_user.id in settings.CHATS


async def bot_get_file(object: Downloadable) -> File:
    return await bot.get_file(object.file_id)

async def bot_get_member(user_id: int) -> ChatMember:
    return await bot.get_chat_member(settings.ANGAR_ID, user_id)

async def bot_send_message(text: str) -> None:
    await bot.send_message(settings.ANGAR_ID, text)