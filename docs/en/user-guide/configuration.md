# Configuration

The application is configured using environment variables. These can be set directly in your shell, but the recommended method is to place them in a `.env` file within the `backend/` directory.

The `docker-compose.yml` file is pre-configured to load variables from this file.

## Backend Configuration

File: `backend/.env`

### Tuya Device Settings
These are the core settings required to connect to your water quality monitor.

`TUYA_DEVICE_ID`
:   **Required**. The unique identifier for your Tuya device.
:   *Example: `ebc123...def456`*

`TUYA_IP_ADDRESS`
:   **Required**. The local IP address of your device. It's recommended to assign a static IP to your device via your router's DHCP settings.
:   *Example: `192.168.1.50`*

`TUYA_LOCAL_KEY`
:   **Required**. The secret key used for local communication.
:   *Example: `a1b2c3d4e5f67890`*

`TUYA_VERSION`
:   The Tuya protocol version number.
:   *Default: `3.3`*

### InfluxDB Settings
These settings tell the backend how to connect to the InfluxDB database. If you are using the standard `docker-compose.yml` setup, the default values should work correctly.

`INFLUXDB_URL`
:   The full URL for the InfluxDB v2 instance.
:   *Default: `http://influxdb:8086`*

`INFLUXDB_TOKEN`
:   The authentication token for InfluxDB. This must match the `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN` in `docker-compose.yml`.
:   *Default: `my-super-secret-auth-token`*

`INFLUXDB_ORG`
:   The organization name in InfluxDB. This must match `DOCKER_INFLUXDB_INIT_ORG`.
:   *Default: `my-org`*

`INFLUXDB_BUCKET`
:   The bucket where data will be stored.
:   *Default: `water_monitor`*

### Alarming Settings (Future Use)
These settings control the (not-yet-implemented) email alerting feature.

`ALARM_EMAIL_ENABLED`
:   Enable or disable email alerts.
:   *Default: `False`*

`ALARM_EMAIL_RECIPIENT`
:   The email address to send alerts to.
:   *Default: `user@example.com`*
