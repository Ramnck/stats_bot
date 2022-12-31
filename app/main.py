import asyncio
import logging

from aiogram import Bot, Dispatcher
from src.db.database import init_db
from src.settings import get_settings
from src.handlers import commands, statictics, voice

from src.base import bot

logging.basicConfig(level=logging.INFO)

async def main():
    settings = get_settings()
    
    await init_db(settings)

    dp = Dispatcher()

    dp.include_router(commands.router)

    dp.include_router(voice.router)

    dp.include_router(statictics.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
