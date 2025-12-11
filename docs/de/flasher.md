# Firmware Flasher

Du kannst dein LILYGO T4 direkt von dieser Seite aus flashen (benötigt Chrome, Edge oder Opera).

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>LILYGO T4 via USB verbinden</h3>
    <p>Stelle sicher, dass keine andere Software (wie Cura oder VS Code) den Port blockiert.</p>
    <esp-web-install-button manifest="../../assets/firmware/manifest.json"></esp-web-install-button>
</div>

## Anleitung
1. Verbinde das Gerät per USB.
2. Klicke oben auf "Install".
3. Wähle den korrekten Serial-Port im Popup aus.
4. Folge den Anweisungen auf dem Bildschirm.

*Hinweis: Du musst die Firmware zuerst kompilieren und die `firmware.bin` in `docs/assets/firmware/` ablegen, damit dies funktioniert.*
