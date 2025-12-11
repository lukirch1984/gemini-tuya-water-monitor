# API Reference

The backend provides a RESTful API for interacting with the system. The API is automatically documented using OpenAPI and Swagger UI.

**For a live, interactive API documentation, please run the application and navigate to:**

> `http://localhost:8000/docs`

## Endpoints

### Get Latest Data

*   **GET** `/api/v1/data/latest`

    Retrieves the most recent data point recorded from the water quality monitor. This is the primary endpoint used by the LILYGO hardware display.

    **Response (200 OK)**
    ```json
    {
      "ph": 7.2,
      "temperature": 25.1,
      "tds": 345,
      "ec": 690,
      "timestamp": "2023-10-27T10:00:00Z"
    }
    ```
    If no data is available yet, it will return a model with `null` values.

## Data Models

### `WaterData`

Represents a single snapshot of water quality data.

| Field       | Type      | Description                   |
|-------------|-----------|-------------------------------|
| `ph`          | `float`   | The pH level.                 |
| `temperature` | `float`   | The temperature in Celsius.   |
| `tds`         | `float`   | Total Dissolved Solids.       |
| `ec`          | `float`   | Electrical Conductivity.      |
| `timestamp`   | `string`  | The UTC timestamp of the reading. |
