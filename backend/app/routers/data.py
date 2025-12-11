from fastapi import APIRouter, HTTPException
from app.database import influx_db
from app.models import WaterData

router = APIRouter()

@router.get("/latest", response_model=WaterData)
async def get_latest_data():
    """
    Get the latest water quality data from InfluxDB.
    """
    data = influx_db.get_latest_data("water_quality")
    if not data:
        # Return empty/default if no data found
        return WaterData()
    
    return WaterData(
        ph=data.get("ph"),
        temperature=data.get("temperature"),
        tds=data.get("tds"),
        ec=data.get("ec")
    )
