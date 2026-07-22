from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from aiogram import Bot

from db.crud import get_all_user_subs_with_join
from ccpk_class import get_all_free_trains
import logging

logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler

def init_scheduler(bot: Bot, check_interval = 300):
    scheduler.add_job(trigger=IntervalTrigger(seconds=check_interval),
                      func=check_all_subs,
                      args=[bot],
                      max_instances=1,
                      replace_existing=True)
    logger.info("планировщик инициализирован")

def start_scheduler():
    scheduler.start()
    logger.info("gпланировщик запущен")

def stop_scheduler():
    scheduler.shutdown()
    logger.info("планировщик сдох")

async def check_all_subs(bot: Bot):
    subs = await get_all_user_subs_with_join()
    print(subs)
    trains = get_all_free_trains()
    for train in trains:
        for sub in subs:
            if train.initialStationCode == sub.from_station_id and train.finalStationCode == sub.to_station_id:
                await bot.send_message(sub.user_id, f"{train.trainName}, {train.trainNumber} отправляется в {train.departureDateTime}")
