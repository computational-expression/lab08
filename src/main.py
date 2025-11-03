"""
Lab 8: Environmental Monitoring System - Main Program
Integrates temperature, light, and buzzer alert modules with real hardware.
Hardware: DHT22 (GPIO 2), LDR (GPIO 26), Buzzer (GPIO 15)

IMPORTANT: To run this on the Pico, you must upload ALL four files:
  - main.py (this file)
  - temperature_monitor.py
  - light_monitor.py
  - buzzer_manager.py

All files must be in the same directory on the Pico (usually the root directory).
"""

try:
    import temperature_monitor as temp
    import light_monitor as light
    import buzzer_manager as buzzer
    import time
except ImportError as e:
    print("ERROR: Missing required module files!")
    print(f"Import error: {e}")
    print("\nPlease upload ALL four Python files to the Pico:")
    print("  - main.py")
    print("  - temperature_monitor.py")
    print("  - light_monitor.py")
    print("  - buzzer_manager.py")
    print("\nAll files must be in the same directory.")
    raise

def display_main_menu():
    print("\n" + "="*50)
    print("   ENVIRONMENTAL MONITORING SYSTEM")
    print("="*50)
    print("\nSelect a module:")
    print("1. Temperature Monitor (DHT22)")
    print("2. Light Monitor (LDR)")
    print("3. Buzzer Alert Manager")
    print("4. System Summary & Alerts")
    print("5. Exit")
    print("-"*50)

def check_all_alerts(temp_data, light_data, alert_data):
    """Check all sensors and trigger buzzers if needed."""
    print("\n" + "="*50)
    print("   CHECKING ALL SENSORS")
    print("="*50)
    
    alert_triggered = False
    
    # Check temperature alerts
    print("\nTemperature Status:")
    if len(temp_data) == 0:
        print("  No temperature data recorded yet")
    else:
        temp_alerts = temp.check_temp_alerts(temp_data)
        if temp_alerts:
            for alert in temp_alerts:
                print(f"  WARNING: {alert}")
                # Trigger buzzer for the specific location
                loc_id = alert.split(":")[0]
                if loc_id in alert_data:
                    buzzer.trigger_buzzer(alert_data, loc_id, "High temperature")
                    alert_triggered = True
                elif len(alert_data) > 0:
                    # Trigger first available alert location
                    first_loc = list(alert_data.keys())[0]
                    buzzer.trigger_buzzer(alert_data, first_loc, "High temperature detected")
                    alert_triggered = True
        else:
            print("  All temperatures OK")
    
    # Check light alerts
    print("\nLight Status:")
    if len(light_data) == 0:
        print("  No light data recorded yet")
    else:
        light_alerts = light.check_light_alerts(light_data)
        if light_alerts:
            for alert in light_alerts:
                print(f"  WARNING: {alert}")
                # Trigger buzzer for the specific location
                loc_id = alert.split(":")[0]
                if loc_id in alert_data:
                    buzzer.trigger_buzzer(alert_data, loc_id, "Low light")
                    alert_triggered = True
                elif len(alert_data) > 0:
                    # Trigger first available alert location
                    first_loc = list(alert_data.keys())[0]
                    buzzer.trigger_buzzer(alert_data, first_loc, "Low light detected")
                    alert_triggered = True
        else:
            print("  All light levels OK")
    
    # Show buzzer status
    print("\nBuzzer Status:")
    if len(alert_data) == 0:
        print("  No alert locations configured")
    else:
        active = 0
        for data in alert_data.values():
            if data["buzzer_on"]:
                active = active + 1
        if active > 0:
            print(f"  {active} active alert(s)")
            for loc_id, data in alert_data.items():
                if data["buzzer_on"]:
                    print(f"    - {loc_id}: {data['last_reason']}")
        else:
            print("  No active alerts")
    
    if alert_triggered:
        print("\n  Physical buzzer was activated!")
    
    print("="*50)

def show_system_summary(temp_data, light_data, alert_data):
    """Display summary of all three systems."""
    print("\n" + "="*50)
    print("   SYSTEM SUMMARY")
    print("="*50)
    
    print("\nTEMPERATURE MONITOR:")
    if len(temp_data) == 0:
        print("  No temperature data recorded yet")
        print("  Add locations using the Temperature Monitor menu")
    else:
        temp.show_temp_stats(temp_data)
    
    print("\n" + "-"*50)
    print("\nLIGHT MONITOR:")
    if len(light_data) == 0:
        print("  No light data recorded yet")
        print("  Add locations using the Light Monitor menu")
    else:
        light.show_light_stats(light_data)
    
    print("\n" + "-"*50)
    print("\nBUZZER ALERTS:")
    if len(alert_data) == 0:
        print("  No alert locations configured yet")
        print("  Add locations using the Buzzer Alert Manager menu")
    else:
        buzzer.show_alert_stats(alert_data)
    
    print("\n" + "="*50)

