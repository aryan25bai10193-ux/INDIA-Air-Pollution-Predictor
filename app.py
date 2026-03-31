import streamlit as st
import joblib
from datetime import datetime

# Load model
model = joblib.load('models/model.pkl')

st.title("🌬️ Bhopal AQI Predictor")
st.write("Enter pollution values:")

# -------------------------
# SESSION STATE (default values)
# -------------------------
default_values = {
    "pm25": 0.0, "pm10": 0.0, "no": 0.0, "no2": 0.0, "nox": 0.0,
    "nh3": 0.0, "co": 0.0, "so2": 0.0, "o3": 0.0,
    "aqi_lag1": 0.0, "aqi_lag2": 0.0, "aqi_lag3": 0.0, "aqi_lag7": 0.0
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------------
# SAMPLE DATA BUTTON
# -------------------------
if st.button("Use Sample Data"):
    st.session_state.pm25 = 60
    st.session_state.pm10 = 100
    st.session_state.no = 20
    st.session_state.no2 = 30
    st.session_state.nox = 40
    st.session_state.nh3 = 10
    st.session_state.co = 1
    st.session_state.so2 = 15
    st.session_state.o3 = 25
    st.session_state.aqi_lag1 = 90
    st.session_state.aqi_lag2 = 85
    st.session_state.aqi_lag3 = 88
    st.session_state.aqi_lag7 = 95

# -------------------------
# INPUT FIELDS
# -------------------------
pm25 = st.number_input("PM2.5", key="pm25")
pm10 = st.number_input("PM10", key="pm10")
no = st.number_input("NO", key="no")
no2 = st.number_input("NO2", key="no2")
nox = st.number_input("NOx", key="nox")
nh3 = st.number_input("NH3", key="nh3")
co = st.number_input("CO", key="co")
so2 = st.number_input("SO2", key="so2")
o3 = st.number_input("O3", key="o3")

aqi_lag1 = st.number_input("AQI lag 1 day", key="aqi_lag1")
aqi_lag2 = st.number_input("AQI lag 2 day", key="aqi_lag2")
aqi_lag3 = st.number_input("AQI lag 3 day", key="aqi_lag3")
aqi_lag7 = st.number_input("AQI lag 7 day", key="aqi_lag7")

# -------------------------
# PREDICTION
# -------------------------
if st.button("Predict AQI"):

    now = datetime.now()
    day_of_week = now.weekday()
    month = now.month
    is_weekend = 1 if day_of_week >= 5 else 0

    features = [[
        pm25, pm10, no, no2, nox, nh3, co, so2, o3,
        day_of_week, month, is_weekend,
        aqi_lag1, aqi_lag2, aqi_lag3, aqi_lag7
    ]]

    pred = model.predict(features)[0]

    # -------------------------
    # AQI CATEGORY + COLOR TEXT
    # -------------------------
    if pred <= 50:
        cat = "Good"
        color = "green"
    elif pred <= 100:
        cat = "Satisfactory"
        color = "blue"
    elif pred <= 200:
        cat = "Moderate"
        color = "orange"
    elif pred <= 300:
        cat = "Poor"
        color = "red"
    else:
        cat = "Severe"
        color = "darkred"

    st.markdown(
        f"<h3 style='color:{color}'>AQI: {pred:.2f} ({cat})</h3>",
        unsafe_allow_html=True
    )

    # -------------------------
    # AQI METER (PROGRESS BAR)
    # -------------------------
    progress_value = min(int(pred) / 500, 1.0)
    st.progress(progress_value)

    # -------------------------
    # STATUS MESSAGE
    # -------------------------
    if pred <= 50:
        st.success("Good Air Quality 😊")
    elif pred <= 100:
        st.info("Satisfactory 👍")
    elif pred <= 200:
        st.warning("Moderate 😐")
    else:
        st.error("Poor/Severe ⚠️")

    st.caption("AQI Scale: 0 (Good) → 500 (Severe)")