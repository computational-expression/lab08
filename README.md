# Lab 8: IoT Dictionary Practice & Git Collaboration

## Table of Contents

- [Overview](#overview)
- [Learning Goals](#learning-goals)
- [Team Requirements](#team-requirements)
- [Hardware Setup](#hardware-setup)
- [System Architecture](#system-architecture)
- [Program Tasks](#program-tasks)
- [Git Workflow](#git-workflow)
- [Requirements](#requirements)
- [Running the Integrated System](#running-the-integrated-system)
- [Assessment Criteria](#assessment-criteria)
- [Getting Help](#getting-help)
- [Sample Output](#sample-output)

## Overview
In this lab, you will practice Python **dictionary operations** and **collaborative git workflows** by building an **integrated environmental monitoring and alert system**. The system uses three interconnected programs that work together to track hardware inventory, log sensor data, and manage IoT devices with automated alerts. Each team member will work on a different Python file using separate git branches, just like in Activity 8.

## Learning Goals
- Create and modify dictionaries for hardware, sensor, and device management
- Use dictionary methods: `.keys()`, `.values()`, `.items()`
- Practice git branching workflow for team collaboration
- Create and review pull requests on GitHub
- Use input validation and error handling
- Analyze and display statistics from dictionary data

## Team Requirements
**Team Size:** 2-3 students  
**Individual Work:** Each team member works on a **different Python file** using **separate git branches**

### Branch Assignment Strategy:
- **Team Member 1:** `temperature-monitor` branch → `temperature_monitor.py`
- **Team Member 2:** `light-monitor` branch → `light_monitor.py`  
- **Team Member 3:** `buzzer-manager` branch → `buzzer_manager.py`

*(For 2-person teams, two people divide the work of the third program)*

## Hardware Setup

### Required Hardware Components

1. **Temperature/Humidity Sensor**
   - Onboard DHT22 sensor for temperature (-40 to 80°C) and humidity (0-100%)
   - Same as the one in lab 07
   
2. **5528 Light Dependent Resistor (LDR/Photoresistor)**
   - Light-sensitive resistor for ambient light detection
   - Resistance decreases with increased light intensity
   - Useful for automatic lighting and day/night detection

3. **Passive Buzzer Module**
   - Audio alert device for notifications
   - Can produce different tones and patterns
   - Used for temperature/light threshold alerts

### Raspberry Pi Pico 2 WH Pinout Reference

![Pico 2 W Pinout](pico-2-r4-pinout.svg)

*Use this pinout diagram to identify the correct GPIO pins for your connections.*

---

### Breadboard Connections

**Required Materials:**
- Half-size breadboard (30 rows minimum)
- Pico 2 WH
- DHT22 Temperature/Humidity Sensor (3 pins: -, OUT, +)
- LDR (Photoresistor) with 10kΩ resistor
- Passive Buzzer
- Male-to-male jumper wires
- Male-to-female jumper wires

#### Step 1: Mount Pico on Breadboard

Insert your Pico 2 WH into the breadboard:
- **Rows 1-20** (all 20 pins of the Pico)
- **Columns c-h** (spanning the center gap)

**Important:** Make sure Pin 1 (GP0) is in Row 1, Column c (or h on the other side)

---

#### Step 2: Connect DHT22 Temperature/Humidity Sensor

The DHT22 has three pins: **-** (GND), **OUT** (Data), and **+** (Power)

**Connections using male-to-female jumpers:**

1. **GND (-)**: 
   - Male-to-male jumper: Row 3, Column j → negative rail (-)
   - Male-to-female jumper: Row 3, Column a → DHT22 **-** pin

2. **DATA (OUT)**: 
   - Male-to-female jumper: Row 4, Column a → DHT22 **OUT** pin
   - This connects to **GP2** (GPIO 2) on the Pico

3. **POWER (+)**: 
   - Male-to-female jumper: Row 5, Column j → DHT22 **+** pin
   - Power comes from the positive rail (+) which is connected to 3V3

**GPIO Used:** GPIO 2 (GP2) - Physical Pin 4 (Row 4)

---

#### Step 3: Connect LDR (Photoresistor) - Light Sensor

The LDR needs a voltage divider circuit with a 10kΩ resistor.

**Building the Voltage Divider Circuit:**

The photoresistor and resistor create a "voltage divider" - as light changes, the voltage at the middle junction changes, which the Pico can read.

**Step-by-Step Connections:**

1. **10kΩ Resistor:**
   - One leg: Insert into positive rail (+)
   - Other leg: Insert into Row 25, Column j

2. **LDR (Photoresistor):**
   - One leg: Insert into Row 25, Column j (same row and column as resistor - this creates the junction)
   - Other leg: Insert into negative rail (-)

3. **Junction to Pico (ADC):**
   - Male-to-male jumper: Row 25, Column i → Row 10, Column i (GP26)
   - This connects the voltage divider junction to **GP26** on the Pico 
   - **GP26 is the ADC pin** (Analog-to-Digital Converter) that reads voltage levels (can also use GP 27 or GP 28)

**GPIO Used:** GPIO 26 (GP26/ADC0) - Physical row 31 on pinout (Row 10 on the breadboard)

**What's an ADC?** ADC = Analog-to-Digital Converter. It reads the voltage (0V to 3.3V) and converts it to a number (0 to 65535) that Python can use. As light hits the photoresistor, its resistance changes, which changes the voltage at the junction.

**Why the 10kΩ resistor?** Without it, the circuit would short. The resistor and LDR together create different voltages based on light levels.

---

#### Step 4: Buzzer Setup

**Buzzer Physical Placement:**
The passive buzzer has two legs (pins). Place the buzzer on the left side of the breadboard:
- **Positive leg (+):** Row 25, Column a
- **Negative leg (-):** Row 28, Column a

**Buzzer Connections:**
1. **Positive leg → GPIO 15:**
   - Male-to-male jumper: Row 20, Column a (GP15 on Pico) → Row 25, Column b, c, d, or e
   - Any column b-e in Row 25 connects to the buzzer's positive leg (columns a-e are connected horizontally)
   - GPIO 15 controls the buzzer signal
   
2. **Negative leg → Ground:**
   - Male-to-male jumper: Row 28, Column b, c, d, or e → GND (i.e., row 18, Column a)
   - Completes the circuit through ground

**GPIO Used:** GPIO 15 (GP15) - Row 20, Column a

---

#### Complete Wiring Example

![Example](lab08_wiring.jpg)

## System Architecture

The three programs work together as an **Environmental Monitoring and Alert System**:

```
┌─────────────────────────────────────────────────────────────┐
│                      MAIN PROGRAM                            │
│              (Coordinates All Modules)                       │
└────────┬─────────────────┬──────────────────┬───────────────┘
         │                 │                  │
         ▼                 ▼                  ▼
┌────────────────┐  ┌─────────────────┐  ┌──────────────────┐
│  TEMPERATURE   │  │  LIGHT          │  │  BUZZER          │
│  MONITOR       │  │  MONITOR        │  │  MANAGER         │
├────────────────┤  ├─────────────────┤  ├──────────────────┤
│ • DHT22 Sensor │  │ • LDR Sensor    │  │ • Trigger Alerts │
│ • Temp/Humidity│  │ • Light Levels  │  │ • Clear Alerts   │
│ • Check > 25°C │  │ • Check < 200   │  │ • Track Status   │
│ • Check > 60%  │  │ • Brightness    │  │ • Alert Counts   │
└────────────────┘  └─────────────────┘  └──────────────────┘
         │                 │                       ▲
         │ Alert if high   │ Alert if dark         │
         └────────┬────────┘                       │
                  │                                │
             Threshold                             │
             Exceeded?                             │
                  │                                │
                  └────────────────────────────────┘
                          Activate Buzzer
```

### How It Works

1. **Temperature Monitor** tracks DHT22 readings and detects high temperature/humidity
2. **Light Monitor** tracks LDR readings and detects insufficient lighting  
3. **Buzzer Manager** receives alerts and activates buzzers for problem locations
4. **Main Program** coordinates all three and automatically checks thresholds

### Real-World Scenario
Imagine a smart building system that:
- Monitors temperature, humidity, and light in multiple rooms (Lab A, Classroom, Office)
- Detects uncomfortable conditions (too warm, too humid, too dark)
- Automatically triggers buzzer alerts when thresholds are exceeded
- Tracks alert history and current buzzer status for each location

---

## Data Structures Overview

Each program uses **dictionaries with nested dictionaries** to organize sensor data and alert information. Understanding these structures is essential for completing the lab.

### temperature_monitor.py - Temperature Database

**Structure:** Dictionary with string keys (location IDs) and nested dictionary values

```python
readings = {
    "LAB_A": {
        "location": "Lab Room A",      # String: Location name
        "temp": 22.5,                  # Float: Temperature in Celsius
        "humidity": 45.0,              # Float: Humidity percentage
        "comfort": "Good"              # String: Comfort level category
    },
    "CLASSROOM": {
        "location": "Classroom B",
        "temp": 26.3,
        "humidity": 52.0,
        "comfort": "Warm"
    }
}
```

**Key Operations:**
- Access temperature: `readings["LAB_A"]["temp"]`
- Iterate through all: `for loc_id, data in readings.items()`
- Check threshold: `if data["temp"] > 25`

---

### light_monitor.py - Light Level Database

**Structure:** Dictionary with string keys (location IDs) and nested dictionary values

```python
readings = {
    "WINDOW": {
        "location": "Window Area",     # String: Location name
        "light_level": 680,            # Integer: Light level (0-1000)
        "brightness": "Bright"         # String: Brightness category
    },
    "CORNER": {
        "location": "Back Corner",
        "light_level": 150,
        "brightness": "Dark"
    }
}
```

**Key Operations:**
- Access light level: `readings["WINDOW"]["light_level"]`
- Build list of levels: `levels = [data["light_level"] for data in readings.values()]`
- Check threshold: `if data["light_level"] < 200`

---

### buzzer_manager.py - Alert Tracking Database

**Structure:** Dictionary with string keys (location IDs) and nested dictionary values

```python
alerts = {
    "LAB_A": {
        "location": "Lab Room A",      # String: Location name
        "buzzer_on": False,            # Boolean: Current buzzer state
        "alert_count": 0,              # Integer: Total alerts triggered
        "last_reason": "None"          # String: Reason for last alert
    },
    "CLASSROOM": {
        "location": "Classroom B",
        "buzzer_on": True,
        "alert_count": 2,
        "last_reason": "High temperature"
    }
}
```

**Key Operations:**
- Update buzzer state: `alerts["LAB_A"]["buzzer_on"] = True`
- Increment count: `alerts[loc_id]["alert_count"] = alerts[loc_id]["alert_count"] + 1`
- Check active alerts: `if data["buzzer_on"]`

---

### main.py - Integration Variables

**Structure:** Three separate dictionaries (one for each module)

```python
# Created in main()
temp_data = {}      # Holds temperature_monitor readings
light_data = {}     # Holds light_monitor readings
alert_data = {}     # Holds buzzer_manager alerts

# Passed between modules:
check_all_alerts(temp_data, light_data, alert_data)
```

**Integration Flow:**
1. `temp.check_temp_alerts(temp_data)` → Returns list of alert strings
2. `light.check_light_alerts(light_data)` → Returns list of alert strings
3. Alert strings parsed to extract location IDs
4. `buzzer.trigger_buzzer(alert_data, loc_id, reason)` → Updates alert dictionary and sounds buzzer

---

### Alert Functions Return Type: Lists of Strings

Both `check_temp_alerts()` and `check_light_alerts()` return **lists of formatted strings**:

```python
# Example return values:
temp_alerts = [
    "CLASSROOM: Temperature 26.3C is too warm",
    "LAB_A: Humidity 65.0% is too high"
]

light_alerts = [
    "CORNER: Light level 150 is too dark (min 200)"
]
```

**Why lists?** Multiple locations can have alerts simultaneously, so functions return all alerts at once.

---

### Summary of Data Structures Used

| Program | Main Structure | Value Type | Purpose |
|---------|---------------|------------|---------|
| `temperature_monitor.py` | Dictionary | Nested Dictionary | Store temp/humidity readings per location |
| `light_monitor.py` | Dictionary | Nested Dictionary | Store light levels per location |
| `buzzer_manager.py` | Dictionary | Nested Dictionary | Track buzzer state and alert history |
| `check_*_alerts()` | List | Strings | Return multiple alert messages |
| `main.py` | Three separate Dictionaries | Nested Dictionary | Coordinate all modules |

**Nested Dictionary Pattern:** All three modules use `outer_dict[key] = inner_dict` where:
- **Outer key:** Location ID (string like "LAB_A")
- **Inner dictionary:** Contains multiple properties (location name, sensor values, status)

This pattern allows you to store multiple pieces of related information for each location!

---

## Program Tasks

### temperature_monitor.py (Person 1)
**Goal:** Monitor DHT22 temperature and humidity readings with alerts
- Create temperature database for different locations
- Add new location readings (temp, humidity, comfort level)
- Check for temperature/humidity alerts (> 25°C or > 60%)
- Show temperature statistics (averages, ranges)
- **Integration point:** Alerts trigger buzzer when thresholds exceeded

### light_monitor.py (Person 2)
**Goal:** Monitor LDR light levels with alerts
- Create light database for different locations
- Add new light readings with brightness categories
- Check for low light alerts (< 200)
- Show light statistics (averages, categories)
- **Integration point:** Alerts trigger buzzer when light too low

### buzzer_manager.py (Person 3 or shared)
**Goal:** Manage buzzer alert system for all locations
- Create alert database tracking buzzer status
- Add new alert locations
- Trigger buzzer alerts with reason
- Clear buzzer alerts
- Show alert statistics (active alerts, total counts)
- **Integration point:** Receives alerts from temperature and light monitors

## Git Workflow

### Step 1: Setup
1. **Repository Keeper:** Accept GitHub Classroom assignment first
2. **Team Members:** Join the same team via GitHub Classroom link
3. **Everyone:** Clone the repository to your local machine

### Step 2: Create Your Branch
```bash
# Check current branch
git branch

# Create and switch to your assigned branch
git checkout -b your_branch_name
```

### Step 3: Work on Your File
- Edit only YOUR assigned Python file
- Test your program frequently
- Commit your changes regularly:
```bash
git add src/your_file.py
git commit -m "Add function to create database"
```

### Step 4: Push and Create Pull Request
```bash
# Push your branch to GitHub
git push origin your-branch-name

Go to GitHub and create a Pull Request

Request review from one of your team members and one TL
```

### Step 5: Review Team Members' Code
- Review at least one teammate's pull request
- Leave constructive comments
- Approve when code looks good

### Step 6: Merge Pull Requests
- After receiving approval, merge your PR to main
- Pull the latest main branch:
```bash
git checkout main
git pull origin main
```

## Requirements

### Individual Module Requirements
- Each program should use at least one **dictionary** with nested data
- Implement exactly 4 core functions: create, add, check alerts, and show stats
- Use input validation and error handling (try/except for numbers)
- Print clear, organized output for user

### Integration Requirements
- **temperature_monitor.py** must include `check_temp_alerts()` function
- **light_monitor.py** must include `check_light_alerts()` function
- **buzzer_manager.py** must include `trigger_buzzer()` and `clear_buzzer()` functions
- **main.py** coordinates all modules and handles automated alert checking
- System should automatically check thresholds and trigger buzzers when needed

## Reflection
Write a team reflection in `writing/reflection.md` about (each person contributes):
- What you learned about dictionaries
- How git branching helped your team collaborate
- Challenges you faced and how you solved them
- How your program models real IoT systems

## Submission
1. All team members merge their branches to main
2. Verify all three programs run correctly
3. Complete the team reflection
4. Check GatorGrade for automated feedback
5. Submit your repository link

## Running the Integrated System

Once all team members have completed their modules, run the integrated system by running `main.py`

### How the Integration Works

The main program coordinates all three modules to create a complete environmental monitoring and alert system:

1. **Temperature Monitor** tracks DHT22 readings for multiple locations
   - Checks if temp > 25°C or humidity > 60%
   - Returns list of alerts
   
2. **Light Monitor** tracks LDR readings for multiple locations  
   - Checks if light < 200 (too dark)
   - Returns list of alerts
   
3. **Buzzer Manager** receives alerts from both monitors
   - Activates buzzer for problem locations
   - Tracks alert count and reason
   
4. **Main Program** coordinates everything
   - Calls `check_all_alerts()` to scan all sensors
   - Automatically triggers buzzers when thresholds exceeded
   - Provides system-wide summary

### Example Alert Flow

```
Location: CLASSROOM

1. Temperature Monitor reads: 26.3°C (exceeds 25°C)
2. check_temp_alerts() returns: "CLASSROOM: Temperature 26.3C is too warm"
3. Main program sees alert
4. Calls buzzer.trigger_buzzer(alerts, "CLASSROOM", "High temperature")
5. Buzzer activated for CLASSROOM
6. System displays: "BUZZER ON at CLASSROOM: High temperature"
```

## Getting Help
- Ask your instructor or TLs for help during lab
- Use course slides and Activity 8 for git workflow reference
- Review Python documentation for dictionaries

## Assessment Criteria

### Technical Implementation (3 points)
- **Automated GatorGrade checks:** All required functions implemented correctly
- **Dictionary operations:** Creating, accessing, modifying, and iterating through dictionaries
- **Error handling:** Input validation and graceful error handling
- **Code functionality:** Programs run without errors and produce correct output

### Git Workflow and Collaboration (1 points)
- Proper branch creation and naming
- Pull request quality and code reviews
- Professional communication with team members

### Reflection (0.5 points)
- Personal insights on dictionary concepts and collaboration
- What you learned and challenges you faced

## Submission Instructions

1. **Ensure all pull requests are merged** into main branch
2. **Verify the integrated system works** by running `python3 src/main.py`
3. **Complete team reflection** in `writing/reflection.md`
4. **Check GatorGrade** for automated feedback
5. **Submit GitHub repository link**

## Getting Help

### During Lab
- **Ask TLs or instructor** for help with dictionary concepts or git workflow
- **Collaborate with teammates** on understanding requirements
- **Use pair programming** for complex functions (but ensure individual contribution)

### Outside Lab
- **Post questions in Discord** with specific code snippets or error messages
- **Attend office hours** for individual help with concepts
- **Review course slides** on dictionaries and git workflows

### Resources
- [Python Dictionary Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Git Branching Tutorial](https://learngitbranching.js.org/)
- [GitHub Pull Request Guide](https://docs.github.com/en/pull-requests)
- Course slides on dictionaries and collaborative development

## Sample Output

### Running Individual Modules

#### temperature_monitor.py
```
$ python3 temperature_monitor.py
Temperature monitor initialized

Temperature Monitor:
1. View all
2. Add location
3. Check alerts
4. Show stats
5. Exit
Choice: 1
LAB_A: Lab Room A - 22.5C, 45.0%, Good
CLASSROOM: Classroom B - 26.3C, 52.0%, Warm
OFFICE: Office - 23.1C, 48.0%, Good

Temperature Monitor:
1. View all
2. Add location
3. Check alerts
4. Show stats
5. Exit
Choice: 4
Total locations: 3
Average temp: 23.9C
Average humidity: 48.3%
Range: 22.5C to 26.3C

ALERTS:
  - CLASSROOM: Temperature 26.3C is too warm
```

#### light_monitor.py
```
$ python3 light_monitor.py
Light monitor initialized

Light Monitor:
1. View all
2. Add location
3. Check alerts
4. Show stats
5. Exit
Choice: 4
Total locations: 3
Average light: 403
Range: 150 to 680
Bright: 1, Medium: 1, Dark: 1

ALERTS:
  - CORNER: Light level 150 is too dark (min 200)
```

#### buzzer_manager.py
```
$ python3 buzzer_manager.py
Buzzer alert manager initialized

Buzzer Alert Manager:
1. View all
2. Add location
3. Trigger buzzer
4. Clear buzzer
5. Show stats
6. Exit
Choice: 1
LAB_A: Lab Room A - Buzzer OFF, Alerts: 0
CLASSROOM: Classroom B - Buzzer ON, Alerts: 2
OFFICE: Office - Buzzer OFF, Alerts: 1

Buzzer Alert Manager:
1. View all
2. Add location
3. Trigger buzzer
4. Clear buzzer
5. Show stats
6. Exit
Choice: 5
Total locations: 3
Active buzzers: 1
Total alerts triggered: 3
Average alerts per location: 1.0
Range: 0 to 2

ALERT HISTORY:
  - CLASSROOM: 2 alerts, Last: High temperature
  - OFFICE: 1 alerts, Last: Low light
```

### Running Integrated System

#### main.py - System Menu and Automated Alerts
```
$ python3 main.py
==================================================
 ENVIRONMENTAL MONITORING SYSTEM
==================================================

Initializing hardware components...
  - DHT22 Temperature/Humidity Sensor (GPIO 2)
  - LDR Photoresistor (GPIO 26)
  - Passive Buzzer (GPIO 15)

[Temperature Monitor]
Temperature monitor initialized

[Light Monitor]
Light monitor initialized

[Buzzer Alert Manager]
Buzzer alert manager initialized

==================================================
 ALL SYSTEMS READY!
==================================================

This system uses dictionaries to manage:
  • Temperature/humidity readings from DHT22
  • Light levels from LDR
  • Alert status and buzzer control

Start by adding locations in each module,
then use 'System Summary & Alerts' to check all sensors!
==================================================

==================================================
   ENVIRONMENTAL MONITORING SYSTEM
==================================================

Select a module:
1. Temperature Monitor (DHT22)
2. Light Monitor (LDR)
3. Buzzer Alert Manager
4. System Summary & Alerts
5. Exit
--------------------------------------------------
Enter choice (1-5): 4

==================================================
   SYSTEM SUMMARY
==================================================

TEMPERATURE MONITOR:
Total locations: 3
Average temp: 23.9C
Average humidity: 48.3%
Range: 22.5C to 26.3C

ALERTS:
  - CLASSROOM: Temperature 26.3C is too warm

--------------------------------------------------

LIGHT MONITOR:
Total locations: 3
Average light: 403
Range: 150 to 680
Bright: 1, Medium: 1, Dark: 1

ALERTS:
  - CORNER: Light level 150 is too dark (min 200)

--------------------------------------------------

BUZZER ALERTS:
Total locations: 3
Active buzzers: 2
Total alerts triggered: 5
Average alerts per location: 1.7
Range: 0 to 2

ALERT HISTORY:
  - CLASSROOM: 2 alerts, Last: High temperature
  - CORNER: 2 alerts, Last: Low light
  - OFFICE: 1 alerts, Last: Low light

==================================================

==================================================
   CHECKING ALL SENSORS
==================================================

Temperature Status:
  WARNING: CLASSROOM: Temperature 26.3C is too warm
BUZZER ON at CLASSROOM: High temperature

Light Status:
  WARNING: CORNER: Light level 150 is too dark (min 200)
BUZZER ON at CORNER: Low light

Buzzer Status:
  2 active alert(s)
    - CLASSROOM: High temperature
    - CORNER: Low light

  Physical buzzer was activated!
==================================================

==================================================
   ENVIRONMENTAL MONITORING SYSTEM
==================================================

Select a module:
1. Temperature Monitor (DHT22)
2. Light Monitor (LDR)
3. Buzzer Alert Manager
4. System Summary & Alerts
5. Exit
--------------------------------------------------
Enter choice (1-5): 5

Shutting down monitoring system...
Goodbye!
```
