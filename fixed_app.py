
import streamlit as st

st.title("🌱 Carbon Footprint Calculator")

st.markdown("""
This app estimates your **weekly carbon footprint** based on:
- Travel (Car, Bus, Flights)
- Electricity usage
- Dietary habits
""")

# User inputs
car_km = st.number_input("Car travel in km per week", min_value=0.0, step=1.0)
bus_km = st.number_input("Bus/Metro travel in km per week", min_value=0.0, step=1.0)
flight_km = st.number_input("Flight travel in km per week", min_value=0.0, step=1.0)
kwh = st.number_input("Electricity usage per week (kWh)", min_value=0.0, step=1.0)
diet = st.selectbox("Your diet type", ["Meat", "Vegetarian", "Mixed"])

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

# Show results
if st.button("Calculate My Carbon Footprint"):
    travel, energy, food, total = calculate_emissions(car_km, bus_km, flight_km, kwh, diet)
    st.subheader("🌍 Results:")
    st.write(f"🚗 Travel Emissions: {travel:.2f} kg CO₂")
    st.write(f"⚡ Energy Emissions: {energy:.2f} kg CO₂")
    st.write(f"🥗 Food Emissions: {food:.2f} kg CO₂")
    st.success(f"🌟 Your Total Weekly Carbon Footprint: {total:.2f} kg CO₂")
