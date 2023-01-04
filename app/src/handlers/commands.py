from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.crud import stats
from ..db.models import Statistics
from ..tools.formatter import stats_format, mention_all

from ..base import bot_get_member, bot_send_message, bot_delete_message
from ..settings import get_settings
from asyncio import sleep


router = Router()
settings = get_settings()


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


@router.message(Command(commands=["infoall"]))
async def info_all(msg: Message):
    if msg.chat.id == settings.ANGAR_ID:
        await msg.reply("В ангар срать не буду, спроси в лс")
    else:
        mentions = await mention_all()
        for mention in mentions:
            user_stats = await stats.get_or_create(int(mention[mention.index("id=")+3:mention.index('">')]))
            res = stats_format(user_stats)
            res = res.replace("Твоя активность, сучка", "Активность " + mention)
            await msg.reply(res, parse_mode="HTML")


@router.message(F.text.contains("@all"))
async def all_command(msg: Message):
    text = await mention_all()
    text = ' '.join(text)
    await msg.answer(text, parse_mode='HTML')