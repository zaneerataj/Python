import time
from random import randint

def monitor_traffic():
    while True:
        traffic_data = {
            "timestamp": time.time(),
            "vehicle_count": randint(0, 100),
            "average_speed": randint(0, 120)
        }
        process_traffic_data(traffic_data)
        time.sleep(1)  # Simulate real-time data collection every second

def process_traffic_data(data):
    print(f"Time: {data['timestamp']}, Vehicles: {data['vehicle_count']}, Speed: {data['average_speed']} km/h")

monitor_traffic()
