# Contribution & Development Guide

We welcome contributions to the project! This guide outlines the development process and best practices.

## Development Environment

The easiest way to develop the backend is to run InfluxDB via Docker but run the FastAPI application on your local machine.

1.  **Start Dependencies:**
    ```bash
    docker-compose up -d influxdb grafana
    ```

2.  **Set up a Virtual Environment:**
    From the project root:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Run the Development Server:**
    The `uvicorn` server provides live-reloading on code changes.
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    *Note: You will still need a `.env` file in the `backend/` directory pointing to `localhost` for InfluxDB if running this way.*

## Running Tests

The project uses `pytest` for unit testing.

To run the test suite:
```bash
# Ensure you are in your virtual environment
pytest
```

## Code Style

This project does not yet enforce a strict code style with a linter, but we encourage following [PEP 8](https://peps.python.org/pep-0008/) conventions.

## Submitting Changes

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bugfix.
3.  **Make your changes** and commit them with clear, descriptive messages.
4.  **Push your branch** to your fork.
5.  **Open a Pull Request** against the `main` branch of the original repository.
