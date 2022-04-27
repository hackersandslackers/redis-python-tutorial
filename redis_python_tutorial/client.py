"""Create Redis client."""
import redis

from config import REDIS_DB, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

r = redis.StrictRedis(
    host=REDIS_HOST,
    password=REDIS_PASSWORD,
    port=REDIS_PORT,
    db=REDIS_DB,
    charset="utf-8",
    decode_responses=True,
)
