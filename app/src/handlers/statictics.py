from aiogram import F, Router
from aiogram.types import Message
from ..logic.stats_logic import update_stats
from ..filters import is_based

router = Router()


@router.message(~F.func(lambda msg: is_based(msg)))
async def count_entities(msg: Message):
    await update_stats(msg)
