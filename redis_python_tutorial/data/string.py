"""Working with string values."""
from redis import Redis

from redis_python_tutorial.logger import LOGGER


def string_values_demo(r: Redis):
    """
    Work with Redis strings to store simple values, or manipulate them as integers.

    :param Redis r: Remote Redis instance.
    """
    # Create string value
    r.set("index", "1")
    LOGGER.info(f"index: {r.get('index')}")

    # Increment string by 1
    r.incr("index")
    LOGGER.info(f"index: {r.get('index')}")

    # Decrement string by 1
    r.decr("index")
    LOGGER.info(f"index: {r.get('index')}")

    # Increment string by 3
    r.incrby("index", 3)
    LOGGER.info(f"index: {r.get('index')}")
