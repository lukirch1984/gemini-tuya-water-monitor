# Hardware Guide: LILYGO T4 Display

This project includes dedicated firmware for the LILYGO T4 (an ESP32 with an integrated display) to act as a real-time, standalone monitor for your water quality data.

## Flashing the Firmware

We provide two methods for getting the firmware onto your device. For the easiest method, please see our dedicated Web Flasher guide. If you are a developer and wish to compile the code yourself, follow the manual PlatformIO instructions below.

[➡️ Go to the Web Flasher Guide](../flasher.md)

---

### Manual Flashing with PlatformIO

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
