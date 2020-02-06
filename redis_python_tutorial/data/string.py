"""Working with string values."""
from redis_python_tutorial.logging import logger


def string_values_demo(r):
    """Manipulate strings as integers."""
    # Create string value
    r.set('index', '1')
    logger.info(f"index: {r.get('index')}")

    # Increment string by 1
    r.incr('index')
    logger.info(f"index: {r.get('index')}")

    # Decrement string by 1
    r.decr('index')
    logger.info(f"index: {r.get('index')}")

    # Increment string by 3
    r.incrby('index', 3)
    logger.info(f"index: {r.get('index')}")
