from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WaterData(BaseModel):
    ph: Optional[float] = None
    temperature: Optional[float] = None
    tds: Optional[float] = None  # Total Dissolved Solids
    ec: Optional[float] = None   # Electrical Conductivity
    timestamp: datetime = datetime.utcnow()

class AlarmConfig(BaseModel):
    parameter: str
    min_val: Optional[float]
    max_val: Optional[float]
    enabled: bool = True
