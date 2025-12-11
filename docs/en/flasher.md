# LILYGO T4 Web Flasher

This page allows you to install or update the firmware on your LILYGO T4 device directly from your browser. This process uses the Web Serial API, which is supported by modern browsers like **Google Chrome**, **Microsoft Edge**, and **Opera**.

## How to Use the Web Flasher

<div style="text-align: center; padding: 20px; border: 1px solid #444; border-radius: 8px; background: #222;">
    <h3>1. Connect Device & Click Install</h3>
    <p>Connect your LILYGO T4 to your computer via a USB data cable. Make sure no other programs (like a serial monitor or 3D printing software) are connected to the device. Then, click the button below.</p>
    <esp-web-install-button manifest="../assets/firmware/manifest.json"></esp-web-install-button>
</div>

### Step-by-Step Guide

1.  **Prepare the Firmware:** For this button to work, a compiled `firmware.bin` file must be available on the server. This is the responsibility of the project maintainers.

2.  **Connect Your Device:** Plug your LILYGO T4 into your computer. The USB cable must be a data cable, not just a charging cable.

3.  **Initiate Installation:** Click the "Install" button above. A dialog box will appear.

4.  **Select the Serial Port:** A list of available serial ports will be shown. Your LILYGO device will usually appear as a `USB-to-Serial` or `CP210x` device. Select it and click "Connect".

5.  **Flashing Process:** The installation will begin automatically. The tool will first connect, erase the flash memory, and then write the new firmware. You will see a progress bar.
    > **Note:** The tool automatically handles putting the device into "bootloader" mode. You do not need to press any buttons on the board.

6.  **Completion:** Once the process is finished, the device will restart with the new firmware. You can open the logs console in the flasher tool to see the device's output as it boots up and connects to WiFi.

### Troubleshooting

*   **Button doesn't appear or is disabled:** You are likely using an unsupported browser (e.g., Firefox, Safari). Please switch to a Chromium-based browser.
*   **No device in the port list:**
    *   Ensure you are using a USB **data** cable.
    *   You may be missing the necessary USB-to-Serial drivers (CP210x). Most modern operating systems have them, but if not, you can download them from [Silicon Labs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).
    *   Check that no other application is using the serial port.
*   **Installation fails:** Try disconnecting and reconnecting the device. Press the "Reset" button on the board and try the installation again immediately.
