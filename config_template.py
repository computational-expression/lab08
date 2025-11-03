# Configuration file for IoT Weather Station
# Lab 08 - CS 100 Fall 2025
# NOTE: This file should NOT be committed to git (add to .gitignore)

# WiFi Configuration
WIFI_SSID = "your_wifi_network_name"
WIFI_PASSWORD = "your_wifi_password"

# Hardware Configuration
DHT_PIN = 2      # GPIO pin for DHT22 sensor
BUZZER_PIN = 15  # GPIO pin for buzzer
SPEAKER_PIN = 14 # GPIO pin for speaker

# API Configuration
DEFAULT_CITY = "Meadville,PA"
API_TIMEOUT = 10  # seconds

# Alert Thresholds
TEMP_HOT_THRESHOLD = 30   # Celsius
TEMP_COLD_THRESHOLD = 10  # Celsius
HUMIDITY_HIGH_THRESHOLD = 80  # Percent

# Audio Settings
ALERT_VOLUME = 0.3      # 0.0 to 1.0
TONE_DURATION = 200     # milliseconds