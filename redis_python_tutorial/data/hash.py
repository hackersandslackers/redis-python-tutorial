"""Working with hash values."""
from redis import Redis

from redis_python_tutorial.logger import LOGGER


def hash_values_demo(r: Redis):
    """
    Create a Redis hash value.

    :param Redis r: Remote Redis instance.
    """
    record = {
        "name": "Hackers and Slackers",
        "description": "Mediocre tutorials",
        "website": "https://hackersandslackers.com/",
        "github": "https://github.com/hackersandslackers",
    }
    r.hset("business", mapping=record)
    LOGGER.info(f"business: {r.hgetall('business')}")
