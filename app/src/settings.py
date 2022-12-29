from pydantic import BaseSettings
from functools import lru_cache
from decouple import config
from pathlib import Path


class Settings(BaseSettings):
    CHATS = ["Ангар без цензуры", "ПРОДА"]
    USERS = []
    # 30 minutes
    TALK_EXPIRE = 60 * 15

    TOKEN = config("TOKEN")
    POSTGRES_DB = config("POSTGRES_DB")
    POSTGRES_USER = config("POSTGRES_USER")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")

    TMP_DIR: Path = Path('.').absolute() / 'tmp'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
