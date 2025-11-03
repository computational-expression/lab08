"""
Lab 8: Buzzer Alert Manager
Manage buzzer alert system using a dictionary.
Connected to Pico 2 WH GPIO 15 (GP15) - Physical Pin 20.
"""

from machine import Pin, PWM
import time

# Initialize buzzer on GPIO 15
buzzer = PWM(Pin(15))
buzzer.freq(1000)  # Set frequency to 1000 Hz
buzzer.duty_u16(0)  # Start with buzzer off

def sound_buzzer(duration=0.5):
    """Sound the buzzer for a specified duration (seconds)."""
    # TODO: Implement buzzer sound
    # 1. Set buzzer duty cycle to 32768 (50%) using buzzer.duty_u16()
    # 2. Sleep for the duration using time.sleep()
    # 3. Turn off buzzer by setting duty cycle to 0
    # 4. Handle exceptions with try/except
    pass

def create_alert_database():
    """Create database tracking alert status for different locations."""
    # TODO: Create and return an empty dictionary
    # Print "Buzzer alert manager initialized"
    pass

def add_alert_location(alerts):
    """Add a new location to the alert system."""
    # TODO: Implement adding an alert location
    # 1. Get location_id from user input
    # 2. Check if location_id already exists in alerts dictionary
    # 3. If exists, print error and return
    # 4. Get location_name from user input
    # 5. Get alert_count from user input (convert to int, handle ValueError)
    # 6. Check if alert_count is negative, print error and return if so
    # 7. Create a dictionary with keys: "location", "buzzer_on" (False), 
    #    "alert_count", "last_reason" ("None")
    # 8. Add this dictionary to alerts using location_id as the key
    # 9. Print confirmation message
    pass

def trigger_buzzer(alerts, location_id, reason):
    """Activate buzzer alert for a specific location."""
    # TODO: Implement buzzer trigger
    # 1. Check if location_id exists in alerts (use 'not in')
    # 2. If not found, print error and return
    # 3. Print activation message
    # 4. Call sound_buzzer() to make physical sound
    # 5. Update dictionary values:
    #    - Set "buzzer_on" to True
    #    - Increment "alert_count" by 1
    #    - Set "last_reason" to reason
    pass

def clear_buzzer(alerts, location_id):
    """Deactivate buzzer alert for a specific location."""
    # TODO: Implement buzzer clear
    # 1. Check if location_id exists in alerts
    # 2. If not found, print error and return
    # 3. Set "buzzer_on" to False in the dictionary
    # 4. Print confirmation message
    pass

def check_alert_history(alerts):
    """Check which locations have alert history."""
    # TODO: Implement alert history check
    # 1. Create empty list called history
    # 2. Loop through alerts.items() to get loc_id and data
    # 3. Check if data["alert_count"] > 0
    # 4. If yes, add formatted message to history list
    # 5. Return the history list
    pass

def show_alert_stats(alerts):
    """Display alert statistics and history."""
    # TODO: Implement statistics display
    # 1. Get total count using len(alerts)
    # 2. Count active buzzers by looping through alerts.values()
    # 3. Calculate total alerts and collect counts in a list
    # 4. Calculate average alerts
    # 5. Find min and max alert counts
    # 6. Print all statistics
    # 7. Call check_alert_history() and print results
    pass

def main():
    # TODO: Implement main menu loop
    # 1. Create database using create_alert_database()
    # 2. Create a while True loop for the menu
    # 3. Display menu options (View all, Add location, Trigger, Clear, Show stats, Exit)
    # 4. Get user choice
    # 5. Use if/elif/else to handle each menu option:
    #    - Option 1: Loop through alerts.items() and print status
    #    - Option 2: Call add_alert_location()
    #    - Option 3: Get location and reason, call trigger_buzzer()
    #    - Option 4: Get location, call clear_buzzer()
    #    - Option 5: Call show_alert_stats()
    #    - Option 6: Break the loop
    pass

if __name__ == "__main__":
    main()
