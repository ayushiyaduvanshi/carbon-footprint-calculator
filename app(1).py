import streamlit as st
import openai
import os

# --- Set API Key ---
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Carbon Footprint App", page_icon="🌱")
st.title("🌍 Smart Carbon Footprint Calculator (GPT-Powered)")

st.markdown("""
Estimate your **weekly carbon footprint** based on your lifestyle, and receive **AI-generated suggestions** using ChatGPT 🌿
""")

# --- Inputs ---
car_km = st.number_input("🚗 Car travel (km/week)", 0.0)
bus_km = st.number_input("🚌 Bus/Metro travel (km/week)", 0.0)
flight_km = st.number_input("✈️ Flight travel (km/week)", 0.0)
kwh = st.number_input("⚡ Electricity usage (kWh/week)", 0.0)
diet = st.selectbox("🍽️ Diet Type", ["Meat", "Vegetarian", "Mixed"])

# --- Emission Calculation ---
def calculate_emissions(car, bus, flight, energy, diet_type):
    travel = car * 0.192 + bus * 0.105 + flight * 0.255
    electricity = energy * 0.7
    if diet_type == 'Meat':
        food = 7 * 27
    elif diet_type == 'Vegetarian':
        food = 7 * 2
    else:
        food = 7 * 4
    return round(travel, 2), round(electricity, 2), round(food, 2), round(travel + electricity + food, 2)

# --- Impact Classification ---
def classify_impact(total):
    if total < 50:
        return "🌱 Low Impact", "Minimal environmental footprint. Excellent lifestyle!"
    elif total < 120:
        return "⚠️ Moderate Impact", "You're doing fairly well, but there’s room to improve."
    else:
        return "🔥 High Impact", "High emissions — time to consider more sustainable changes."

# --- Generate GPT Tip Prompt ---
def generate_tip_prompt(travel, electricity, food, diet, car, bus, flight):
    return f"""
You are an environmental sustainability expert. A user just received their weekly carbon footprint breakdown:

- Travel: {travel} kg CO2
  - Car: {car} km/week
  - Bus: {bus} km/week
  - Flight: {flight} km/week
- Electricity: {electricity} kg CO2
- Diet: {diet} (Food emissions: {food} kg CO2)

Based on this exact data, provide 4 specific, personalized tips they can apply. 
Avoid suggesting changes the user already follows. Be motivating and practical.
"""

# --- Run everything ---
if st.button("Calculate and Get AI Suggestions"):
    travel, electricity, food, total = calculate_emissions(car_km, bus_km, flight_km, kwh, diet)
    level, msg = classify_impact(total)

    st.subheader("📊 Emission Breakdown")
    st.write(f"- 🚗 Travel: **{travel} kg CO₂/week**")
    st.write(f"- ⚡ Electricity: **{electricity} kg CO₂/week**")
    st.write(f"- 🥗 Food: **{food} kg CO₂/week**")
    st.success(f"🌟 Total Carbon Footprint: **{total} kg CO₂/week**")

    st.markdown("---")
    st.subheader("📉 Environmental Impact")
    st.markdown(f"**{level}** — {msg}")

    st.markdown("### 💡 ChatGPT Suggestions")

    with st.spinner("Asking GPT for tips..."):
        prompt = generate_tip_prompt(travel, electricity, food, diet, car_km, bus_km, flight_km)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=300
            )
            gpt_reply = response.choices[0].message["content"]
            st.markdown(gpt_reply)
        except Exception as e:
            st.error(f"Failed to generate tips: {e}")
