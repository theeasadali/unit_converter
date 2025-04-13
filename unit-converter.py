import streamlit as st

def units_convert(value, unit_from, unit_to):
    conversions = {
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key similar to dictionary based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function, call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Or, multiply by the conversion value
    else:
        return "Conversion not supported"  # Return message if conversion is not defined

st.title("Simple Unit Converter by Asad Ali")

# User input
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
from_unit = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
)

# Dropdown to select unit to convert to
to_unit = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = units_convert(value, from_unit, to_unit)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Shows result
