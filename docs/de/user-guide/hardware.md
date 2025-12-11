# Hardware-Anleitung: LILYGO T4 Display

Dieses Projekt enthält eine dedizierte Firmware für das LILYGO T4 (ein ESP32 mit integriertem Display), um als eigenständiger Echtzeit-Monitor für Ihre Wasserqualitätsdaten zu fungieren.

## Flashen der Firmware

Wir bieten zwei Methoden an, um die Firmware auf Ihr Gerät zu bekommen. Für die einfachste Methode besuchen Sie bitte unsere dedizierte Web-Flasher-Anleitung. Wenn Sie ein Entwickler sind und den Code selbst kompilieren möchten, folgen Sie den manuellen PlatformIO-Anweisungen unten.

[➡️ Zur Web-Flasher-Anleitung wechseln](../flasher.md)

---

### Manuelles Flashen mit PlatformIO

Wenn Sie die Firmware ändern oder selbst kompilieren möchten, müssen Sie PlatformIO verwenden.

#### Voraussetzungen
*   [Visual Studio Code](https://code.visualstudio.com/)
*   [PlatformIO IDE Extension](https://platformio.org/install/ide?install=vscode) für VS Code.

#### Schritte
1.  Öffnen Sie das `firmware/`-Verzeichnis dieses Projekts in VS Code.
2.  PlatformIO sollte das Projekt automatisch erkennen.
3.  Öffnen Sie `firmware/src/main.cpp`.
4.  **Konfiguration ändern**:
    *   Aktualisieren Sie die Variablen `ssid` und `password` mit Ihren WLAN-Anmeldeinformationen.
    *   Aktualisieren Sie die `api_url`, sodass sie auf die IP-Adresse des Computers verweist, auf dem Ihr Docker-Stack läuft. Zum Beispiel: `http://192.168.1.100:8000/api/v1/data/latest`.
5.  **Kompilieren & Hochladen**:
    *   Verbinden Sie das LILYGO T4 mit Ihrem Computer.
    *   Verwenden Sie die PlatformIO-Symbolleiste in VS Code, um das Projekt zu kompilieren und auf das Gerät hochzuladen.

Ihr Hardware-Display sollte nun starten, sich mit dem WLAN verbinden und Daten anzeigen.
