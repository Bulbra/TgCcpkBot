from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

load_dotenv()

import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from db import crud
from handlers.registry_handler import router as registry_router
from handlers.info_handler import router as info_router
from handlers.subs_handler import router as subs_router
from aiogram.client.session.base import BaseSession
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def on_startup(dp: Dispatcher, bot: Bot):
    logging.info('Starting up the bot...')
    await crud.init_all_tables()
    logging.info('All tables initialized.')


async def main():
    file_path = Path("working_proxies.txt")
    if not file_path.is_file():
        print("PROXY IS NONE")
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        proxy = file.readline().strip()
    session = AiohttpSession(proxy=proxy)
    dp = Dispatcher()
    dp.include_router(registry_router)
    dp.include_router(info_router)
    dp.include_router(subs_router)
    bot = Bot(token=os.getenv("BOT_TOKEN"), session=session)

    dp.startup.register(lambda: asyncio.run(on_startup(dp, bot)))

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
