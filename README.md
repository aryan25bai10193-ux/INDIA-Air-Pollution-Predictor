# Bhopal AQI Predictor
This project predicts the **Air Quality Index (AQI)** for Bhopal using Machine Learning.  
It uses historical pollution data and temporal features to forecast AQI values.

# Project Overview
Air pollution is a major environmental issue. This project builds a predictive model to estimate 
AQI based on pollutant concentrations like PM2.5, PM10, NO₂, CO, etc.
A **Random Forest Regressor** is used along with feature engineering (lag features + time-based features)
to improve prediction accuracy.

# Features
- Data preprocessing and cleaning  
- Temporal features (day, month, weekend)  
- Lag features (previous AQI values)  
- Machine Learning model (Random Forest)  
- Interactive UI using Streamlit  
- Real-time AQI prediction  
- AQI category classification (Good, Moderate, etc.)

# Model Details
- Model: Random Forest Regressor  
- Features Used:
  - PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3  
  - Day of week, Month, Weekend  
  - AQI lag (1, 2, 3, 7 days)

# Model Performance
- MAE (Mean Absolute Error): 8.59  
- R² Score: 0.74  

## 📁 Project Structure
