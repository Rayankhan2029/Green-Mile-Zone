# 🌿 Green Mile Zone – Eco Travel Calculator
Green Mile Zone is a Streamlit application that shows consumers how the carbon footprint of their travel changes. By inputting the **mode** and **distance** of travel, users can immediately view CO₂ emissions and compare greener options such as train or bus.

## 🔍 Research Background
Transportation is one of the largest sources of CO₂ emissions globally. To keep our tool realistic, we used **average emission factors (kg CO₂ per km)** from public climate data (IPCC / government transport research):
- 🚗 Car → **0.18 kg CO₂/km**
- 🚌 Bus → **0.09 kg CO₂/km**
- 🚆 Train → **0.04 kg CO₂/km**
- 🚶 Walk → **0.00 kg CO₂/km**
- 🚴 Bike → **0.00 kg CO₂/km**
> These values are simplified for demo purposes. In the real world, they depend on vehicle type, fuel, and efficiency. Our aim is to make carbon-aware commuting accessible at a click.

## ✨ Features
- Select travel mode from dropdown (car, bus, train, walk, bike)
- Input distance in km
- Instant CO₂ calculation
- Tips for greener alternatives (bus/train savings)
- Easy, quick, and hackathon-friendly Streamlit interface

