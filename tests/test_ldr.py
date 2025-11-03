"""
Test script for LDR (Photoresistor) on GPIO 26 (ADC0)
Run this on the Pico to test if your LDR is working correctly.
"""

from machine import Pin, ADC
import time

# Set up ADC on GPIO 26 (ADC0)
ldr = ADC(Pin(26))

print("Testing LDR on GPIO 26 (Pin 31)")
print("Cover the sensor with your hand to see values change")
print("Press Ctrl+C to stop\n")

try:
    while True:
        # Read raw ADC value (0-65535)
        raw_value = ldr.read_u16()
        
        # Convert to 0-1000 scale for easier reading
        light_level = int((raw_value / 65535) * 1000)
        
        # Determine brightness category
        if light_level > 500:
            brightness = "Bright"
        elif light_level > 200:
            brightness = "Medium"
        else:
            brightness = "Dark"
        
        print(f"Raw: {raw_value:5d} | Light Level: {light_level:4d} | {brightness}")
        
        time.sleep(0.5)  # Update every 0.5 seconds
        
except KeyboardInterrupt:
    print("\nTest stopped")
