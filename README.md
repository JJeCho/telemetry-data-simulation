# Telemetry Data Simulation

## Overview

This project is designed to simulate streams of telemetry data, such as GPS coordinates and sensor readings, and send this data over a WebSocket connection. It is useful for testing systems that process real-time telemetry data without the need for actual sensors or external data sources.

## Features

- **Simulated GPS Data**: Generates random latitude, longitude, altitude, speed, and timestamps to mimic real-world GPS data.
- **Sensor Data**: Includes additional simulated sensor readings to enhance data streams.
- **WebSocket Support**: Streams the generated telemetry data over a WebSocket connection, allowing easy integration with systems that require real-time data input.
- **Graceful Shutdown**: Handles signals to stop data transmission smoothly.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `websockets` library (install via pip)

```bash
pip install websockets
```

### Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/telemetry-data-simulation.git
cd telemetry-data-simulation
```

### Usage

To start the telemetry data simulation, run:

```bash
python main.py
```

The script will begin generating and streaming telemetry data through a WebSocket. You can connect a client to the WebSocket server to receive and process the data.

### Customization

You can customize the data generation logic in the `main.py` file. Modify functions like `generate_gps_data` to adjust the ranges or add new types of simulated telemetry data as needed.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

Inspired by the need for testing telemetry processing systems without relying on real-time external data sources.
