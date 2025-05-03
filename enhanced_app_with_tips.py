
import streamlit as st

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌱")
st.title("🌍 Carbon Footprint Calculator + Impact & Tips")

st.markdown("""
Estimate your **weekly carbon footprint** and get **personalized insights** 🌱

We consider:
- 🚗 Travel habits
- ⚡ Electricity usage
- 🍽️ Diet type

Find out what your lifestyle means for the planet and how you can improve! 🌎
""")

# User inputs
car_km = st.number_input("🚗 Car travel in km per week", min_value=0.0, step=1.0)
bus_km = st.number_input("🚌 Bus/Metro travel in km per week", min_value=0.0, step=1.0)
flight_km = st.number_input("✈️ Flight travel in km per week", min_value=0.0, step=1.0)
kwh = st.number_input("⚡ Electricity usage per week (kWh)", min_value=0.0, step=1.0)
diet = st.selectbox("🍽️ Your diet type", ["Meat", "Vegetarian", "Mixed"])

# Calculation logic
def calculate_emissions(car_km, bus_km, flight_km, kwh, diet):
    travel_emissions = car_km * 0.192 + bus_km * 0.105 + flight_km * 0.255
    energy_emissions = kwh * 0.7
    if diet == 'Meat':
        food_emissions = 7 * 27
    elif diet == 'Vegetarian':
        food_emissions = 7 * 2
    else:
        food_emissions = 7 * 4
    total = travel_emissions + energy_emissions + food_emissions
    return travel_emissions, energy_emissions, food_emissions, total

# Impact explanation logic with tips
def get_impact_feedback(total_emissions):
    if total_emissions < 50:
        return (
            "🌟 **Low impact** – You're ahead of the curve!",
            "💡 Tips:
- Inspire others to reduce their emissions.
- Offset remaining emissions via credible carbon offset programs.
- Continue biking, walking, or using public transit!"
        )
    elif 50 <= total_emissions <= 100:
        return (
            "⚠️ **Moderate impact** – You're doing fairly well, but there’s room to improve.",
            "💡 Tips:
- Try switching to LED lights and unplugging devices.
- Explore meat-free meals a few days a week.
- Choose direct flights or train travel when possible."
        )
    else:
        return (
            "🚨 **High impact** – Your lifestyle has a significant environmental cost.",
            "💡 Tips:
- Limit flying or use trains for domestic travel.
- Use energy-efficient appliances and switch to renewable energy plans.
- Reduce meat and dairy consumption."
        )

# Show results
if st.button("Calculate My Carbon Footprint"):
    travel, energy, food, total = calculate_emissions(car_km, bus_km, flight_km, kwh, diet)
    st.subheader("📊 Results")
    st.write(f"🚗 Travel Emissions: **{travel:.2f} kg CO₂**")
    st.write(f"⚡ Energy Emissions: **{energy:.2f} kg CO₂**")
    st.write(f"🥗 Food Emissions: **{food:.2f} kg CO₂**")
    st.success(f"🌟 Your Total Weekly Carbon Footprint: **{total:.2f} kg CO₂**")

    st.markdown("---")
    st.subheader("📉 Environmental Impact")
    title, tips = get_impact_feedback(total)
    st.markdown(f"{title}")
    st.markdown(tips)
