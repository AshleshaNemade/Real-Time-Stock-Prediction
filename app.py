from fastapi import FastAPI
import pandas as pd

from src.stock_project.pipeline.prediction_pipeline import (
    PredictionPipeline
)

from src.stock_project.services.producer import (
    get_latest_stock_data,
    publish_stock_data,
)

from src.stock_project.services.redis_client import (
    get_redis_client,
)


app = FastAPI()


# Load prediction pipeline
pipeline = PredictionPipeline()


# Redis configuration
STREAM_NAME = "stock_data"
GROUP_NAME = "prediction_group"
CONSUMER_NAME = "api_consumer"


# Features expected by the trained model
FEATURE_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Volume",
    "SMA_10",
    "SMA_20",
    "RSI",
    "MACD",
    "Daily_Return",
    "Volatility",
]


class StockData(pd.DataFrame):
    pass


@app.get("/")
def home():
    return {
        "message": "Stock Prediction API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/produce")
def produce():

    redis_client = get_redis_client()

    stock_data = get_latest_stock_data("AAPL")

    message_id = redis_client.xadd(
        STREAM_NAME,
        stock_data
    )

    return {
        "status": "success",
        "message_id": message_id,
        "data": stock_data
    }


@app.post("/consume")
def consume():

    redis_client = get_redis_client()

    # Create consumer group if it doesn't exist
    try:
        redis_client.xgroup_create(
            name=STREAM_NAME,
            groupname=GROUP_NAME,
            id="0",
            mkstream=True
        )

    except Exception as e:

        if "BUSYGROUP" not in str(e):
            raise

    # Read one new message
    messages = redis_client.xreadgroup(
        groupname=GROUP_NAME,
        consumername=CONSUMER_NAME,
        streams={
            STREAM_NAME: ">"
        },
        count=1,
        block=1000
    )

    if not messages:

        return {
            "status": "no_data",
            "message": "No new stock data available"
        }

    for stream, entries in messages:

        for message_id, data in entries:

            # Prepare model input
            input_data = pd.DataFrame([{
                column: float(data[column])
                for column in FEATURE_COLUMNS
            }])

            # Run prediction
            prediction = pipeline.predict(
                input_data
            )

            predicted_price = float(
                prediction[0]
            )

            # Acknowledge message
            redis_client.xack(
                STREAM_NAME,
                GROUP_NAME,
                message_id
            )

            return {
                "status": "success",
                "message_id": message_id,
                "symbol": data.get("symbol"),
                "predicted_close_price": round(
                    predicted_price,
                    2
                )
            }