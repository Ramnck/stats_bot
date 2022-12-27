from aiogram.types import Message
from decouple import config

def is_based(msg: Message) -> bool:
    return msg.from_user.id in config("USERS")