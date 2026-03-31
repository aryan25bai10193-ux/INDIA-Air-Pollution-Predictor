#  Bhopal AQI Predictor
This project predicts the **Air Quality Index (AQI)** for Bhopal using Machine Learning.
It uses historical pollution data and temporal features to forecast AQI values.

##  Project Overview
Air pollution is a major environmental issue. This project builds a predictive model to estimate AQI based on pollutant concentrations like PM2.5, PM10, NO₂, CO, etc.
A **Random Forest Regressor** is used along with feature engineering (lag features + time-based features) to improve prediction accuracy.

##  Features

- Data preprocessing and cleaning
- Temporal features (day, month, weekend)
- Lag features (previous AQI values)
- Machine Learning model (Random Forest)
- Interactive UI using Streamlit
- Real-time AQI prediction
- AQI category classification (Good, Moderate, etc.)

##  Model Details
**Model:** Random Forest Regressor

##  Features Used:-
- PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3
- Day of week, Month, Weekend
- AQI lag (1, 2, 3, 7 days)

##  Model Performance
- **MAE:** 8.59
- **R² Score:** 0.74

## 📁 Project Structure

```
bhopal-air-pollution-predictor/
├── data/
├── models/
│   └── model.pkl
├── notebooks/
├── src/
├── app.py
├── requirements.txt
└── README.md
```

##  How to Run the Project
1. Clone the repository
```
git clone <your-repo-link>
cd bhopal-air-pollution-predictor
```
2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the app
```
streamlit run app.py
```

4. Open in browser
```
http://localhost:8501
```

##  How to Use
1. Enter pollution values
2. OR click **Use Sample Data**
3. Click **Predict AQI**
4. View AQI value, category, and visual indicator



Aryan
Machine Learning Project – AQI Prediction
