import tinytuya

def scan_tuya_devices():
    """
    Scans the local network for Tuya devices and prints their information.
    """
    print("Scanning for Tuya devices on your local network...")
    print("Please ensure UDP ports 6666, 6667, and 7000 are open.")

    devices = tinytuya.scan(timeout=10, maxretry=5)

    if not devices:
        print("No Tuya devices found.")
        return

    print("\nFound Tuya Devices:")
    for ip in devices:
        device_info = devices[ip]
        print(f"  IP Address: {ip}")
        print(f"  Device ID: {device_info['gwId']}")
        print(f"  Product ID: {device_info['productKey']}")
        print(f"  Version: {device_info['version']}")
        print("-" * 30)

if __name__ == "__main__":
    scan_tuya_devices()
