# Konfiguration

Die Anwendung wird über Umgebungsvariablen konfiguriert. Diese können direkt in Ihrer Shell gesetzt werden, aber die empfohlene Methode ist, sie in einer `.env`-Datei im `backend/`-Verzeichnis zu platzieren.

Die `docker-compose.yml`-Datei ist so vorkonfiguriert, dass sie Variablen aus dieser Datei lädt.

## Backend-Konfiguration

Datei: `backend/.env`

### Tuya-Geräteeinstellungen
Dies sind die Kerneinstellungen, die für die Verbindung zu Ihrem Wasserqualitätsmonitor erforderlich sind.

`TUYA_DEVICE_ID`
:   **Erforderlich**. Die eindeutige Kennung für Ihr Tuya-Gerät.
:   *Beispiel: `ebc123...def456`*

`TUYA_IP_ADDRESS`
:   **Erforderlich**. Die lokale IP-Adresse Ihres Geräts. Es wird empfohlen, Ihrem Gerät über die DHCP-Einstellungen Ihres Routers eine statische IP zuzuweisen.
:   *Beispiel: `192.168.1.50`*

`TUYA_LOCAL_KEY`
:   **Erforderlich**. Der geheime Schlüssel für die lokale Kommunikation.
:   *Beispiel: `a1b2c3d4e5f67890`*

`TUYA_VERSION`
:   Die Tuya-Protokollversionsnummer.
:   *Standard: `3.3`*

### InfluxDB-Einstellungen
Diese Einstellungen teilen dem Backend mit, wie es sich mit der InfluxDB-Datenbank verbinden soll. Wenn Sie das Standard-`docker-compose.yml`-Setup verwenden, sollten die Standardwerte korrekt funktionieren.

`INFLUXDB_URL`
:   Die vollständige URL für die InfluxDB v2-Instanz.
:   *Standard: `http://influxdb:8086`*

`INFLUXDB_TOKEN`
:   Das Authentifizierungstoken für InfluxDB. Dieses muss mit dem `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN` in `docker-compose.yml` übereinstimmen.
:   *Standard: `my-super-secret-auth-token`*

`INFLUXDB_ORG`
:   Der Organisationsname in InfluxDB. Dieser muss mit `DOCKER_INFLUXDB_INIT_ORG` übereinstimmen.
:   *Standard: `my-org`*

`INFLUXDB_BUCKET`
:   Der Bucket, in dem die Daten gespeichert werden.
:   *Standard: `water_monitor`*

### Alarmeinstellungen (Zukünftige Verwendung)
Diese Einstellungen steuern die (noch nicht implementierte) E-Mail-Alarmierungsfunktion.

`ALARM_EMAIL_ENABLED`
:   Aktivieren oder deaktivieren Sie E-Mail-Alarme.
:   *Standard: `False`*

`ALARM_EMAIL_RECIPIENT`
:   Die E-Mail-Adresse, an die Alarme gesendet werden sollen.
:   *Standard: `user@example.com`*
