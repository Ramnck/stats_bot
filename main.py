import logging, asyncio

from aiogram import Bot, Dispatcher
from decouple import config

from handlers import default

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=config("TOKEN"))
    dp = Dispatcher()

    dp.include_router(default.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())