import streamlit as st

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌱")
st.title("🌍 Carbon Footprint Calculator + Smart Tips")

st.markdown("""
This tool helps you estimate your **weekly carbon footprint** and gives you **smart, personalized tips** 🌱  
We calculate emissions from:
- 🚗 Travel (car, bus, flight)
- ⚡ Electricity
- 🥗 Diet
""")

# --- INPUT SECTION ---
car_km = st.number_input("🚗 Car travel in km per week", min_value=0.0, step=1.0)
bus_km = st.number_input("🚌 Bus/Metro travel in km per week", min_value=0.0, step=1.0)
flight_km = st.number_input("✈️ Flight travel in km per week", min_value=0.0, step=1.0)
kwh = st.number_input("⚡ Electricity usage in kWh per week", min_value=0.0, step=1.0)
diet = st.selectbox("🍽️ Your diet type", ["Meat", "Vegetarian", "Mixed"])

# --- CALCULATION LOGIC ---
def calculate_emissions(car, bus, flight, energy_kwh, diet_type):
    travel = car * 0.192 + bus * 0.105 + flight * 0.255
    energy = energy_kwh * 0.7
    if diet_type == 'Meat':
        food = 7 * 27
    elif diet_type == 'Vegetarian':
        food = 7 * 2
    else:  # Mixed
        food = 7 * 4
    return travel, energy, food, travel + energy + food

# --- SMART TIPS GENERATOR ---
def generate_tips(car, bus, flight, energy, diet_type):
    tips = []
    if car > 100:
        tips.append("🚘 Consider reducing car usage by carpooling or using public transport.")
    if bus + metro := bus > 50:
        tips.append("🚌 Great job using public transport. Try walking or cycling for nearby trips.")
    if flight > 100:
        tips.append("✈️ Flights contribute heavily. Try trains or virtual meetings if possible.")
    if energy > 50:
        tips.append("🔌 Reduce energy usage by turning off devices and switching to LED lighting.")
    if diet_type == 'Meat':
        tips.append("🥩 Try having 1–2 meat-free days per week to lower your footprint.")
    elif diet_type == 'Vegetarian':
        tips.append("🌾 Your plant-based diet is great for the planet — keep it up!")
    else:
        tips.append("🥗 Mixed diets are better than meat-heavy ones. Going vegetarian a few days helps!")

    return tips if tips else ["🎉 Your lifestyle already reflects low emissions. Keep inspiring others!"]

# --- IMPACT LEVEL ---
def get_impact_level(total):
    if total < 50:
        return "🌱 Low Impact", "You’re living sustainably. Awesome job!"
    elif total < 120:
        return "⚠️ Moderate Impact", "Good effort — but there’s room to improve!"
    else:
        return "🔥 High Impact", "High footprint — time to make eco-friendlier choices!"

# --- BUTTON & RESULTS ---
if st.button("Calculate My Carbon Footprint"):
    travel, energy, food, total = calculate_emissions(car_km, bus_km, flight_km, kwh, diet)

    st.subheader("📊 Results")
    st.write(f"🚗 Travel Emissions: **{travel:.2f} kg CO₂**")
    st.write(f"⚡ Energy Emissions: **{energy:.2f} kg CO₂**")
    st.write(f"🥗 Food Emissions: **{food:.2f} kg CO₂**")
    st.success(f"🌟 Total Weekly Carbon Footprint: **{total:.2f} kg CO₂**")

    st.markdown("---")
    st.subheader("📉 Impact Summary")
    impact, message = get_impact_level(total)
    st.markdown(f"**{impact}** — {message}")

    st.markdown("### 💡 Smart Tips to Improve")
    for tip in generate_tips(car_km, bus_km, flight_km, kwh, diet):
        st.markdown(f"- {tip}")
