# src/stock_project/services/redis_client.py

import os
import redis


def get_redis_client():
    redis_url = os.getenv("REDIS_URL")

    if not redis_url:
        raise ValueError("REDIS_URL environment variable is not set")

    return redis.from_url(
        redis_url,
        decode_responses=True
    )
    
        # Verify connection
    client.ping()

    return client