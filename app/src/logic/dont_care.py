from aiogram import Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..tools.file_manager import read_chat, update_bot_chat
from ..tools.formatter import rand_dont_care


class Menu(StatesGroup):
    dont_care = State()
    ne_dont_care = State()


async def set_dont_care(chat_id: int | str, member_id: int | str) -> str | None:
    chat_id, member_id = str(chat_id), str(member_id)
    chat = await read_chat(chat_id)
    status = None
    if member_id in chat["dont_care"]:
        status = "Already dont_care"
    else:
        chat["dont_care"].append(member_id)
    await update_bot_chat(chat_id, chat)
    return status


async def unset_dont_care(chat_id: int | str, member_id: int | str) -> str | None:
    chat_id, member_id = str(chat_id), str(member_id)
    chat = await read_chat(chat_id)
    status = None
    if member_id not in chat["dont_care"]:
        status = "Already nedont_care"
    else:
        chat["dont_care"].remove(member_id)
    await update_bot_chat(chat_id, chat)
    return status


async def analyze_dont_care(msg: Message, bot: Bot):
    chat_name = str(msg.chat.id)
    chat = await read_chat(chat_name)
    if chat["analysis"]:
        if chat["dont_care_msg_id"]:
            await bot.delete_message(chat_name, chat["dont_care_msg_id"])
            chat["dont_care_msg_id"] = 0
        chat["dont_care_count"] = 0

    if chat["dont_care_msg_id"] == 0 and str(msg.from_user.id) in chat["dont_care"]:
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text=f"{rand_dont_care()}", callback_data="+dont_care")
        dont_care_msg = await bot.send_message(
            chat_name,
            f"{rand_dont_care()}\nx 0",
            reply_markup=keyboard.as_markup(),
            reply_to_message_id=msg.message_id,
        )
        chat["dont_care_msg_id"] = dont_care_msg.message_id
    await update_bot_chat(chat_name, chat)


async def get_count(chat_id: str | int) -> int:
    chat = await read_chat(str(chat_id))
    return chat["dont_care_count"]


async def set_count(chat_id: str | int, count: int) -> None:
    await update_bot_chat(str(chat_id), {"dont_care_count": count})
