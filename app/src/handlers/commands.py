from asyncio import sleep

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.crud import stats
from ..settings import get_settings
from ..tools.formatter import mention_all, stats_format

router = Router()
settings = get_settings()


@router.message(Command(commands=["start"]))
async def start(msg: Message):
    await msg.answer("Тебе не понадобится этот бот")


@router.message(Command(commands=["help"]))
async def help(msg: Message):
    await msg.answer("Если ты не знаешь что это за бот значит он тебе не нужен")


@router.message(Command(commands=["info"]))
async def info(msg: Message, bot: Bot):
    user_stats = await stats.get_or_create(msg.from_user.id)
    res = stats_format(user_stats)
    answer = await msg.reply(res, parse_mode="HTML")
    if msg.chat.id == settings.ANGAR_ID:
        await sleep(10)
        await bot.delete_message(msg.chat.id, answer)
        await bot.delete_message(msg.chat.id, msg)


@router.message(Command(commands=["happynewyear"]))
async def new_year(msg: Message, bot: Bot):
    await bot.send_message(
        settings.ANGAR_ID,
        "Ангар dev поздравляет вас с Новым Годом и дарит вам этого ебейшего бота. С Новым годом, братья ❤️‍🔥🥳🎉",
    )


@router.message(Command(commands=["infoall"]))
async def info_all(msg: Message, bot: Bot):
    if msg.chat.id == settings.ANGAR_ID:
        await msg.reply("В ангар срать не буду, спроси в лс")
    else:
        mentions = await mention_all(bot)
        for mention in mentions:
            user_stats = await stats.get_or_create(
                int(mention[mention.index("id=") + 3 : mention.index('">')])
            )
            res = stats_format(user_stats)
            res = res.replace("Твоя активность, сучка", "Активность " + mention)
            await msg.reply(res, parse_mode="HTML")


@router.message(F.text.contains("@all"))
async def all_command(msg: Message):
    text = await mention_all()
    text = " ".join(text)
    await msg.answer(text, parse_mode="HTML")