def main():
    print("="*50)
    print(" ENVIRONMENTAL MONITORING SYSTEM")
    print("="*50)
    print("\nInitializing hardware components...")
    print("  - DHT22 Temperature/Humidity Sensor (GPIO 2)")
    print("  - LDR Photoresistor (GPIO 26)")
    print("  - Passive Buzzer (GPIO 15)")
    
    time.sleep(1)
    
    print("\n[Temperature Monitor]")
    temp_data = temp.create_temp_database()
    
    print("\n[Light Monitor]")
    light_data = light.create_light_database()
    
    print("\n[Buzzer Alert Manager]")
    alert_data = buzzer.create_alert_database()
    
    print("\n" + "="*50)
    print(" ALL SYSTEMS READY!")
    print("="*50)
    print("\nThis system uses dictionaries to manage:")
    print("  • Temperature/humidity readings from DHT22")
    print("  • Light levels from LDR")
    print("  • Alert status and buzzer control")
    print("\nStart by adding locations in each module,")
    print("then use 'System Summary & Alerts' to check all sensors!")
    print("="*50)
    
    while True:
        display_main_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            # Temperature Monitor module
            while True:
                print("\n--- TEMPERATURE MONITOR ---")
                print("1. View all locations")
                print("2. Add location")
                print("3. Check alerts")
                print("4. Show stats")
                print("5. Back to main menu")
                sub_choice = input("Choice: ")
                
                if sub_choice == "1":
                    if len(temp_data) == 0:
                        print("No locations recorded yet. Choose option 2 to add.")
                    else:
                        for loc_id, data in temp_data.items():
                            print(f"{loc_id}: {data['location']} - {data['temp']}C, {data['humidity']}%, {data['comfort']}")
                elif sub_choice == "2":
                    temp.add_temp_reading(temp_data)
                elif sub_choice == "3":
                    alerts = temp.check_temp_alerts(temp_data)
                    if alerts:
                        for alert in alerts:
                            print(alert)
                    else:
                        print("No alerts")
                elif sub_choice == "4":
                    temp.show_temp_stats(temp_data)
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice")
        
        elif choice == "2":
            # Light Monitor module
            while True:
                print("\n--- LIGHT MONITOR ---")
                print("1. View all locations")
                print("2. Add location")
                print("3. Check alerts")
                print("4. Show stats")
                print("5. Back to main menu")
                sub_choice = input("Choice: ")
                
                if sub_choice == "1":
                    if len(light_data) == 0:
                        print("No locations recorded yet. Choose option 2 to add.")
                    else:
                        for loc_id, data in light_data.items():
                            print(f"{loc_id}: {data['location']} - Level {data['light_level']}, {data['brightness']}")
                elif sub_choice == "2":
                    light.add_light_reading(light_data)
                elif sub_choice == "3":
                    alerts = light.check_light_alerts(light_data)
                    if alerts:
                        for alert in alerts:
                            print(alert)
                    else:
                        print("No alerts")
                elif sub_choice == "4":
                    light.show_light_stats(light_data)
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice")
        
        elif choice == "3":
            # Buzzer Alert Manager module
            while True:
                print("\n--- BUZZER ALERT MANAGER ---")
                print("1. View all alerts")
                print("2. Add location")
                print("3. Trigger buzzer")
                print("4. Clear buzzer")
                print("5. Show stats")
                print("6. Back to main menu")
                sub_choice = input("Choice: ")
                
                if sub_choice == "1":
                    if len(alert_data) == 0:
                        print("No alert locations configured yet. Choose option 2 to add.")
                    else:
                        for loc_id, data in alert_data.items():
                            status = "ON" if data["buzzer_on"] else "OFF"
                            print(f"{loc_id}: {data['location']} - Buzzer {status}, Alerts: {data['alert_count']}")
                elif sub_choice == "2":
                    buzzer.add_alert_location(alert_data)
                elif sub_choice == "3":
                    loc_id = input("Location ID: ")
                    reason = input("Alert reason: ")
                    buzzer.trigger_buzzer(alert_data, loc_id, reason)
                elif sub_choice == "4":
                    loc_id = input("Location ID: ")
                    buzzer.clear_buzzer(alert_data, loc_id)
                elif sub_choice == "5":
                    buzzer.show_alert_stats(alert_data)
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice")
        
        elif choice == "4":
            # System summary and automated alert check
            show_system_summary(temp_data, light_data, alert_data)
            check_all_alerts(temp_data, light_data, alert_data)
        
        elif choice == "5":
            print("\nShutting down monitoring system...")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Enter 1-5")

if __name__ == "__main__":
    main()
