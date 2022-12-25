from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=['start']))
async def start(msg: types.Message):
    await msg.answer('aboba')