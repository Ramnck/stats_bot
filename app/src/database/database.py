from tortoise import Tortoise
from decouple import config

DB_URL = "postgres://{}:{}@{}:{}/{}".format(
    config('POSTGRES_USER'),
    config('POSTGRES_PASSWORD'),
    config('DB_HOST'),
    config('DB_PORT'),
    config('POSTGRES_DB'),
)

async def init_db():
    
    await Tortoise.init(
        db_url=DB_URL,
        modules = {"models" : ['src.database.models']}
    )

    await Tortoise.generate_schemas()