import logging, asyncio
from aiogram import Dispatcher, Bot
from src.handlers import service, statictics
from src.database.database import init_db
from decouple import config

logging.basicConfig(level=logging.INFO)

async def main():

    await init_db()

    bot = Bot(token=config("TOKEN"))
    dp = Dispatcher()


    dp.include_router(service.router)

    # Include Routers here



    dp.include_router(statictics.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    
    asyncio.run(main())