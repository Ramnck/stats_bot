from ..db.crud import stats
from ..tools.schemas import StatsBase, UpdateStats
from aiogram.types import ContentType, Message


def exclude(obj: StatsBase, field: str) -> UpdateStats:
    del obj[field]
    return UpdateStats(**obj)


fields = {
    ContentType.TEXT: "messages",
    ContentType.VOICE: "voices",
    ContentType.VIDEO_NOTE: "video_notes",
    ContentType.STICKER: "stickers",
    ContentType.PHOTO: "photos",
    ContentType.VIDEO: "videos",
}


async def update_stats(msg: Message):
    user = dict(await stats.get_or_create(msg.from_user.id))
    user[fields[msg.content_type]] += 1
    await stats.update_field(user["id"], exclude(user, "id"))
