from random import choice

from aiogram import Bot

from ..db.crud import stats
from ..settings import get_settings
from .schemas import StatsBase

settings = get_settings()

pohui_phrases = [
    "Господи, как же похуй",
    "Поебать",
    "Кристаллически похуй",
    "Индифферентно",
    "Индифферентно в полной мере",
    "Похуй",
    "Кому то не похуй?",
    "Похую",
    "Похуям",
    "Рубиново насрать",
    "Экстра похуй",
    "МЕГА похуй",
    "Похуй+Поебать",
]

words = {
    "talk_stats": "Разгоны",
    "messages": "Сообщения",
    "voices": "Голосовых",
    "video_notes": "Кружочки",
    "stickers": "Cтикеры",
    "photos": "Фото",
    "videos": "Видео",
}


def stats_format(stats: StatsBase):
    row, stat = [], stats.dict()
    for k in stat.keys():
        if k in words.keys() and k != "talk_stats":
            row.append(f"{words[k]}: {stat[k]}")
    row.sort(key=len, reverse=True)
    row.insert(0, "<b>Твоя активность, сучка:</b>\n")
    row.insert(1, f"{words['talk_stats']}: {stat['talk_stats']} 🔥")
    return "\n".join(row)


async def mention_all(bot: Bot) -> list:
    members = await stats.all("id", values_list=True)
    mentions = []
    members.remove(1087968824)
    for user_id in members:
        usr = (await bot.get_chat_member(settings.ANGAR_ID, user_id)).user
        mentions.append(usr.mention_html(usr.full_name))
    return mentions


def rand_pohui() -> str:
    return choice(pohui_phrases)
