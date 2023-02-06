from aiogram import Bot, F, Router
from aiogram.types import Message

from ..logic.pohui import analyze_pohui
from ..logic.privacy import is_based
from ..logic.stats import analyze_talk, update_stats

router = Router()


@router.message(~F.func(lambda msg: is_based(msg)))
async def count_entities(msg: Message, bot: Bot):
    await update_stats(msg)
    await analyze_talk(msg)
    await analyze_pohui(msg, bot)
