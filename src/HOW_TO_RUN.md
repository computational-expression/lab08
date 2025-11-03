# How to Run the Environmental Monitoring System

## Files Required

You need to upload **ALL FOUR** Python files to your Pico:

1. `main.py` - Main program with menu system
2. `temperature_monitor.py` - DHT22 sensor module
3. `light_monitor.py` - LDR sensor module
4. `buzzer_manager.py` - Buzzer control module

## Upload Instructions (Using MicroPico Extension)

### Method 1: Upload All Files at Once
1. In VS Code, open the `src` folder
2. Select all four `.py` files (Cmd+Click or Ctrl+Click each file)
3. Right-click → "Upload to Pico"
4. Wait for all files to transfer

### Method 2: Upload Files Individually
1. Open `temperature_monitor.py`
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type "MicroPico: Upload current file to Pico"
4. Press Enter
5. Repeat for `light_monitor.py`, `buzzer_manager.py`, and `main.py`

## Running the Program

### Option 1: Run Directly from VS Code
1. Open `main.py` in VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type "MicroPico: Run current file on Pico"
4. Press Enter

### Option 2: Run from Pico Terminal
1. Connect to the Pico terminal (MicroPico vREPL)
2. Type: `import main`
3. Press Enter

### Option 3: Auto-run on Pico Boot
1. Upload all four files as described above
2. Rename `main.py` to `main.py` on the Pico (it's already the right name)
3. Create a file called `boot.py` with this content:
   ```python
   import main
   ```
4. The program will run automatically when you plug in the Pico

## Verifying Files Are Uploaded

In the MicroPico vREPL terminal, type:
```python
import os
print(os.listdir())
```

You should see all four files listed:
- `main.py`
- `temperature_monitor.py`
- `light_monitor.py`
- `buzzer_manager.py`

## Troubleshooting

### ImportError: no module named 'temperature_monitor'
**Problem:** Not all files were uploaded to the Pico.

**Solution:** 
1. Check which files are on the Pico: `import os; print(os.listdir())`
2. Upload missing files using Method 1 or 2 above
3. Make sure all files are in the root directory (not in a subfolder)

### Program runs but sensors don't work
**Problem:** Hardware not connected correctly.

**Solution:**
1. Run the test programs first:
   - `tests/test_dht22.py` - Test temperature sensor
   - `tests/test_ldr.py` - Test light sensor
   - `tests/test_buzzer.py` - Test buzzer
2. Verify wiring matches the README.md instructions

### Can't see output
**Problem:** Not connected to the terminal.

**Solution:**
1. Open MicroPico vREPL terminal in VS Code
2. Click the terminal to make sure it's active
3. Run the program again

## Quick Start Guide

1. **Upload all 4 files** to Pico
2. **Run** `main.py`
3. **Add locations** in each module (Temperature, Light, Buzzer)
4. **Check System Summary** (option 4) to see all data and trigger alerts
5. **Experiment** with covering the LDR or heating the DHT22 to trigger alerts

## Hardware Requirements

- Raspberry Pi Pico 2 WH
- DHT22 Temperature/Humidity Sensor (GPIO 2)
- LDR Photoresistor (GPIO 26)
- Passive Buzzer (GPIO 15)
- Breadboard and jumper wires

See main `README.md` for complete wiring diagrams.
