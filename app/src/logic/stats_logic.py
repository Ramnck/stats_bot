from db.models import Statistics, GetStats
from db.crud import stats
from aiogram.types import Message


# async def update_stats(user_id: int, msg: Message):
#     user = await stats.get_or_create(user_id)
