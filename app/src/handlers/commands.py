from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.crud import stats
from ..db.models import Statistics
from ..tools.formatter import stats_format

from ..base import bot_get_member, bot_send_message, bot_delete_message
from asyncio import sleep

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
    answer = await msg.reply(res, parse_mode="HTML")
    await sleep(10)
    await bot_delete_message(answer, msg)


@router.message(Command(commands=["happynewyear"]))
async def new_year(msg: Message):
    await bot_send_message("Ангар dev поздравляет вас с Новым Годом и дарит вам этого ебейшего бота. С Новым годом, братья ❤️‍🔥🥳🎉")


@router.message(F.text.contains("@all"))
async def mention_all(msg: Message):
    members = await Statistics.all().values_list('id', flat=True)
    print(members)
    text = ""
    for user_id in members:
        usr = (await bot_get_member(user_id)).user
        text += usr.mention_html(usr.full_name) + " "
    await msg.answer(text, parse_mode='html')