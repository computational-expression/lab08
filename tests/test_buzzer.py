"""
Test script for Passive Buzzer on GPIO 15
Run this on the Pico to test if your buzzer is connected correctly.
BUZZER PLACEMENT: + in Row 25, - in Row 28, Column a
GP15 connection: Row 20, Column a
"""

from machine import Pin, PWM
import time

print("Testing Buzzer on GPIO 15 (Pin 20)")
print("Buzzer should be: + in Row 25, - in Row 28\n")

# Try basic digital pin test first
print("Test 1: Digital Pin On/Off Test")
print("This tests basic connection...")
buzzer_pin = Pin(15, Pin.OUT)
for i in range(3):
    print(f"  Beep {i+1}")
    buzzer_pin.on()
    time.sleep(0.2)
    buzzer_pin.off()
    time.sleep(0.2)
print("Did you hear 3 clicks? (If yes, buzzer is connected)")
time.sleep(2)

# Now try PWM with different settings
print("\nTest 2: PWM Test with Different Frequencies")
buzzer = PWM(Pin(15))

def play_tone(frequency, duration, duty=32768):
    """Play a tone at the given frequency for the specified duration."""
    try:
        buzzer.freq(frequency)
        buzzer.duty_u16(duty)  # duty cycle
        time.sleep(duration)
        buzzer.duty_u16(0)  # Turn off
    except Exception as e:
        print(f"Error: {e}")

print("Testing frequencies: 500Hz, 1000Hz, 2000Hz, 4000Hz")
test_freqs = [500, 1000, 2000, 4000]
for freq in test_freqs:
    print(f"  Playing {freq}Hz...")
    play_tone(freq, 0.5)
    time.sleep(0.3)
print("Did you hear 4 different tones?\n")
time.sleep(2)

# Test different duty cycles
print("Test 3: Testing Different Volumes (Duty Cycles)")
print("Playing same tone at different volumes...")
for duty in [16384, 32768, 49152]:  # 25%, 50%, 75%
    percent = int((duty / 65535) * 100)
    print(f"  Volume {percent}%")
    play_tone(1000, 0.5, duty)
    time.sleep(0.3)
print()
time.sleep(2)

def play_beep_pattern():
    """Play a simple beep pattern."""
    print("Playing beep pattern...")
    for i in range(3):
        play_tone(2000, 0.2)  # Short beep at 2000 Hz (louder for passive buzzers)
        time.sleep(0.2)       # Pause

def play_scale():
    """Play a simple musical scale."""
    print("Playing musical scale...")
    notes = [262, 294, 330, 349, 392, 440, 494, 523]  # C, D, E, F, G, A, B, C
    for freq in notes:
        play_tone(freq, 0.3)
        time.sleep(0.1)

def play_alarm():
    """Play an alarm sound."""
    print("Playing alarm sound...")
    for i in range(5):
        play_tone(2000, 0.2)
        time.sleep(0.1)
        play_tone(1000, 0.2)
        time.sleep(0.1)

try:
    print("=" * 50)
    print("INTERACTIVE TESTS")
    print("=" * 50)
    while True:
        print("\n1. Beep Pattern")
        print("2. Musical Scale")
        print("3. Alarm Sound")
        print("4. Custom Frequency Test")
        print("5. Exit")
        
        choice = input("Choose a test (1-5): ")
        
        if choice == "1":
            play_beep_pattern()
        elif choice == "2":
            play_scale()
        elif choice == "3":
            play_alarm()
        elif choice == "4":
            try:
                freq = int(input("Enter frequency (100-5000 Hz): "))
                if 100 <= freq <= 5000:
                    print(f"Playing {freq}Hz for 1 second...")
                    play_tone(freq, 1.0)
                else:
                    print("Frequency out of range")
            except ValueError:
                print("Invalid number")
        elif choice == "5":
            print("Test complete")
            break
        else:
            print("Invalid choice")
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\nTest stopped")
finally:
    buzzer.duty_u16(0)  # Ensure buzzer is off
