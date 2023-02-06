import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.db.database import init_db
from src.handlers import commands, statictics, voice
from src.settings import get_settings

logging.basicConfig(level=logging.INFO)


async def main():
    settings = get_settings()

    await init_db(settings)

    bot = Bot(settings.TOKEN)

    dp = Dispatcher()

    dp.include_router(commands.router)

    dp.include_router(voice.router)

    dp.include_router(statictics.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
