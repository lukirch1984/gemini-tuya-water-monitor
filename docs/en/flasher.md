# Firmware Flasher

You can flash your LILYGO T4 directly from this page using Chrome, Edge, or Opera.

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>Connect LILYGO T4 via USB</h3>
    <p>Ensure no other software (like Cura, VS Code Serial Monitor) is using the port.</p>
    <esp-web-install-button manifest="../../assets/firmware/manifest.json"></esp-web-install-button>
</div>

## Instructions
1. Connect your device via USB.
2. Click "Install" above.
3. Select the correct serial port from the popup.
4. Follow the on-screen instructions.

*Note: You need to compile the firmware and place the `firmware.bin` file in `docs/assets/firmware/` before this works.*
