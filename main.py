import asyncio
import sys, os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

async def main(token: str):
    bot = Bot(token=os.get)

if __name__ == "__main__":
    load_dotenv()
    
    token = ''
    if len(sys.argv) > 1 and sys.argv[1] in ['-t','t','-test','test','-d', 'd', 'dev', '-dev']:
        token = os.getenv('TOKEN_DEV')
    else:
        token = os.getenv('TOKEN')

    asyncio.run(main(token))
    