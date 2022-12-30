from .schemas import StatsBase

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
