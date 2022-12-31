from aiogram.types import Message
from aiogram import Bot
from .settings import get_settings

settings = get_settings()

bot = Bot(settings.TOKEN)

def is_based(msg: Message) -> bool:
    return msg.from_user.id in settings.CHATS
