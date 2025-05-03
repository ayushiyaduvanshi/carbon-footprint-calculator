#!/usr/bin/env python
# coding: utf-8

# In[8]:


# carbon_calculator.py

def calculate_travel_emissions(kms_car, kms_bus, flight_kms):
    car_factor = 0.192
    bus_factor = 0.105
    flight_factor = 0.255
    return kms_car * car_factor + kms_bus * bus_factor + flight_kms * flight_factor

def calculate_energy_emissions(kwh):
    energy_factor = 0.7
    return kwh * energy_factor

def calculate_food_emissions(diet_type):
    if diet_type.lower() == 'meat':
        return 7 * 27  # avg 1 kg/week
    elif diet_type.lower() == 'vegetarian':
        return 7 * 2
    else:
        return 7 * 4  # mixed

def total_emissions(travel, energy, food):
    return travel + energy + food

if __name__ == "__main__":
    car_km = float(input("Enter car travel in km: "))
    bus_km = float(input("Enter bus/metro travel in km: "))
    flight_km = float(input("Enter flight travel in km: "))
    kwh = float(input("Enter electricity usage in kWh: "))
    diet = input("Enter diet type (meat/vegetarian/mixed): ")

    travel = calculate_travel_emissions(car_km, bus_km, flight_km)
    energy = calculate_energy_emissions(kwh)
    food = calculate_food_emissions(diet)

    total = total_emissions(travel, energy, food)

    print(f"\nYour weekly carbon footprint is approximately: {total:.2f} kg CO₂")


# In[ ]:




