from functools import lru_cache

from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    CHATS = ["Ангар без цензуры", "ПРОДА"]
    USERS = []
    # 30 minutes 60 * 15
    TALK_EXPIRE = 60 * 15

    TOKEN = config("TOKEN")
    POSTGRES_DB = config("POSTGRES_DB")
    POSTGRES_USER = config("POSTGRES_USER")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
