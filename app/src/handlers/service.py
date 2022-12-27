from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from ..base import is_based

router = Router()

@router.message(~F.func(lambda msg: is_based(msg)))
async def wrong_people(msg: Message):
    return
    
@router.message(Command(commands=['start']))
async def start(msg: Message):
    await msg.answer('Тебе не понадобится этот бот')

@router.message(Command(commands=['help']))
async def help(msg: Message):
    await msg.answer('Если ты не знаешь что это за бот значит он тебе не нужен')