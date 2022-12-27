from .models import Statistics, GetStats
from tools.schemas import StatsBase
from tortoise.exceptions import ValidationError


class CRUDStats:
    def __init__(self, model: Statistics) -> None:
        self.model = model

    async def get_or_create(self, id: int) -> StatsBase:
        stats = await self.model.get_or_create(id=id)
        return await GetStats.from_tortoise_orm(stats)

    async def update_field(self, id: int, schema: StatsBase) -> StatsBase | None:
        try:
            await self.model.filter(id=id).update(**schema.dict())
        except ValidationError:
            print("ALert hui")


stats = CRUDStats(Statistics)
