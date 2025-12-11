import tinytuya
import time
import logging
from app.core.config import settings
from app.database import influx_db

logger = logging.getLogger(__name__)

class TuyaMonitor:
    def __init__(self):
        self.device = None
        if settings.TUYA_DEVICE_ID and settings.TUYA_LOCAL_KEY:
            try:
                self.device = tinytuya.OutletDevice(
                    dev_id=settings.TUYA_DEVICE_ID,
                    address=settings.TUYA_IP_ADDRESS,
                    local_key=settings.TUYA_LOCAL_KEY,
                    version=settings.TUYA_VERSION
                )
                logger.info(f"Initialized Tuya Device: {settings.TUYA_DEVICE_ID}")
            except Exception as e:
                logger.error(f"Failed to initialize Tuya device: {e}")
        else:
            logger.warning("Tuya credentials not set. Running in mock/passive mode.")

    def poll_data(self):
        if not self.device:
            return None

        try:
            data = self.device.status()
            logger.info(f"Tuya Data: {data}")
            
            # Map DPS to meaningful values. 
            # NOTE: These DPS keys '1', '2', etc. are specific to the hardware.
            # You must check the output of `tinytuya.scan()` or `device.status()` to map correctly.
            dps = data.get('dps', {})
            
            # Example mapping (needs adjustment based on real device)
            parsed_data = {
                "ph": float(dps.get('1', 0)),
                "temperature": float(dps.get('2', 0)),
                "tds": float(dps.get('3', 0)),
                "ec": float(dps.get('4', 0))
            }

            # Write to InfluxDB
            influx_db.write_data(
                measurement="water_quality",
                tags={"device_id": settings.TUYA_DEVICE_ID},
                fields=parsed_data
            )
            return parsed_data
        except Exception as e:
            logger.error(f"Error polling Tuya device: {e}")
            return None

tuya_monitor = TuyaMonitor()
