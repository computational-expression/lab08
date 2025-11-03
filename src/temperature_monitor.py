"""
Lab 8: Temperature Monitor
Manage DHT22 temperature and humidity readings using a dictionary.
Connected to Pico 2 WH GPIO 2 (GP2) - Physical Pin 4.
"""

from machine import Pin
import dht
import time

# Initialize DHT22 sensor on GPIO 2
sensor = dht.DHT22(Pin(2))

def read_sensor():
    """Read temperature and humidity from DHT22 sensor."""
    # TODO: Implement sensor reading
    # 1. Use sensor.measure() to trigger a reading
    # 2. Get temperature with sensor.temperature()
    # 3. Get humidity with sensor.humidity()
    # 4. Return both values as a tuple (temp, humidity)
    # 5. Handle exceptions and return (None, None) on error
    pass

def create_temp_database():
    """Create database with temperature/humidity readings from different locations."""
    # TODO: Create and return an empty dictionary
    # Print "Temperature monitor initialized"
    pass

def add_temp_reading(readings):
    """Add a new temperature reading for a location using DHT22 sensor."""
    # TODO: Implement adding a temperature reading
    # 1. Get location_id from user input
    # 2. Check if location_id already exists in readings dictionary (use 'in')
    # 3. If exists, print error and return
    # 4. Get location_name from user input
    # 5. Read sensor using read_sensor() function (use time.sleep(2) before reading)
    # 6. Check if sensor reading failed (None values)
    # 7. Determine comfort level based on temperature:
    #    - temp > 25: "Warm"
    #    - temp < 20: "Cool"
    #    - else: "Good"
    # 8. Create a dictionary with keys: "location", "temp", "humidity", "comfort"
    # 9. Add this dictionary to readings using location_id as the key
    # 10. Print confirmation message with temperature and humidity
    pass

def check_temp_alerts(readings):
    """Check which locations exceed temperature or humidity thresholds."""
    # TODO: Implement alert checking
    # 1. Create empty list called alerts
    # 2. Loop through readings.items() to get loc_id and data
    # 3. Check if data["temp"] > 25, add alert message to list
    # 4. Check if data["humidity"] > 60, add alert message to list
    # 5. Return the alerts list
    pass

def show_temp_stats(readings):
    """Display temperature statistics and alerts."""
    # TODO: Implement statistics display
    # 1. Get total count using len(readings)
    # 2. Create empty lists for temps and humidities
    # 3. Loop through readings.values() to collect all temps and humidities
    # 4. Calculate averages using sum() and len()
    # 5. Find min and max temperatures
    # 6. Print all statistics
    # 7. Call check_temp_alerts() and print any alerts found
    pass

def main():
    # TODO: Implement main menu loop
    # 1. Create database using create_temp_database()
    # 2. Create a while True loop for the menu
    # 3. Display menu options (View all, Add location, Check alerts, Show stats, Exit)
    # 4. Get user choice
    # 5. Use if/elif/else to handle each menu option:
    #    - Option 1: Loop through readings.items() and print each location
    #    - Option 2: Call add_temp_reading()
    #    - Option 3: Call check_temp_alerts() and print results
    #    - Option 4: Call show_temp_stats()
    #    - Option 5: Break the loop
    pass

if __name__ == "__main__":
    main()
