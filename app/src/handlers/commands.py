from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.models import Statistics

router = Router()


@router.message(Command(commands=["start"]))
async def start(msg: Message):
    await msg.answer("Тебе не понадобится этот бот")


@router.message(Command(commands=["help"]))
async def help(msg: Message):
    await msg.answer("Если ты не знаешь что это за бот значит он тебе не нужен")


# Refactor this
@router.message(Command(commands=["info"]))
async def info(msg: Message):
    stats = (
        await Statistics.filter(id=msg.from_user.id)
        .first()
        .values_list(
            "messages", "voices", "video_notes", "stickers", "photos", "videos"
        )
    )
    if not stats:
        stats = [0] * 6
    await msg.reply(
        """Вот твоя статистика:
Отправлено:
{} сообщений,
{} голосовых,
{} кружочков,
{} стикеров,
{} фото,
{} видео""".format(
            *stats
        )
    )
