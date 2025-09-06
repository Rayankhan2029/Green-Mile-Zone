import streamlit as st

# ---------- App setup ----------
st.set_page_config(page_title="Green Mile Zone", page_icon="🌿")
st.title("🌿 Green Mile Zone – Simple Eco Travel Calculator")

# Emission factors (kg CO₂e per km)
EF = {
    "car": 0.18,
    "bus": 0.09,
    "train": 0.04,
    "walk": 0.0,
    "bike": 0.0,
}

# Nice labels for the dropdown, but map back to EF keys safely

OPTIONS = ["Car", "Bus", "Train", "Walk", "Bike"]

mode_label = st.selectbox("Choose your travel mode:", OPTIONS, index=0)
mode_key = mode_label.lower()  # "Car" -> "car"

distance = st.number_input(
    "Enter distance (km):",
    min_value=0.0,
    value=5.0,
    step=0.5,
    format="%.2f",
)

if st.button("Calculate CO₂"):
    # Defensive guard in case someone edits OPTIONS/EF later
    if mode_key not in EF:
        st.error("Unknown travel mode. Please pick from the list.")
    else:
        ef = EF[mode_key]
        emission = distance * ef
        st.success(f"Your trip produces **{emission:.2f} kg CO₂e** using **{mode_label}**.")

        # Show alternatives only if they actually save emissions
        for alt_label in ["Bus", "Train"]:
            alt_key = alt_label.lower()
            alt_emission = distance * EF[alt_key]
            saving = emission - alt_emission
            if saving > 0.00001:  # only show if better than current
                st.info(
                    f"If you used **{alt_label}**: **{alt_emission:.2f} kg** "
                    f"(save **{saving:.2f} kg CO₂e**)"
                )

st.caption("Tip: Emission factors are approximate examples. Adjust to your data if needed.")
