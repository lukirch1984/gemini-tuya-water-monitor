# Hardware Guide: LILYGO T4 Display

This project includes dedicated firmware for the LILYGO T4 (an ESP32 with an integrated display) to act as a real-time, standalone monitor for your water quality data.

## Features
*   Connects to your local WiFi.
*   Periodically fetches the latest sensor data from the backend API.
*   Displays values on the screen.
*   Low power consumption.

## Flashing the Firmware

There are two ways to get the firmware onto your device.

### Method 1: Web Flasher (Recommended)

You can flash the device directly from your browser without needing to install any development tools.

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>Connect LILYGO T4 via USB</h3>
    <p>Ensure no other software (like Cura, VS Code Serial Monitor) is using the port.</p>
    <esp-web-install-button manifest="../../assets/firmware/manifest.json"></esp-web-install-button>
</div>

#### Instructions
1.  **Prepare the binary**: Before the flasher can be used, the project maintainer must have compiled the firmware and placed the `firmware.bin` file in the correct location (`docs/assets/firmware/`).
2.  **Connect your device**: Plug your LILYGO T4 into your computer via USB.
3.  **Click Install**: Press the "Install" button above. A popup will appear.
4.  **Select the port**: Choose the serial port corresponding to your device and click "Connect".
5.  The flashing process will begin automatically.

*This tool requires a modern browser like Chrome, Edge, or Opera that supports Web Serial.*


### Method 2: Manual Flashing with PlatformIO

If you want to modify the firmware or compile it yourself, you'll need to use PlatformIO.

#### Prerequisites
*   [Visual Studio Code](https://code.visualstudio.com/)
*   [PlatformIO IDE Extension](https://platformio.org/install/ide?install=vscode) for VS Code.

#### Steps
1.  Open the `firmware/` directory of this project in VS Code.
2.  PlatformIO should automatically recognize the project.
3.  Open `firmware/src/main.cpp`.
4.  **Modify the configuration**:
    *   Update the `ssid` and `password` variables with your WiFi credentials.
    *   Update the `api_url` to point to the IP address of the machine running your Docker stack. For example: `http://192.168.1.100:8000/api/v1/data/latest`.
5.  **Build & Upload**:
    *   Connect the LILYGO T4 to your computer.
    *   Use the PlatformIO toolbar in VS Code to build and upload the project to the device.

Your hardware display should now boot, connect to WiFi, and start showing data.
