from aiogram import Router, F
from aiogram.types import Message
from ..database.models import Statistics
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=['info']))
async def info(msg: Message):
    stats = await Statistics.filter(id=msg.from_user.id).first().values_list('messages', 'voices', 'video_notes', 'stickers', 'photos', 'videos')
    if not stats:
        stats = [0]*6
    await msg.reply("""Вот твоя статистика:
Отправлено:
{} сообщений,
{} голосовых,
{} кружочков,
{} стикеров,
{} фото,
{} видео""".format(*stats))

# @router.message(F.sticker)
# async def test(msg: Message):
#     msg.reply("бля это ж стикер")


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