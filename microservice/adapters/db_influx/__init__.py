"""General DB."""
import logging

from influxdb_client import InfluxDBClient, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

from microservice.core.exceptions import NoConfigFile
from microservice.core.interfaces.db import DBAdapterTimesSeries
from microservice.core.model import InfluxData
# from .exceptions import TokenError


class DBTimeSeries(DBAdapterTimesSeries):
    """Database connection implementation class."""

    db = None
    default_bucket = None

    def __init__(self, connection_string: str, token: str, default_org: str, default_bucket: str):
        self.default_bucket = default_bucket
        if self.db is None:
            self.connect(connection_string, token, default_org)
        logging.info('db time_series object created')

    def connect(self, connection_string: str, token: str, default_org: str):
        if connection_string is None:
            logging.critical('No config defined (time_Series db)')
            raise NoConfigFile()
        try:
            self.db = InfluxDBClient(
                url=connection_string,
                token=token,
                org=default_org
            )
            health = self.db.health()
            if health.status == "pass":
                logging.info(f'Connection success! health: {health}')
            else:
                logging.error(f'Connection failure: {health.message}!')
        except Exception as e:
            logging.error('error in connection string (time_series):', e)
            raise

    def save_measurement(self, data: InfluxData):
        write_api = self.db.write_api(write_options=SYNCHRONOUS)

        measure = {
            'measurement': data.measurement,
            'tags': data.tags,
            'fields': data.fields,
            'time': data.time
        }

        write_api.write(bucket=self.default_bucket, record=measure)

    def get_measurement(self, measurement: str, start_time: str = '-9d'):
        end_time = str('now()')
        query_api = self.db.query_api()
        query = f'from(bucket:"{self.default_bucket}")\
            |> range(start: {start_time}, stop: {end_time})\
            |> filter(fn:(r) => r._measurement == "{measurement}" )'
            # |> filter(fn:(r) => r._measurement == "{measurement}" )\
            # |> filter(fn: (r) => r.host_ip == "10.224.31.136")'
        response = query_api.query(query=query)
        return response

    def save_measurement_batch(self, data: [InfluxData]):
        with self.db as _client:
            with _client.write_api(write_options=WriteOptions(batch_size=500,
                                                              flush_interval=10_000,
                                                              jitter_interval=2_000,
                                                              max_retries=5,
                                                              max_retry_delay=30_000,
                                                              exponential_base=2)) as _write_client:

                _write_client.write(bucket=self.default_bucket, record=data)
