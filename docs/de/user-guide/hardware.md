# Hardware-Anleitung: LILYGO T4 Display

Dieses Projekt enthält eine dedizierte Firmware für das LILYGO T4 (ein ESP32 mit integriertem Display), um als eigenständiger Echtzeit-Monitor für Ihre Wasserqualitätsdaten zu fungieren.

## Merkmale
*   Verbindet sich mit Ihrem lokalen WLAN.
*   Ruft regelmäßig die neuesten Sensordaten von der Backend-API ab.
*   Zeigt Werte auf dem Bildschirm an.
*   Geringer Stromverbrauch.

## Flashen der Firmware

Es gibt zwei Möglichkeiten, die Firmware auf Ihr Gerät zu bringen.

### Methode 1: Web-Flasher (Empfohlen)

Sie können das Gerät direkt von Ihrem Browser aus flashen, ohne Entwicklungstools installieren zu müssen.

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>LILYGO T4 via USB verbinden</h3>
    <p>Stellen Sie sicher, dass keine andere Software (wie Cura oder VS Code) den Port blockiert.</p>
    <esp-web-install-button manifest="../../assets/firmware/manifest.json"></esp-web-install-button>
</div>

#### Anleitung
1.  **Binary vorbereiten**: Bevor der Flasher verwendet werden kann, muss der Projektbetreuer die Firmware kompiliert und die Datei `firmware.bin` am richtigen Ort (`docs/assets/firmware/`) platziert haben.
2.  **Gerät verbinden**: Stecken Sie Ihr LILYGO T4 über USB an Ihren Computer an.
3.  **Auf "Install" klicken**: Drücken Sie die "Install"-Schaltfläche oben. Ein Popup wird erscheinen.
4.  **Port auswählen**: Wählen Sie den seriellen Port, der Ihrem Gerät entspricht, und klicken Sie auf "Verbinden".
5.  Der Flash-Vorgang beginnt automatisch.

*Dieses Tool erfordert einen modernen Browser wie Chrome, Edge oder Opera, der Web Serial unterstützt.*


### Methode 2: Manuelles Flashen mit PlatformIO

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
