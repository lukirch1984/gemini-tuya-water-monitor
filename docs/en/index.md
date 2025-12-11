# Welcome to the Tuya Water Quality Monitor

This project provides a complete, self-hosted solution for monitoring water quality using common Tuya-compatible devices. It's designed to be robust, scalable, and easy to use, giving you full ownership and control over your data without relying on third-party cloud services.

![Architecture Diagram](https://via.placeholder.com/800x400.png?text=High-Level+Architecture+Diagram)

## The Problem
Many IoT devices, especially affordable consumer-grade sensors, lock your data into proprietary apps and cloud platforms. This limits your ability to create custom dashboards, trigger complex automations, or ensure long-term data retention.

## Our Solution
This project liberates your data by communicating directly with your Tuya device on your local network. It provides all the necessary components to collect, store, visualize, and access your water quality metrics in real-time.

### Key Features
*   **Local First**: No data is sent to external cloud services (after initial setup to get the `LocalKey`). Your data stays on your network.
*   **Full Stack Included**: From firmware to database to API, everything is containerized and ready to run.
*   **Extensible**: A clean FastAPI backend and a time-series database (InfluxDB) make it easy to integrate with other systems like Home Assistant or custom applications.
*   **Real-time Physical Display**: Includes firmware for a LILYGO T4 ESP32 board to act as a standalone, real-time monitor.
*   **Open Source**: The entire stack is open and ready to be customized.

Ready to get started? Head to the [Getting Started](./user-guide/getting-started.md) guide.