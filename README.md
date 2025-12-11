# Tuya Water Quality Monitor

This project monitors water quality using Tuya-compatible sensors, stores the data in InfluxDB, and visualizes it via Grafana and a LILYGO T4 display.

## Features
- **Data Acquisition**: Reads from Tuya devices via `tinytuya`.
- **Storage**: InfluxDB time-series database.
- **API**: RESTful API using FastAPI.
- **Visualization**: Grafana Dashboards & LILYGO T4 Display.
- **Alerting**: Configurable thresholds.

## Quick Start
1.  Setup `.env` file in `backend/`.
2.  Run `docker-compose up -d`.
3.  Access docs at `http://localhost:8000/docs`.

## Documentation
Full documentation is available in the `docs/` folder.
