from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class InfluxClient:
    def __init__(self):
        self.client = InfluxDBClient(
            url=settings.INFLUXDB_URL,
            token=settings.INFLUXDB_TOKEN,
            org=settings.INFLUXDB_ORG
        )
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()

    def write_data(self, measurement: str, tags: dict, fields: dict):
        try:
            point = Point(measurement)
            for key, value in tags.items():
                point = point.tag(key, value)
            for key, value in fields.items():
                point = point.field(key, value)
            
            self.write_api.write(bucket=settings.INFLUXDB_BUCKET, org=settings.INFLUXDB_ORG, record=point)
        except Exception as e:
            logger.error(f"Failed to write to InfluxDB: {e}")

    def get_latest_data(self, measurement: str):
        query = f'''
        from(bucket: "{settings.INFLUXDB_BUCKET}")
        |> range(start: -1h)
        |> filter(fn: (r) => r["_measurement"] == "{measurement}")
        |> last()
        '''
        try:
            result = self.query_api.query(org=settings.INFLUXDB_ORG, query=query)
            data = {}
            for table in result:
                for record in table.records:
                    data[record.get_field()] = record.get_value()
            return data
        except Exception as e:
            logger.error(f"Failed to query InfluxDB: {e}")
            return {}

influx_db = InfluxClient()
