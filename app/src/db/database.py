from decouple import config
from tortoise import Tortoise
from ..settings import Settings


async def init_db(settings: Settings):
    DB_URL = "postgres://{}:{}@{}:{}/{}".format(
        settings.POSTGRES_USER,
        settings.POSTGRES_PASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.POSTGRES_DB,
    )
    await Tortoise.init(db_url=DB_URL, modules={"models": ["src.db.models"]})
    await Tortoise.generate_schemas()
