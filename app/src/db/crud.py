from logging import getLogger

from tortoise.exceptions import ValidationError
from tortoise.expressions import F

from ..tools.schemas import StatsBase
from .models import GetStats, Statistics

logger = getLogger("db.crud")


class CRUDStats:
    def __init__(self, model: Statistics) -> None:
        self.model = model

    async def get_or_create(self, id: int) -> StatsBase:
        stats = await self.model.get_or_create(id=id)
        return await GetStats.from_tortoise_orm(stats[0])

    async def update_field(self, id: int, field: str) -> StatsBase | None:
        try:
            await self.model.filter(id=id).update(**{field: F(field) + 1})
        except ValidationError:
            logger.error("ValidationError: stats update alidation")

    async def all(self, *fields, values_list = False) -> dict | list:
        members = self.model.all()
        if values_list:
            members = await members.values_list(*fields, flat=True if len(fields) == 1 else False)
        else:
            members = await members.values(*fields)
        return members

stats = CRUDStats(Statistics)
