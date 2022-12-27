from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from ..db.models import Statistics

router = Router()


@router.message((F.chat.title == "Ангар без цензуры") | (F.chat.title == "ПРОДА"))
async def count_entities(msg: Message):
    stat = (await Statistics.get_or_create(id=msg.from_user.id))[0]
    message = msg.text
    voice = msg.voice
    video_note = msg.video_note
    sticker = msg.sticker
    photo = msg.photo
    video = msg.video

    if message:
        stat.messages += 1
    if voice:
        stat.voices += 1
    if video_note:
        stat.video_notes += 1
    if sticker:
        stat.stickers += 1
    if photo:
        stat.photos += 1
    if video:
        stat.videos += 1

    await stat.save()
