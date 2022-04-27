"""Working with list values."""
from redis import Redis

from redis_python_tutorial.logger import LOGGER


def list_values_demo(r: Redis):
    """
    Create and modify a Redis list.

    :param Redis r: Remote Redis instance.
    """
    """Push and pop items from a list."""
    # Add single string to a new list.
    r.lpush("my_list", "A")
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")

    # Push second string to list from the right.
    r.rpush("my_list", "B")
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")

    # Push third string to list from the right.
    r.rpush("my_list", "C")
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")

    # Remove 1 instance from the list where the value equals 'C'.
    r.lrem("my_list", 1, "C")
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")

    # Push a string to our list from the left.
    r.lpush("my_list", "C")
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")

    # Pop first element of our list and move it to the back.
    r.rpush("my_list", r.lpop("my_list"))
    LOGGER.info(f"my_list: {r.lrange('my_list', 0, -1)}")
