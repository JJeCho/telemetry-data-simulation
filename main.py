import asyncio
import websockets
import json
import random
import time
import signal

stop_sending = False

def generate_gps_data():
    return {
        "latitude": random.uniform(-90, 90),       # degrees
        "longitude": random.uniform(-180, 180),    # degrees
        "altitude": random.uniform(100, 500),      # meters
        "speed": random.uniform(0, 200),           # km/h
        "timestamp": time.time()                   # Current time in seconds since epoch
    }

def generate_sensor_data():
    return {
        "acceleration_x": random.uniform(-10, 10),           # m/s^2
        "acceleration_y": random.uniform(-10, 10),           # m/s^2
        "acceleration_z": random.uniform(-10, 10),           # m/s^2
        "orientation_pitch": random.uniform(-180, 180),      # degrees
        "orientation_roll": random.uniform(-180, 180),       # degrees
        "orientation_yaw": random.uniform(-180, 180),        # degrees
        "rotational_velocity_x": random.uniform(-100, 100),  # deg/s
        "rotational_velocity_y": random.uniform(-100, 100),  # deg/s
        "rotational_velocity_z": random.uniform(-100, 100),  # deg/s
        "timestamp": time.time()                             # Current time in seconds since epoch
    }

def generate_environmental_data():
    return {
        "temperature": random.uniform(-30, 50),  # Celsius
        "humidity": random.uniform(0, 100),      # Percentage
        "pressure": random.uniform(950, 1050),   # hPa
        "timestamp": time.time()                 # Current time in seconds since epoch
    }

def generate_system_health_data():
    return {
        "battery_level": random.uniform(0, 100),            # Percentage
        "signal_strength": random.uniform(-120, -30),       # dBm
        "error_code": random.choice([0, 1, 2, 3]),          # Simulated error codes
        "internal_temperature": random.uniform(-20, 85),    # Celsius
        "timestamp": time.time()                            # Current time in seconds since epoch
    }

def generate_communications_data():
    return {
        "uplink_latency": random.uniform(10, 200),      # ms
        "downlink_latency": random.uniform(10, 200),    # ms
        "packet_loss_rate": random.uniform(0, 5),       # Percentage
        "data_transfer_rate": random.uniform(0.5, 10),  # Mbps
        "timestamp": time.time()                        # Current time in seconds since epoch
    }

async def send_data():
    uri = "ws://localhost:5000/telemetry"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to {uri}")
            while not stop_sending:
                try:
                    gps_data = generate_gps_data()
                    sensor_data = generate_sensor_data()
                    environmental_data = generate_environmental_data()
                    system_health_data = generate_system_health_data()
                    communications_data = generate_communications_data()

                    combined_data = {
                        "gps_data": gps_data,
                        "sensor_data": sensor_data,
                        "environmental_data": environmental_data,
                        "system_health_data": system_health_data,
                        "communications_data": communications_data,
                        "timestamp": time.time()
                    }

                    await websocket.send(json.dumps(combined_data))
                    print("Data sent at", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                    await asyncio.sleep(1)
                except Exception as e:
                    print(f"Error sending data: {e}")
                    break
    except Exception as e:
        print(f"Could not connect to server: {e}")
    finally:
        print("Connection closed")

def signal_handler(sig, frame):
    global stop_sending
    print("Termination signal received. Shutting down gracefully...")
    stop_sending = True

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        asyncio.run(send_data())
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Program terminated.")
