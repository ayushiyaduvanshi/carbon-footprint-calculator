import streamlit as st

st.set_page_config(page_title="AI Carbon Footprint Calculator", page_icon="🌱")
st.title("🌍 Smart Carbon Footprint Calculator with AI-Generated Tips")

st.markdown("""
Estimate your **weekly carbon footprint** based on how you live and get **intelligent, behavior-based suggestions** 🌿
""")

# --- INPUTS ---
car_km = st.number_input("🚗 Car travel in km/week", min_value=0.0)
bus_km = st.number_input("🚌 Bus/Metro travel in km/week", min_value=0.0)
flight_km = st.number_input("✈️ Flight travel in km/week", min_value=0.0)
kwh = st.number_input("⚡ Electricity usage per week (kWh)", min_value=0.0)
diet = st.selectbox("🍽️ Diet Type", ["Meat", "Vegetarian", "Mixed"])

# --- CALCULATIONS ---
def calc_emissions(car, bus, flight, energy, diet_type):
    travel = car * 0.192 + bus * 0.105 + flight * 0.255
    electricity = energy * 0.7
    if diet_type == 'Meat':
        food = 7 * 27
    elif diet_type == 'Vegetarian':
        food = 7 * 2
    else:
        food = 7 * 4
    total = travel + electricity + food
    return round(travel, 2), round(electricity, 2), round(food, 2), round(total, 2)

# --- AI-LIKE TIP GENERATOR ---
def generate_ai_tips(car, bus, flight, energy, diet_type):
    tips = []

    # Analyze travel
    if car > 100:
        tips.append("🚘 You drive a lot — switching to carpool or using public transport can reduce emissions.")
    elif car > 0:
        tips.append("🚙 Moderate car usage — consider combining errands to reduce trips.")
    else:
        tips.append("🛴 Great! No car usage detected.")

    if bus > 100:
        tips.append("🚌 Heavy public transport use — it's low emission, but biking/walking can help further.")
    elif bus > 0:
        tips.append("🚶‍♂️ You use public transport — a great step already!")
    else:
        tips.append("🚫 No public transport — try using it once or twice a week.")

    if flight > 200:
        tips.append("✈️ High flight activity — consider virtual alternatives or slower travel.")
    elif flight > 0:
        tips.append("🌍 Occasional flights — consider direct flights or greener airlines.")
    else:
        tips.append("🛑 No flights — that's excellent for the planet!")

    # Analyze energy
    if energy > 100:
        tips.append("🔌 High electricity use — try turning off devices, efficient cooling, or LED lighting.")
    elif energy > 50:
        tips.append("💡 Moderate energy usage — consider unplugging unused electronics.")
    else:
        tips.append("🌞 Low electricity footprint — keep it going!")

    # Analyze food
    if diet_type == "Meat":
        tips.append("🥩 A meat-heavy diet causes high emissions — try vegetarian days 2–3 times a week.")
    elif diet_type == "Mixed":
        tips.append("🥗 Balanced diet — reducing red meat can further cut your footprint.")
    else:
        tips.append("🌿 Your vegetarian diet is already helping the planet!")

    return tips

# --- IMPACT CATEGORIES ---
def get_impact_status(total):
    if total < 50:
        return "🌱 Low Impact", "Your lifestyle has minimal environmental impact. Amazing!"
    elif total < 120:
        return "⚠️ Moderate Impact", "You're doing fairly well. A few tweaks could make it even better."
    else:
        return "🔥 High Impact", "Your lifestyle generates significant emissions. Let’s explore how to reduce it."

# --- OUTPUT ---
if st.button("Calculate My Carbon Footprint"):
    travel, electricity, food, total = calc_emissions(car_km, bus_km, flight_km, kwh, diet)

    st.subheader("📊 Emission Breakdown:")
    st.write(f"- 🚗 Travel: **{travel} kg CO₂/week**")
    st.write(f"- ⚡ Electricity: **{electricity} kg CO₂/week**")
    st.write(f"- 🥗 Food: **{food} kg CO₂/week**")
    st.success(f"🌟 Total Carbon Footprint: **{total} kg CO₂/week**")

    st.markdown("---")
    level, message = get_impact_status(total)
    st.subheader("📉 Impact Level:")
    st.markdown(f"**{level}** — {message}")

    st.markdown("### 🤖 AI-Generated Tips Based on Your Behavior")
    tips = generate_ai_tips(car_km, bus_km, flight_km, kwh, diet)
    for t in tips:
        st.markdown(f"- {t}")
