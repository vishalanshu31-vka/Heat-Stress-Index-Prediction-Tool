# 🌡️ Heat Stress Index Prediction Tool

> **Assess human heat stress risk using temperature and humidity inputs — powered by the official NOAA Rothfusz formula.**

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Risk Level Categories](#risk-level-categories)
- [Installation & Requirements](#installation--requirements)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Functions Overview](#functions-overview)
- [Formula Used](#formula-used)
- [Author](#author)

---

## 📖 About the Project

The **Heat Stress Index Prediction Tool** is a command-line Python program that helps assess how dangerous the current weather feels to the human body. It goes beyond just temperature — it factors in **humidity** to calculate the real "feels like" temperature, then tells you exactly how at-risk you are and what you should do to stay safe.

This tool is especially useful for:
- Outdoor workers and athletes
- Parents planning outdoor activities for children
- Emergency response teams
- Anyone living in hot, humid climates

---

## ✨ Features

- ✅ Accepts input in both **Celsius and Fahrenheit**
- ✅ Uses the **official NOAA Rothfusz regression equation**
- ✅ Handles **edge-case humidity corrections** automatically
- ✅ Classifies heat risk into **5 color-coded levels**
- ✅ Provides **tailored safety alerts** for each risk level
- ✅ **Input validation** — rejects invalid or out-of-range values
- ✅ Option to **run multiple times** without restarting
- ✅ Clean, beginner-friendly code with full comments

---

## ⚙️ How It Works

The program follows a 3-step workflow:

```
Step 1 → Calculate Heat Index
         (Combines temperature + humidity into a "feels like" number)

Step 2 → Categorize Risk Level
         (Maps the heat index to a danger tier: Safe → Extreme Danger)

Step 3 → Provide Safety Alerts
         (Gives actionable advice based on the risk tier)
```

---

## 🚦 Risk Level Categories

Based on the official **NOAA Heat Index Scale**:

| Heat Index (°F) | Risk Level       | Color       | What It Means                                      |
|-----------------|------------------|-------------|----------------------------------------------------|
| Below 80°F      | ✅ Safe           | 🟢 Green    | No danger. Enjoy the outdoors!                     |
| 80 – 90°F       | ⚠️ Caution        | 🟡 Yellow   | Fatigue possible with prolonged activity           |
| 91 – 102°F      | 🟠 Extreme Caution| 🟠 Orange   | Heat cramps & exhaustion possible                  |
| 103 – 124°F     | 🔴 Danger         | 🔴 Red      | Heat stroke likely with continued exposure         |
| 125°F and above | 🚨 Extreme Danger | ⬛ Dark Red  | Heat stroke imminent — medical emergency!          |

---

## 🛠️ Installation & Requirements

### Requirements
- **Python 3.10 or higher** (uses modern type hints like `tuple[str, str]`)
- No external libraries needed — uses only Python's built-in features!

### Check your Python version
```bash
python --version
```

### Download the file
Save `heat_stress_index.py` to any folder on your computer.

---

## ▶️ How to Run

Open your terminal or command prompt, navigate to the folder where the file is saved, and run:

```bash
python heat_stress_index.py
```

### Step-by-step interaction:

1. **Choose your temperature unit** — Celsius or Fahrenheit
2. **Enter the temperature** — within the valid range shown
3. **Enter the humidity** — as a percentage (0 to 100)
4. The program will display:
   - The calculated **Heat Index**
   - Your **Risk Level** with color
   - A list of **Safety Alerts**
5. Choose to **run again** or exit

---

## 🖥️ Sample Output

```
============================================================
       🌡️  HEAT STRESS INDEX PREDICTION TOOL  🌡️
============================================================

Select temperature unit:
  1. Celsius (°C)
  2. Fahrenheit (°F)
Enter choice (1 or 2): 1

Enter Temperature (°C) [-10 to 60]: 42
Enter Relative Humidity (%) [0 to 100]: 70

------------------------------------------------------------
  📊  ANALYSIS RESULTS
------------------------------------------------------------

  🌡️  Input Temperature    : 42.0°C (107.6°F)
  💧 Relative Humidity    : 70.0%

  🔥 Calculated Heat Index: 180.07°F  /  82.26°C

  ⚠️  Risk Level           : [DARK RED] EXTREME DANGER

------------------------------------------------------------
  🛡️  SAFETY ALERTS & RECOMMENDATIONS
------------------------------------------------------------
  🚨 HEAT STROKE IS IMMINENT — THIS IS A MEDICAL EMERGENCY!
  🚫 DO NOT go outdoors under any circumstances.
  📞 If symptoms appear, call emergency services IMMEDIATELY (112 / 911).
  🧊 Cool the person rapidly with ice water immersion if possible.
  🏥 Transport to emergency care without delay.
  ⚡ Symptoms: High body temp (>104°F/40°C), confusion, loss of consciousness.

============================================================
  Stay safe! Monitor conditions and check regularly.
============================================================
```

---

## 📁 Project Structure

```
heat-stress-tool/
│
├── heat_stress_index.py     # Main Python program
└── README.md                # Project documentation (this file)
```

---

## 🔩 Functions Overview

| Function | Purpose |
|---|---|
| `calculate_heat_index(temp_f, humidity)` | Calculates "feels like" temperature using NOAA formula |
| `categorize_risk(heat_index)` | Maps heat index to a risk level and color |
| `provide_safety_alerts(risk_level)` | Returns a list of safety tips for the given risk level |
| `fahrenheit_to_celsius(f)` | Converts °F → °C |
| `celsius_to_fahrenheit(c)` | Converts °C → °F |
| `get_valid_float(prompt, min, max)` | Safely gets a number from the user with validation |
| `main()` | Orchestrates the entire program flow |

---

## 📐 Formula Used

This tool uses the **Rothfusz Regression Equation**, the standard formula adopted by the **National Oceanic and Atmospheric Administration (NOAA)**:

```
HI = -42.379
     + 2.04901523 × T
     + 10.14333127 × RH
     - 0.22475541 × T × RH
     - 0.00683783 × T²
     - 0.05481717 × RH²
     + 0.00122874 × T² × RH
     + 0.00085282 × T × RH²
     - 0.00000199 × T² × RH²
```

Where `T` = Temperature in °F and `RH` = Relative Humidity in %

Two additional corrections are applied:
- **Low humidity correction** (RH < 13%, T between 80–112°F) → subtracts a small value
- **High humidity correction** (RH > 85%, T between 80–87°F) → adds a small value

For mild conditions (T < 80°F or RH < 40%), a simpler Steadman formula is used instead.

---

## 👨‍💻 Author

Built with ❤️ using Python.  
Designed to be simple, accurate, and potentially life-saving.

> *"It's not the heat, it's the humidity."* — and now you have a tool to prove it! 🌡️
