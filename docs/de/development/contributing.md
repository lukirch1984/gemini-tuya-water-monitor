# Leitfaden für Beitragende & Entwicklung

Wir freuen uns über Beiträge zum Projekt! Dieser Leitfaden beschreibt den Entwicklungsprozess und bewährte Verfahren.

## Entwicklungsumgebung

Der einfachste Weg, das Backend zu entwickeln, besteht darin, InfluxDB über Docker auszuführen, aber die FastAPI-Anwendung auf Ihrem lokalen Rechner laufen zu lassen.

1.  **Abhängigkeiten starten:**
    ```bash
    docker-compose up -d influxdb grafana
    ```

2.  **Einrichten einer virtuellen Umgebung:**
    Vom Projekt-Root aus:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Entwicklungsserver starten:**
    Der `uvicorn`-Server bietet Live-Reloading bei Code-Änderungen.
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    *Hinweis: Sie benötigen immer noch eine `.env`-Datei im `backend/`-Verzeichnis, die auf `localhost` für InfluxDB verweist, wenn Sie auf diese Weise arbeiten.*

## Tests ausführen

Das Projekt verwendet `pytest` für Unit-Tests.

So führen Sie die Testsuite aus:
```bash
# Stellen Sie sicher, dass Sie sich in Ihrer virtuellen Umgebung befinden
pytest
```

## Code-Stil

Dieses Projekt erzwingt noch keinen strengen Code-Stil mit einem Linter, aber wir empfehlen, die [PEP 8](https://peps.python.org/pep-0008/)-Konventionen zu befolgen.

## Änderungen einreichen

1.  **Forken Sie das Repository** auf GitHub.
2.  **Erstellen Sie einen neuen Branch** für Ihr Feature oder Ihre Fehlerbehebung.
3.  **Machen Sie Ihre Änderungen** und committen Sie sie mit klaren, beschreibenden Nachrichten.
4.  **Pushen Sie Ihren Branch** zu Ihrem Fork.
5.  **Öffnen Sie einen Pull Request** gegen den `main`-Branch des ursprünglichen Repositorys.
