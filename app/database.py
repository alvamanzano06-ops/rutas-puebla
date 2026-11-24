import os
import redis
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)


def probar_conexion():
    try:
        return redis_client.ping()
    except Exception:
        return False