from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data_pipeline import pipeline
import logging

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(pipeline(), "interval", hours=6)
    logging.info("Data fetched")
    scheduler.start()