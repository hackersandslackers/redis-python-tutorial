"""Working with set values."""
from redis import Redis

from redis_python_tutorial.logger import LOGGER


def set_values_demo(r: Redis):
    """
    Create Redis sets & execute unions and intersects.

    :param Redis r: Remote Redis instance.
    """
    # Add item to set 1
    r.sadd("my_set_1", "Y")
    LOGGER.info(f"my_set_1: {r.smembers('my_set_1')}'")

    # Add item to set 1
    r.sadd("my_set_1", "X")
    LOGGER.info(f"my_set_1: {r.smembers('my_set_1')}'")

    # Add item to set 2
    r.sadd("my_set_2", "X")
    LOGGER.info(f"my_set_2: {r.smembers('my_set_2')}'")

    # Add item to set 2
    r.sadd("my_set_2", "Z")
    LOGGER.info(f"my_set2: {r.smembers('my_set_2')}'")

    # Union set 1 and set 2
    LOGGER.info(f"Union: {r.sunion('my_set_1', 'my_set_2')}")

    # Intersect set 1 and set 2
    LOGGER.info(f"Intersect: {r.sinter('my_set_1', 'my_set_2')}")
