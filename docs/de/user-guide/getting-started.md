# Erste Schritte

Diese Anleitung bietet eine schrittweise Beschreibung, um Ihren Tuya Wasserqualitäts-Monitor in Betrieb zu nehmen.

## Voraussetzungen

Stellen Sie vor Beginn sicher, dass Sie Folgendes installiert haben:

*   **Docker & Docker Compose**: Zum Ausführen des serverseitigen Stacks (Backend, Datenbank, Grafana).
*   **Git**: Zum Klonen des Repositorys.
*   **Python 3.9+**: Zum Ausführen lokaler Hilfsskripte.
*   **Ein Tuya-kompatibler Wasserqualitätsmonitor**.

## Schritt 1: Tuya-Geräteanmeldeinformationen abrufen

Dies ist der kritischste Schritt. Um lokal mit Ihrem Gerät zu kommunizieren, benötigen Sie drei Informationen:

1.  **Geräte-ID (Device ID)**
2.  **IP-Adresse**
3.  **Lokaler Schlüssel (Local Key)**

Die **IP-Adresse** und die **Geräte-ID** können einfach mit dem im Projekt enthaltenen Skript `scan_tuya.py` gefunden werden:

```bash
pip install tinytuya
python scan_tuya.py
```

Der **Local Key** ist ein geheimer Schlüssel, den das Gerät zur Ver- und Entschlüsselung des lokalen Datenverkehrs verwendet. Um ihn zu erhalten, müssen Sie Ihr Gerät mit einem kostenlosen Tuya IoT-Entwicklerkonto verknüpfen.

> **Hinweis:** Der Prozess zum Erhalt des Local Key kann sich ändern. Wir empfehlen, den detaillierten, aktuellen Anleitungen des `tinytuya`-Projekts zu folgen oder nach "get tuya local key" zu suchen.

## Schritt 2: Projekt konfigurieren

1.  Klonen Sie dieses Repository:
    ```bash
    git clone https://github.com/ihr-benutzername/tuya-water-monitor.git
    cd tuya-water-monitor
    ```

2.  Erstellen Sie eine `.env`-Datei im `backend/`-Verzeichnis. Diese Datei wird Ihre Geheimnisse enthalten.
    ```
    backend/.env
    ```

3.  Fügen Sie Ihre Geräteanmeldeinformationen und Datenbankkonfiguration zur `.env`-Datei hinzu:
    ```dotenv
    # Tuya Gerät
    TUYA_DEVICE_ID="IHRE_GERÄTE_ID"
    TUYA_IP_ADDRESS="IHRE_GERÄTE_IP"
    TUYA_LOCAL_KEY="IHR_LOCAL_KEY"

    # InfluxDB (kann als Standard belassen werden, wenn docker-compose verwendet wird)
    INFLUXDB_URL="http://influxdb:8086"
    INFLUXDB_TOKEN="my-super-secret-auth-token"
    INFLUXDB_ORG="my-org"
    INFLUXDB_BUCKET="water_monitor"
    ```

## Schritt 3: Den Stack starten

Starten Sie bei laufendem Docker den gesamten Anwendungsstack:

```bash
docker-compose up -d --build
```

Dieser Befehl wird:
*   Das FastAPI-Backend-Image erstellen.
*   Die Container `backend`, `influxdb` und `grafana` starten.
*   Das Backend beginnt automatisch, Ihr Gerät abzufragen.

## Schritt 4: Überprüfen, ob alles funktioniert

*   **API**: Öffnen Sie Ihren Browser und navigieren Sie zu `http://localhost:8000/docs`. Sie sollten die interaktive API-Dokumentation von FastAPI sehen.
*   **InfluxDB**: Navigieren Sie zu `http://localhost:8086`. Sie können die Anmeldeinformationen aus der `docker-compose.yml` verwenden, um sich anzumelden und das `water_monitor`-Bucket zu erkunden. Sie sollten ankommende Datenpunkte sehen.
*   **Grafana**: Navigieren Sie zu `http://localhost:3000`. Melden Sie sich an (Standard `admin`/`admin`) und konfigurieren Sie eine neue InfluxDB-Datenquelle, um Dashboards zu erstellen.

Herzlichen Glückwunsch! Ihr Überwachungssystem ist jetzt live. Der nächste Schritt ist die Einrichtung Ihres [Hardware-Displays](./hardware.md).
