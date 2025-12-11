# LILYGO T4 Web-Flasher

Diese Seite ermöglicht es Ihnen, die Firmware auf Ihrem LILYGO T4 Gerät direkt aus Ihrem Browser zu installieren oder zu aktualisieren. Dieser Prozess verwendet die Web Serial API, die von modernen Browsern wie **Google Chrome**, **Microsoft Edge** und **Opera** unterstützt wird.

## Wie man den Web-Flasher benutzt

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>1. Gerät verbinden & auf Installieren klicken</h3>
    <p>Verbinden Sie Ihr LILYGO T4 über ein USB-Datenkabel mit Ihrem Computer. Stellen Sie sicher, dass keine anderen Programme (wie ein serieller Monitor oder eine 3D-Drucksoftware) mit dem Gerät verbunden sind. Klicken Sie dann auf die Schaltfläche unten.</p>
    <esp-web-install-button manifest="../assets/firmware/manifest.json"></esp-web-install-button>
</div>

### Schritt-für-Schritt-Anleitung

1.  **Firmware vorbereiten:** Damit diese Schaltfläche funktioniert, muss eine kompilierte `firmware.bin`-Datei auf dem Server verfügbar sein. Dies liegt in der Verantwortung der Projektbetreuer.

2.  **Gerät verbinden:** Stecken Sie Ihr LILYGO T4 an Ihren Computer an. Das USB-Kabel muss ein Datenkabel sein, nicht nur ein Ladekabel.

3.  **Installation starten:** Klicken Sie auf die "Install"-Schaltfläche oben. Ein Dialogfeld wird angezeigt.

4.  **Seriellen Port auswählen:** Eine Liste der verfügbaren seriellen Ports wird angezeigt. Ihr LILYGO-Gerät erscheint normalerweise als `USB-to-Serial`- oder `CP210x`-Gerät. Wählen Sie es aus und klicken Sie auf "Verbinden".

5.  **Flash-Vorgang:** Die Installation beginnt automatisch. Das Tool wird sich zuerst verbinden, den Flash-Speicher löschen und dann die neue Firmware schreiben. Sie werden einen Fortschrittsbalken sehen.
    > **Hinweis:** Das Tool versetzt das Gerät automatisch in den "Bootloader"-Modus. Sie müssen keine Tasten auf dem Board drücken.

6.  **Abschluss:** Sobald der Vorgang abgeschlossen ist, wird das Gerät mit der neuen Firmware neu gestartet. Sie können die Protokollkonsole im Flasher-Tool öffnen, um die Ausgabe des Geräts beim Hochfahren und Verbinden mit dem WLAN zu sehen.

### Fehlerbehebung

*   **Schaltfläche wird nicht angezeigt oder ist deaktiviert:** Sie verwenden wahrscheinlich einen nicht unterstützten Browser (z.B. Firefox, Safari). Bitte wechseln Sie zu einem Chromium-basierten Browser.
*   **Kein Gerät in der Port-Liste:**
    *   Stellen Sie sicher, dass Sie ein USB-**Daten**kabel verwenden.
    *   Möglicherweise fehlen Ihnen die notwendigen USB-zu-Seriell-Treiber (CP210x). Die meisten modernen Betriebssysteme haben sie, aber wenn nicht, können Sie sie von [Silicon Labs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) herunterladen.
    *   Überprüfen Sie, ob keine andere Anwendung den seriellen Port verwendet.
*   **Installation schlägt fehl:** Versuchen Sie, das Gerät zu trennen und wieder zu verbinden. Drücken Sie die "Reset"-Taste auf dem Board und versuchen Sie die Installation sofort erneut.
