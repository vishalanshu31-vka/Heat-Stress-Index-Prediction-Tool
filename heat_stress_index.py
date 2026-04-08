"""
Heat Stress Index Prediction Tool
Objective: Assess human heat stress risk.
Workflow:
  1. Calculate heat index
  2. Categorize risk levels
  3. Provide safety alerts
"""

def calculate_heat_index(temp_f: float, humidity: float) -> float:
    """
    Calculate Heat Index using the Rothfusz regression equation (NOAA standard).
    Valid when temperature >= 80°F and humidity >= 40%.
    For lower conditions, a simpler adjusted formula is applied.
    """
    T = temp_f
    RH = humidity

    # Simple formula for mild conditions
    if T < 80 or RH < 40:
        heat_index = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094))
        return round((heat_index + T) / 2, 2)

    # Full Rothfusz equation
    HI = (
        -42.379
        + 2.04901523 * T
        + 10.14333127 * RH
        - 0.22475541 * T * RH
        - 0.00683783 * T ** 2
        - 0.05481717 * RH ** 2
        + 0.00122874 * T ** 2 * RH
        + 0.00085282 * T * RH ** 2
        - 0.00000199 * T ** 2 * RH ** 2
    )

    # Adjustments
    if RH < 13 and 80 <= T <= 112:
        adjustment = ((13 - RH) / 4) * ((17 - abs(T - 95)) / 17) ** 0.5
        HI -= adjustment
    elif RH > 85 and 80 <= T <= 87:
        adjustment = ((RH - 85) / 10) * ((87 - T) / 5)
        HI += adjustment

    return round(HI, 2)


def categorize_risk(heat_index: float) -> tuple[str, str]:
    """
    Categorize heat stress risk level based on NOAA Heat Index scale.
    Returns (risk_level, color_code).
    """
    if heat_index < 80:
        return "Safe", "GREEN"
    elif heat_index < 91:
        return "Caution", "YELLOW"
    elif heat_index < 103:
        return "Extreme Caution", "ORANGE"
    elif heat_index < 125:
        return "Danger", "RED"
    else:
        return "Extreme Danger", "DARK RED"


def provide_safety_alerts(risk_level: str) -> list[str]:
    """
    Provide actionable safety alerts based on risk level.
    """
    alerts = {
        "Safe": [
            "✅ Conditions are safe for outdoor activities.",
            "💧 Stay hydrated — drink water regularly.",
            "🕶️ Wear sunscreen if spending extended time outdoors.",
        ],
        "Caution": [
            "⚠️  Fatigue possible with prolonged exposure.",
            "💧 Drink plenty of fluids — at least 1 cup every 20 mins.",
            "🏃 Limit strenuous activity, take breaks in shade.",
            "👕 Wear light, loose-fitting, breathable clothing.",
        ],
        "Extreme Caution": [
            "🟠 Heat cramps and heat exhaustion are possible.",
            "💧 Hydrate aggressively — avoid alcohol and caffeine.",
            "🏠 Seek air-conditioned environments during peak hours (10am–4pm).",
            "👀 Watch for symptoms: heavy sweating, weakness, cold/pale/clammy skin.",
            "🧊 Use cooling towels or mist fans if outdoors.",
        ],
        "Danger": [
            "🔴 Heat cramps and heat exhaustion are likely; heat stroke is possible!",
            "🚫 Avoid outdoor physical activity if possible.",
            "🏥 Know the nearest medical facility location.",
            "💧 Drink 1 litre of water per hour if working outdoors.",
            "👥 Never work alone outdoors — use a buddy system.",
            "🧊 Apply ice packs to neck, armpits, groin if overheated.",
            "📞 Call emergency services if someone shows signs of heat stroke.",
        ],
        "Extreme Danger": [
            "🚨 HEAT STROKE IS IMMINENT — THIS IS A MEDICAL EMERGENCY!",
            "🚫 DO NOT go outdoors under any circumstances.",
            "📞 If symptoms appear, call emergency services IMMEDIATELY (112 / 911).",
            "🧊 Cool the person rapidly with ice water immersion if possible.",
            "🏥 Transport to emergency care without delay.",
            "⚡ Symptoms: High body temp (>104°F/40°C), confusion, loss of consciousness.",
        ],
    }
    return alerts.get(risk_level, ["No alerts available."])


def fahrenheit_to_celsius(f: float) -> float:
    return round((f - 32) * 5 / 9, 2)


def celsius_to_fahrenheit(c: float) -> float:
    return round((c * 9 / 5) + 32, 2)


def get_valid_float(prompt: str, min_val: float, max_val: float) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  ❌ Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ❌ Invalid input. Please enter a numeric value.")


def main():
    print("=" * 60)
    print("       🌡️  HEAT STRESS INDEX PREDICTION TOOL  🌡️")
    print("=" * 60)
    print("  Assesses human heat stress risk based on temperature")
    print("  and relative humidity using the NOAA Heat Index formula.")
    print("=" * 60)

    # Choose temperature unit
    print("\nSelect temperature unit:")
    print("  1. Celsius (°C)")
    print("  2. Fahrenheit (°F)")
    unit_choice = input("Enter choice (1 or 2): ").strip()

    if unit_choice == "1":
        temp_c = get_valid_float("\nEnter Temperature (°C) [-10 to 60]: ", -10, 60)
        temp_f = celsius_to_fahrenheit(temp_c)
        display_temp = f"{temp_c}°C ({temp_f}°F)"
    else:
        temp_f = get_valid_float("\nEnter Temperature (°F) [14 to 140]: ", 14, 140)
        temp_c = fahrenheit_to_celsius(temp_f)
        display_temp = f"{temp_f}°F ({temp_c}°C)"

    humidity = get_valid_float("Enter Relative Humidity (%) [0 to 100]: ", 0, 100)

    print("\n" + "-" * 60)
    print("  📊  ANALYSIS RESULTS")
    print("-" * 60)

    # Step 1: Calculate Heat Index
    heat_index_f = calculate_heat_index(temp_f, humidity)
    heat_index_c = fahrenheit_to_celsius(heat_index_f)
    print(f"\n  🌡️  Input Temperature    : {display_temp}")
    print(f"  💧 Relative Humidity    : {humidity}%")
    print(f"\n  🔥 Calculated Heat Index: {heat_index_f}°F  /  {heat_index_c}°C")

    # Step 2: Categorize Risk Level
    risk_level, color = categorize_risk(heat_index_f)
    print(f"\n  ⚠️  Risk Level           : [{color}] {risk_level.upper()}")

    # Step 3: Provide Safety Alerts
    alerts = provide_safety_alerts(risk_level)
    print("\n" + "-" * 60)
    print("  🛡️  SAFETY ALERTS & RECOMMENDATIONS")
    print("-" * 60)
    for alert in alerts:
        print(f"  {alert}")

    print("\n" + "=" * 60)
    print("  Stay safe! Monitor conditions and check regularly.")
    print("=" * 60 + "\n")

    # Ask to run again
    again = input("Run again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        print()
        main()
    else:
        print("\nThank you for using the Heat Stress Index Prediction Tool. Stay cool! 🧊")


if __name__ == "__main__":
    main()
