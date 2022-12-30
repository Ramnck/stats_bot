from aiogram.types import ContentType, Message

from ..db.crud import stats
from ..settings import get_settings
from ..tools.file_manager import read_chat, update_bot_chat
from time import monotonic
from logging import getLogger


logger = getLogger("logic.stats_logic")

settings = get_settings()
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
    try:
        await stats.update_field(user["id"], fields[msg.content_type])
    except KeyError:
        logger.error("KeyError: Unknown filetype!")


async def _check_user(msg: Message, chat: dict, chat_name: str) -> True | False:
    user_id = msg.from_user.id
    if not msg.from_user.is_bot and chat["user_id"] != user_id:
        if str(user_id) not in chat["diff_users"].keys():
            chat["diff_users"][str(user_id)] = 0
            await update_bot_chat(chat_name, {"diff_users": chat["diff_users"]})
    return len(chat["diff_users"].keys()) > 0


async def _check_msg_count(msg: Message, chat: dict, chat_name: str) -> True | False:
    if not msg.from_user.is_bot and msg.from_user.id != chat["user_id"]:
        chat["diff_users"][str(msg.from_user.id)] += 1
        await update_bot_chat(chat_name, {"diff_users": chat["diff_users"]})
    return sum(chat["diff_users"].values()) > 5


async def analyze_talk(msg: Message):
    chat_name, msg_time = str(msg.chat.id), msg.date.timestamp()
    chat = await read_chat(chat_name)
    if not chat is None:

        if not chat["last_msg_time"]:
            await update_bot_chat(chat_name, {"last_msg_time": msg_time})

        if monotonic() - chat["last_msg_time"] > settings.TALK_EXPIRE:
            await update_bot_chat(
                chat_name, {"analysis": False, "user_id": 0, "diff_users": {}}
            )

        if msg_time - chat["last_msg_time"] > settings.TALK_START or chat["analysis"]:
            if not chat["analysis"]:
                await update_bot_chat(
                    chat_name, {"analysis": True, "user_id": msg.from_user.id}
                )
                chat["user_id"] = msg.from_user.id
            if await _check_user(msg, chat, chat_name) and await _check_msg_count(
                msg, chat, chat_name
            ):
                await stats.update_field(chat["user_id"], "talk_stats")
                await update_bot_chat(
                    chat_name, {"analysis": False, "user_id": 0, "diff_users": {}}
                )
        await update_bot_chat(chat_name, {"last_msg_time": msg_time})
