"""
Lab 8: Light Monitor
Manage LDR (photoresistor) light level readings using a dictionary.
Connected to Pico 2 WH GPIO 26 (ADC0) with 10k resistor.
"""

from machine import Pin, ADC

# Initialize LDR on GPIO 26 (ADC0)
ldr = ADC(Pin(26))

def read_light_level():
    """Read light level from LDR sensor and convert to 0-1000 scale."""
    # TODO: Implement light sensor reading
    # 1. Read raw ADC value using ldr.read_u16() (returns 0-65535)
    # 2. Convert to 0-1000 scale: (raw_value / 65535) * 1000
    # 3. Convert to integer using int()
    # 4. Return the light level
    # 5. Handle exceptions and return None on error
    pass

def create_light_database():
    """Create database with light level readings from different locations."""
    # TODO: Create and return an empty dictionary
    # Print "Light monitor initialized"
    pass

def add_light_reading(readings):
    """Add a new light level reading for a location using LDR sensor."""
    # TODO: Implement adding a light reading
    # 1. Get location_id from user input
    # 2. Check if location_id already exists in readings dictionary
    # 3. If exists, print error and return
    # 4. Get location_name from user input
    # 5. Read sensor using read_light_level() function
    # 6. Check if sensor reading failed (None value)
    # 7. Determine brightness category based on light level:
    #    - light_level > 500: "Bright"
    #    - light_level > 200: "Medium"
    #    - else: "Dark"
    # 8. Create a dictionary with keys: "location", "light_level", "brightness"
    # 9. Add this dictionary to readings using location_id as the key
    # 10. Print confirmation message with light level and brightness
    pass

def check_light_alerts(readings):
    """Check which locations have insufficient lighting."""
    # TODO: Implement light alert checking
    # 1. Create empty list called alerts
    # 2. Set minimum light threshold (e.g., 200)
    # 3. Loop through readings.items() to get loc_id and data
    # 4. Check if data["light_level"] is below threshold
    # 5. If below, add alert message to list
    # 6. Return the alerts list
    pass

def show_light_stats(readings):
    """Display light level statistics and alerts."""
    # TODO: Implement statistics display
    # 1. Get total count using len(readings)
    # 2. Create empty list for light levels
    # 3. Loop through readings.values() to collect all light levels
    # 4. Calculate average using sum() and len()
    # 5. Find min and max light levels
    # 6. Count each brightness category (Bright, Medium, Dark) using a loop
    # 7. Print all statistics
    # 8. Call check_light_alerts() and print any alerts found
    pass

def main():
    # TODO: Implement main menu loop
    # 1. Create database using create_light_database()
    # 2. Create a while True loop for the menu
    # 3. Display menu options (View all, Add location, Check alerts, Show stats, Exit)
    # 4. Get user choice
    # 5. Use if/elif/else to handle each menu option:
    #    - Option 1: Loop through readings.items() and print each location
    #    - Option 2: Call add_light_reading()
    #    - Option 3: Call check_light_alerts() and print results
    #    - Option 4: Call show_light_stats()
    #    - Option 5: Break the loop
    pass

if __name__ == "__main__":
    main()
