from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data_pipeline.pipeline import run_pipeline
import logging

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(run_pipeline, "interval", hours=6)
    logging.info("Data fetched")
    scheduler.start()