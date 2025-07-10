from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.ticketmaster_service import transform_all
import logging

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(transform_all, "interval", hours=6)
    logging.info("Data fetched")
    scheduler.start()