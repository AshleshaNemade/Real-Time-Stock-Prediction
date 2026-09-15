import pandas as pd

from .redis_client import get_redis_client
from ..pipeline.prediction_pipeline import PredictionPipeline


STREAM_NAME = "stock_data"
GROUP_NAME = "prediction_group"
CONSUMER_NAME = "prediction_worker"


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


def create_consumer_group(redis_client):

    try:
        redis_client.xgroup_create(
            name=STREAM_NAME,
            groupname=GROUP_NAME,
            id="0",
            mkstream=True
        )

        print(f"Created consumer group: {GROUP_NAME}")

    except Exception as e:

        if "BUSYGROUP" in str(e):
            print("Consumer group already exists")

        else:
            raise


def consume_stock_data():

    redis_client = get_redis_client()

    # Load model once
    pipeline = PredictionPipeline()

    create_consumer_group(redis_client)

    print("Prediction worker started...")
    print("Waiting for stock data...")

    while True:

        messages = redis_client.xreadgroup(
            groupname=GROUP_NAME,
            consumername=CONSUMER_NAME,
            streams={STREAM_NAME: ">"},
            count=1,
            block=5000
        )

        if not messages:
            continue

        for stream, entries in messages:

            for message_id, data in entries:

                try:

                    print("\nReceived stock data:")
                    print(f"Message ID: {message_id}")
                    print(data)

                    # Create dataframe using model features
                    input_data = pd.DataFrame([{
                        column: float(data[column])
                        for column in FEATURE_COLUMNS
                    }])

                    # Run prediction
                    prediction = pipeline.predict(input_data)

                    predicted_price = float(prediction[0])

                    print(
                        f"Predicted Close Price: "
                        f"{predicted_price:.2f}"
                    )

                    # Acknowledge successful processing
                    redis_client.xack(
                        STREAM_NAME,
                        GROUP_NAME,
                        message_id
                    )

                    print("Message acknowledged")

                except Exception as e:

                    print(
                        f"Error processing message "
                        f"{message_id}: {e}"
                    )


if __name__ == "__main__":
    consume_stock_data()