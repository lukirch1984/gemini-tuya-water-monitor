from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "Tuya Water Monitor"
    API_V1_STR: str = "/api/v1"
    
    # InfluxDB
    INFLUXDB_URL: str = "http://influxdb:8086"
    INFLUXDB_TOKEN: str = "my-super-secret-auth-token"
    INFLUXDB_ORG: str = "my-org"
    INFLUXDB_BUCKET: str = "water_monitor"

    # Tuya Device
    TUYA_DEVICE_ID: str = ""
    TUYA_IP_ADDRESS: str = ""
    TUYA_LOCAL_KEY: str = ""
    TUYA_VERSION: float = 3.3
    
    # Alarming
    ALARM_EMAIL_ENABLED: bool = False
    ALARM_EMAIL_RECIPIENT: str = "user@example.com"

    class Config:
        env_file = ".env"

settings = Settings()
