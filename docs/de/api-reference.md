# API-Referenz

Das Backend stellt eine RESTful-API zur Interaktion mit dem System bereit. Die API wird automatisch mit OpenAPI und Swagger UI dokumentiert.

**Für eine live, interaktive API-Dokumentation führen Sie bitte die Anwendung aus und navigieren Sie zu:**

> `http://localhost:8000/docs`

## Endpunkte

### Neueste Daten abrufen

*   **GET** `/api/v1/data/latest`

    Ruft den zuletzt vom Wasserqualitätsmonitor aufgezeichneten Datenpunkt ab. Dies ist der primäre Endpunkt, der von der LILYGO-Hardwareanzeige verwendet wird.

    **Antwort (200 OK)**
    ```json
    {
      "ph": 7.2,
      "temperature": 25.1,
      "tds": 345,
      "ec": 690,
      "timestamp": "2023-10-27T10:00:00Z"
    }
    ```
    Wenn noch keine Daten verfügbar sind, wird ein Modell mit `null`-Werten zurückgegeben.

## Datenmodelle

### `WaterData`

Stellt eine einzelne Momentaufnahme der Wasserqualitätsdaten dar.

| Feld          | Typ       | Beschreibung                  |
|---------------|-----------|-------------------------------|
| `ph`          | `float`   | Der pH-Wert.                  |
| `temperature` | `float`   | Die Temperatur in Celsius.    |
| `tds`         | `float`   | Gesamt gelöste Feststoffe.    |
| `ec`          | `float`   | Elektrische Leitfähigkeit.    |
| `timestamp`   | `string`  | Der UTC-Zeitstempel der Messung.|
