# Getting Started

This guide provides a step-by-step walkthrough to get your Tuya Water Quality Monitor up and running.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Docker & Docker Compose**: For running the server-side stack (Backend, Database, Grafana).
*   **Git**: For cloning the repository.
*   **Python 3.9+**: For running local helper scripts.
*   **A Tuya-compatible Water Quality Monitor**.

## Step 1: Obtain Tuya Device Credentials

This is the most critical step. To communicate with your device locally, you need three pieces of information:

1.  **Device ID**
2.  **IP Address**
3.  **Local Key**

The **IP Address** and **Device ID** can be found easily using the `scan_tuya.py` script included in this project:

```bash
pip install tinytuya
python scan_tuya.py
```

The **Local Key** is a secret key that the device uses to encrypt and decrypt local traffic. Obtaining it requires linking your device to a free Tuya IoT Developer Account.

> **Note:** The process for getting the Local Key can change. We recommend following the detailed, up-to-date guides provided by the `tinytuya` project or searching for "get tuya local key".

## Step 2: Configure the Project

1.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/tuya-water-monitor.git
    cd tuya-water-monitor
    ```

2.  Create a `.env` file inside the `backend/` directory. This file will hold your secrets.
    ```
    backend/.env
    ```

3.  Add your device credentials and database configuration to the `.env` file:
    ```dotenv
    # Tuya Device
    TUYA_DEVICE_ID="YOUR_DEVICE_ID"
    TUYA_IP_ADDRESS="YOUR_DEVICE_IP"
    TUYA_LOCAL_KEY="YOUR_LOCAL_KEY"

    # InfluxDB (can be left as default if using docker-compose)
    INFLUXDB_URL="http://influxdb:8086"
    INFLUXDB_TOKEN="my-super-secret-auth-token"
    INFLUXDB_ORG="my-org"
    INFLUXDB_BUCKET="water_monitor"
    ```

## Step 3: Launch the Stack

With Docker running, launch the entire application stack:

```bash
docker-compose up -d --build
```

This command will:
*   Build the FastAPI backend image.
*   Start the `backend`, `influxdb`, and `grafana` containers.
*   The backend will automatically start polling your device.

## Step 4: Verify Everything is Working

*   **API**: Open your browser and navigate to `http://localhost:8000/docs`. You should see the FastAPI interactive API documentation.
*   **InfluxDB**: Navigate to `http://localhost:8086`. You can use the credentials from `docker-compose.yml` to log in and explore the `water_monitor` bucket. You should see data points arriving.
*   **Grafana**: Navigate to `http://localhost:3000`. Log in (default `admin`/`admin`) and configure a new InfluxDB data source to start building dashboards.

Congratulations! Your monitoring system is now live. The next step is to set up your [Hardware Display](./hardware.md).
