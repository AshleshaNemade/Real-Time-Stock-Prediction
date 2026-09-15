# src/stock_project/services/producer.py

import time
from datetime import datetime

from .redis_client import get_redis_client


STREAM_NAME = "stock_data"


def publish_stock_data():
    redis_client = get_redis_client()

    stock_data = {
        "symbol": "AAPL",
        "Open": "220.50",
        "High": "225.20",
        "Low": "218.70",
        "Volume": "1500000",
        "timestamp": datetime.utcnow().isoformat()
    }

    message_id = redis_client.xadd(
        STREAM_NAME,
        stock_data
    )

    print(f"Published message: {message_id}")
    print(stock_data)


if __name__ == "__main__":
    publish_stock_data()