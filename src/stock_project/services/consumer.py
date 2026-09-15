# src/stock_project/services/consumer.py

import time

from .redis_client import get_redis_client


STREAM_NAME = "stock_data"
GROUP_NAME = "prediction_group"
CONSUMER_NAME = "prediction_worker"


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
            print(f"Consumer group already exists: {GROUP_NAME}")
        else:
            raise


def consume_stock_data():

    redis_client = get_redis_client()

    create_consumer_group(redis_client)

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

                print("\nReceived message:")
                print(f"Message ID: {message_id}")
                print(f"Data: {data}")

                # Acknowledge message
                redis_client.xack(
                    STREAM_NAME,
                    GROUP_NAME,
                    message_id
                )

                print("Message acknowledged.")


if __name__ == "__main__":
    consume_stock_data()