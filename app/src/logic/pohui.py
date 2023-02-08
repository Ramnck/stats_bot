from aiogram import Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..tools.file_manager import read_chat, update_bot_chat
from ..tools.formatter import rand_pohui


class Menu(StatesGroup):
    pohui = State()
    ne_pohui = State()


async def set_pohui(chat_id: int | str, member_id: int | str) -> str | None:
    chat_id, member_id = str(chat_id), str(member_id)
    chat = await read_chat(chat_id)
    status = None
    if member_id in chat["pohui"]:
        status = "Already pohui"
    else:
        chat["pohui"].append(member_id)
    await update_bot_chat(chat_id, chat)
    return status


async def unset_pohui(chat_id: int | str, member_id: int | str) -> str | None:
    chat_id, member_id = str(chat_id), str(member_id)
    chat = await read_chat(chat_id)
    status = None
    if member_id not in chat["pohui"]:
        status = "Already nepohui"
    else:
        chat["pohui"].remove(member_id)
    await update_bot_chat(chat_id, chat)
    return status


async def analyze_pohui(msg: Message, bot: Bot):
    chat_name = str(msg.chat.id)
    chat = await read_chat(chat_name)
    if not chat["analysis"]:
        if chat["pohui_msg_id"]:
            await bot.delete_message(chat_name, chat["pohui_msg_id"])
            chat["pohui_msg_id"] = 0
        chat["pohui_count"] = 0

    if chat["pohui_msg_id"] == 0 and str(msg.from_user.id) in chat["pohui"]:
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text=f"{rand_pohui()}", callback_data="+pohui")
        pohui_msg = await bot.send_message(
            chat_name, f"{rand_pohui()}\nx 0", reply_markup=keyboard.as_markup()
        )
        chat["pohui_msg_id"] = pohui_msg.message_id
    await update_bot_chat(chat_name, chat)


async def get_count(chat_id: str | int) -> int:
    chat = await read_chat(str(chat_id))
    return chat["pohui_count"]


async def set_count(chat_id: str | int, count: int) -> None:
    await update_bot_chat(str(chat_id), {"pohui_count": count})
