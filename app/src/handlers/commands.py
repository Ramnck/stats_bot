from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.crud import stats
from ..db.models import Statistics
from ..tools.formatter import stats_format

from ..base import bot_get_member

router = Router()


@router.message(Command(commands=["start"]))
async def start(msg: Message):
    await msg.answer("Тебе не понадобится этот бот")


@router.message(Command(commands=["help"]))
async def help(msg: Message):
    await msg.answer("Если ты не знаешь что это за бот значит он тебе не нужен")


@router.message(Command(commands=["info"]))
async def info(msg: Message):
    user_stats = await stats.get_or_create(msg.from_user.id)
    res = stats_format(user_stats)
    await msg.reply(res, parse_mode="HTML")


@router.message(F.text == "@all")
async def mention_all(msg: Message):
    members = await Statistics.all().values_list('id', flat=True)
    print(members)
    text = ""
    for user_id in members:
        usr = (await bot_get_member(user_id)).user
        text += usr.mention_html(usr.full_name) + " "
    await msg.answer(text, parse_mode='html')