"""Working with hash values."""
from redis_python_tutorial.logging import logger


def hash_values_demo(r):
    """Create a hash value."""
    record = {
        "name": "Hackers and Slackers",
        "description": "Mediocre tutorials",
        "website": "https://hackersandslackers.com/",
        "github": "https://github.com/hackersandslackers"
    }
    r.hmset('business', record)
    logger.info(f"business: {r.hgetall('business')}")
