#imports
import streamlit as st
import pandas as pd
import numpy as np
import joblib

#loading saved files
filepath = r"C:\Users\julia\downloads\IDX_summer_internship"

model = joblib.load(filepath + r"\xgb_model.pkl")
feature_names = joblib.load(filepath + r"\feature_names.pkl")
feature_medians = joblib.load(filepath + r"\feature_medians.pkl")

# city to approximate scaled lat/lon
city_coords = {
    "Los Angeles":   {"lat": -0.76,  "lon": -0.45},
    "San Diego":     {"lat": -1.62,  "lon":  0.18},
    "San Francisco": {"lat":  1.22,  "lon": -1.93},
    "San Jose":      {"lat":  0.89,  "lon": -1.59},
    "Sacramento":    {"lat":  1.53,  "lon": -0.86},
    "Fresno":        {"lat":  0.24,  "lon":  0.33},
    "Long Beach":    {"lat": -0.61,  "lon": -0.38},
    "Oakland":       {"lat":  1.27,  "lon": -1.84},
    "Riverside":     {"lat": -0.52,  "lon":  0.09},
    "Irvine":        {"lat": -0.69,  "lon": -0.29},
}

# app layout
st.title("🏡 California Home Price Predictor")
st.write("Estimate the sale price of a California single-family home.")
st.divider()

st.subheader("Property Details")

# two column layout
col1, col2 = st.columns(2)

with col1:
    living_area = st.number_input("Living Area (sq ft)",
                                   min_value=200, max_value=15000,
                                   value=1800, step=100)
    bedrooms = st.number_input("Bedrooms",
                                min_value=1, max_value=10,
                                value=3, step=1)

with col2:
    bathrooms = st.number_input("Bathrooms",
                                 min_value=1, max_value=10,
                                 value=2, step=1)
    lot_size = st.number_input("Lot Size (sq ft)",
                                min_value=500, max_value=100000,
                                value=6000, step=500)

# city is the only extra input since lat/lon are important features
city = st.selectbox("City (used for location)", list(city_coords.keys()))

st.divider()

# predict button
if st.button("Predict Home Value", type="primary"):

    # start with medians for all features
    input_data = pd.DataFrame(
        feature_medians.values.reshape(1, -1),
        columns=feature_names
    )

    # override required inputs (scaled approximations)
    if "LivingArea" in input_data.columns:
        input_data["LivingArea"] = (living_area - 1800) / 800
    if "BedroomsTotal" in input_data.columns:
        input_data["BedroomsTotal"] = (bedrooms - 3.5) / 1.0
    if "BathroomsTotalInteger" in input_data.columns:
        input_data["BathroomsTotalInteger"] = (bathrooms - 2.3) / 1.0
    if "LotSizeSquareFeet" in input_data.columns:
        input_data["LotSizeSquareFeet"] = (lot_size - 8000) / 12000
    if "LotSizeArea" in input_data.columns:
        input_data["LotSizeArea"] = (lot_size - 8000) / 12000

    # engineered features from user inputs
    if "BedBathRatio" in input_data.columns:
        input_data["BedBathRatio"] = bedrooms / (bathrooms + 1e-9)
    if "AreaPerBedroom" in input_data.columns:
        input_data["AreaPerBedroom"] = living_area / (bedrooms + 1e-9)

    # predict
    prediction = model.predict(input_data)[0]

    # display
    st.success(f"### Estimated Home Value: ${prediction:,.0f}")

    st.write(f"""
    **Property Summary:**
    - Location: {city}
    - Living Area: {living_area:,} sq ft
    - Bedrooms: {bedrooms} | Bathrooms: {bathrooms}
    - Lot Size: {lot_size:,} sq ft
    - All other features set to dataset medians
    """)

    st.info(f"""
    **Model Performance:** MdAPE of 7.66% on June 2026 test data.
    Typical prediction range: **${prediction * 0.9234:,.0f} – ${prediction * 1.0766:,.0f}**
    """)

st.divider()
st.caption("Built using XGBoost trained on 400,000+ CRMLS California MLS records | IDX Exchange Data Science Internship 2026")