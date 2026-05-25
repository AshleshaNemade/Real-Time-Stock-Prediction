from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.stock_project.pipeline.prediction_pipeline import (
    PredictionPipeline
)

app = FastAPI()

# Load prediction pipeline
pipeline = PredictionPipeline()


# ================================
# Request Schema
# ================================

class StockData(BaseModel):

    Open: float
    High: float
    Low: float
    Volume: float
    SMA_10: float
    SMA_20: float
    RSI: float
    MACD: float
    Daily_Return: float
    Volatility: float


# ================================
# Home Route
# ================================

@app.get("/")

def home():

    return {
        "message": "Stock Prediction API Running"
    }


# ================================
# Prediction Route
# ================================

@app.post("/predict")

def predict(data: StockData):

    input_data = pd.DataFrame([{

        "High": data.High,
        "Low": data.Low,
        "Open": data.Open,
        "Volume": data.Volume,
        "SMA_10": data.SMA_10,
        "SMA_20": data.SMA_20,
        "RSI": data.RSI,
        "MACD": data.MACD,
        "Daily_Return": data.Daily_Return,
        "Volatility": data.Volatility
    }])

    prediction = pipeline.predict(input_data)

    return {
        "Predicted_Close_Price":
        round(float(prediction[0]), 2)
    }