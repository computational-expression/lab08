"""
Test script for DHT22 Temperature/Humidity Sensor on GPIO 2
Run this on the Pico to test if your DHT22 is connected correctly.
"""

from machine import Pin
import dht
import time

# Set up DHT22 sensor on GPIO 2
sensor = dht.DHT22(Pin(2))

print("Testing DHT22 on GPIO 2 (Pin 4)")
print("DHT22 readings update every 2 seconds")
print("Press Ctrl+C to stop\n")

try:
    while True:
        try:
            # Measure temperature and humidity
            sensor.measure()
            temp = sensor.temperature()
            humidity = sensor.humidity()
            
            # Determine comfort level
            if temp > 25:
                comfort = "Warm"
            elif temp < 20:
                comfort = "Cool"
            else:
                comfort = "Good"
            
            print(f"Temperature: {temp:.1f} C | Humidity: {humidity:.1f}% | Comfort: {comfort}")
            
        except Exception as e:
            print(f"Read error: {e}")
        
        time.sleep(2)  # DHT22 needs at least 2 seconds between readings
        
except KeyboardInterrupt:
    print("\nTest stopped")
