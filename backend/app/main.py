from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.routers import data
from app.services.tuya_service import tuya_monitor
from apscheduler.schedulers.background import BackgroundScheduler
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def scheduled_job():
    logger.info("Polling Tuya Device...")
    tuya_monitor.poll_data()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Tuya Water Monitor API...")
    if settings.TUYA_DEVICE_ID:
        scheduler.add_job(scheduled_job, 'interval', seconds=60)
        scheduler.start()
    yield
    # Shutdown
    scheduler.shutdown()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.include_router(data.router, prefix=settings.API_V1_STR + "/data", tags=["data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuya Water Monitor API"}
