from functools import lru_cache
from pathlib import Path

from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    CHATS = ["Ангар без цензуры", "ПРОДА"]
    USERS = []

    TALK_EXPIRE = 60 * 40
    TALK_START = 60 * 15

    # ANGAR_ID = -1001661456708
    ANGAR_ID = -1001873958874
    TOKEN = config("TOKEN")
    POSTGRES_DB = config("POSTGRES_DB")
    POSTGRES_USER = config("POSTGRES_USER")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")

    TMP_DIR: Path = Path(".").absolute() / "tmp"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
