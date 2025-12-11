# Tuya Water Quality Monitor

## Project Overview
This project is a comprehensive IoT solution for monitoring water quality (pH, Temperature, TDS/EC) using Tuya-compatible hardware. It bridges local device control with a modern data stack, allowing for real-time monitoring without reliance on external cloud services for data history.

**Key Technologies:**
*   **Language:** Python 3.11+ (Backend), C++/Arduino (Firmware)
*   **Frameworks:** FastAPI (API), PlatformIO (Embedded)
*   **Database:** InfluxDB v2 (Time-series data)
*   **Visualization:** Grafana (Dashboards), LILYGO T4 (Physical Display)
*   **Protocol:** Tuya Local Protocol (UDP/TCP via `tinytuya`)
*   **Documentation:** MkDocs (Material Theme, Bilingual EN/DE)

## Architecture
1.  **Data Source:** A Tuya-compatible water quality tester.
2.  **Ingestion:** The **Backend** (`tinytuya`) polls the device locally at set intervals.
3.  **Storage:** Data is normalized and written to **InfluxDB**.
4.  **Presentation:** 
    *   **Grafana** queries InfluxDB for historical trends.
    *   **LILYGO T4** fetches real-time data from the Backend API.

## Directory Structure
*   `backend/`: Python FastAPI application.
    *   `app/`: Source code.
    *   `tests/`: Pytest unit tests.
*   `docker/`: Data volumes for InfluxDB and Grafana.
*   `docs/`: MkDocs source files (English and German).
    *   `assets/firmware/`: Contains compiled binaries for the Web Flasher.
*   `firmware/`: PlatformIO project for the LILYGO T4 display.
*   `scan_tuya.py`: Utility script to discover Tuya devices on the local network.
*   `docker-compose.yml`: Orchestration for the full server stack.

## Building and Running

### 1. Device Discovery
Before running the stack, you need the Tuya Device ID and IP.
```bash
pip install tinytuya
python scan_tuya.py
```
*Note: You will also need the `LOCAL_KEY`, which requires a one-time setup via the Tuya IoT Platform.*

### 2. Configuration
Create a `.env` file in `backend/` or configure environment variables in `docker-compose.yml`:
*   `TUYA_DEVICE_ID`
*   `TUYA_IP_ADDRESS`
*   `TUYA_LOCAL_KEY`
*   `INFLUXDB_...` (Standard InfluxDB credentials)

### 3. Server Stack
Run the application using Docker Compose:
```bash
docker-compose up -d --build
```
*   **API:** http://localhost:8000/docs
*   **Grafana:** http://localhost:3000 (Default User/Pass: `admin`/`admin` - check docker-compose)
*   **InfluxDB:** http://localhost:8086

### 4. Firmware (LILYGO T4)
**Option A: Web Flasher**
1.  Serve the docs: `mkdocs serve`
2.  Navigate to the "Flasher" page in the browser.
3.  Connect the device via USB and flash (requires a compiled `firmware.bin` in `docs/assets/firmware/`).

**Option B: PlatformIO**
1.  Open the `firmware/` directory in VS Code with the PlatformIO extension.
2.  Modify `src/main.cpp` with your WiFi credentials and Server IP.
3.  Run "Upload".

## Development Conventions

*   **Testing:** Run `pytest` in the `backend/` directory.
*   **Documentation:** Documentation is bilingual. Edit `docs/en/` and `docs/de/` correspondingly.
*   **Dependency Management:** 
    *   Python: `backend/requirements.txt`
    *   C++: `firmware/platformio.ini`
