"""Working with set values."""
from redis_python_tutorial.logging import logger


def set_values_demo(r):
    """Execute unions and intersects between sets."""
    # Add item to set 1
    r.sadd('my_set_1', 'Y')
    logger.info(f"my_set_1: {r.smembers('my_set_1')}'")

    # Add item to set 1
    r.sadd('my_set_1', 'X')
    logger.info(f"my_set_1: {r.smembers('my_set_1')}'")

    # Add item to set 2
    r.sadd('my_set_2', 'X')
    logger.info(f"my_set_2: {r.smembers('my_set_2')}'")

    # Add item to set 2
    r.sadd('my_set_2', 'Z')
    logger.info(f"my_set2: {r.smembers('my_set_2')}'")

    # Union set 1 and set 2
    logger.info(f"Union: {r.sunion('my_set_1', 'my_set_2')}")

    # Interset set 1 and set 2
    logger.info(f"Intersect: {r.sinter('my_set_1', 'my_set_2')}")
