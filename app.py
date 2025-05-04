import streamlit as st

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌱")
st.title("🌍 Carbon Footprint Calculator and Suggestions")

st.markdown("""
---
### 🧠 What is Carbon Footprint?

Your **carbon footprint** is the total amount of greenhouse gases — especially carbon dioxide (CO₂) — that are released into the atmosphere as a result of your daily activities.

This includes:
- 🚗 How much you travel by car, bus, or plane  
- ⚡ How much electricity you use  
- 🍽️ What kind of food you eat  

### A smaller carbon footprint means you're contributing less to climate change — and this app helps you **understand and reduce yours**!
---
""")

st.markdown("""
Estimate your **weekly carbon footprint** from:
- 🚗 Travel (car, bus, flights)
- ⚡ Electricity usage
- 🍽️ Dietary habits

Get personalized suggestions to lower your footprint 🌿
""")

# --- Inputs ---
car_km = st.number_input("🚗 Car travel in km/week", 0.0)
bus_km = st.number_input("🚌 Bus/Metro travel in km/week", 0.0)
flight_km = st.number_input("✈️ Flight travel in km/week", 0.0)
kwh = st.number_input("⚡ Electricity usage (kWh/week)", 0.0)
diet = st.selectbox("🍽️ Diet Type", ["Meat", "Mixed", "Vegetarian"])

# --- Emission Calculation ---
def calculate_emissions(car, bus, flight, energy, diet_type):
    travel = car * 0.192 + bus * 0.105 + flight * 0.255
    electricity = energy * 0.7
    if diet_type == 'Meat':
        food = 7 * 27
    elif diet_type == 'Mixed':
        food = 7 * 4
    else:  # Vegetarian
        food = 7 * 2
    total = travel + electricity + food
    return round(travel, 2), round(electricity, 2), round(food, 2), round(total, 2)

# --- Personalized Suggestions ---
def get_suggestions(car, bus, flight, energy, diet_type):
    suggestions = []

    if car > 100:
        suggestions.append("🚘 You use a car frequently — consider carpooling or working remotely 1–2 days/week.")
    elif 0 < car <= 100:
        suggestions.append("🚙 Moderate car use — great! Try combining trips to save more.")

    if bus + flight == 0 and car > 0:
        suggestions.append("🚌 You don’t use public transport — try switching 1–2 days/week to bus or metro.")

    if flight > 200:
        suggestions.append("✈️ Consider reducing flights — try trains for short distances or virtual meetings.")
    elif 0 < flight <= 200:
        suggestions.append("🛬 Occasional flights — great! Stick to direct flights to reduce emissions.")

    if energy > 100:
        suggestions.append("💡 High electricity use — consider switching to LED bulbs or reducing AC use.")
    elif 50 < energy <= 100:
        suggestions.append("🔌 Moderate energy usage — unplug devices when not in use.")

    if diet_type == 'Meat':
        suggestions.append("🥩 Meat-rich diet — try one or two vegetarian days per week to reduce food emissions.")
    elif diet_type == 'Mixed':
        suggestions.append("🥗 Mixed diet — great start! Replacing red meat with legumes helps further.")
    elif diet_type == 'Vegetarian':
        suggestions.append("🌿 Vegetarian diet — excellent for carbon savings!")

    if not suggestions:
        suggestions.append("🎉 Your habits already reflect a low-carbon lifestyle! Keep it up!")

    return suggestions

# --- Impact Classification ---
def classify_impact(total):
    if total < 50:
        return "🌱 Low Impact", "You’re doing amazing for the planet. 🌍"
    elif total < 120:
        return "⚠️ Moderate Impact", "You're on a good path. A few lifestyle tweaks can lower it more!"
    else:
        return "🔥 High Impact", "High emissions — time to shift toward more eco-conscious choices."

# --- Button Action ---
if st.button("Calculate My Carbon Footprint"):
    travel, electricity, food, total = calculate_emissions(car_km, bus_km, flight_km, kwh, diet)
    impact_level, message = classify_impact(total)
    suggestions = get_suggestions(car_km, bus_km, flight_km, kwh, diet)

    st.subheader("📊 Emission Breakdown:")
    st.write(f"🚗 Travel Emissions: **{travel} kg CO₂/week**")
    st.write(f"⚡ Electricity Emissions: **{electricity} kg CO₂/week**")
    st.write(f"🍽️ Food Emissions: **{food} kg CO₂/week**")
    st.success(f"🌟 Total Weekly Carbon Footprint: **{total} kg CO₂**")

    st.markdown("---")
    st.subheader("📉 Environmental Impact")
    st.markdown(f"**{impact_level}** — {message}")

    st.markdown("### 💡 Smart Suggestions")
    for tip in suggestions:
        st.markdown(f"- {tip}")
