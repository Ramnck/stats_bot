from .schemas import StatsBase
from ..db.crud import stats
from ..base import bot_get_member

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

async def mention_all() -> str:
    members = await stats.all('id', values_list=True)
    mentions = []
    for user_id in members:
        usr = (await bot_get_member(user_id)).user
        mentions.append(usr.mention_html(usr.full_name))
    return mentions