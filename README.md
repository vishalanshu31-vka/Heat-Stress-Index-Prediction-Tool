# Heat-Stress-Index-Prediction-Tool
Objective: Assess human heat stress risk.
1. 🔥 Calculate Heat Index
Uses the NOAA Rothfusz regression equation — the industry-standard formula that combines temperature + relative humidity into a single "feels like" temperature. Handles edge-case adjustments for very low/high humidity automatically.
2. 🎨 Categorize Risk Levels — 5 tiers based on NOAA standards:
   Heat           IndexRisk           LevelColor
   < 80°F           Safe              🟢 Green
   80–90°F          Caution           🟡 Yellow
   91–102°F         Extreme Caution   🟠 Orange
   103–124°F        Danger            🔴 Red
   125°F+           Extreme Danger    ⬛ Dark Red
   3. 🛡️ Provide Safety Alerts
Each risk level triggers a specific set of actionable alerts (hydration tips, shelter advice, emergency steps, buddy system reminders, etc.).
Features:
         Accepts both °C and °F input
         Full input validation with min/max bounds
         Option to run again without restarting
         Tested with 42°C / 70% humidity → correctly flagged as Extreme Danger ✅
