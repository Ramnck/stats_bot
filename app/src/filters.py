from aiogram.types import Message

from .settings import get_settings

settings = get_settings()


def is_based(msg: Message) -> bool:
    return msg.from_user.id in settings.CHATS
