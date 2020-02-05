"""Application entry point."""
import time
from config import redis_expiration
from loguru import logger
import sys


logger.add(sys.stderr,
           format="{time} {level} {message}",
           filter="redis_python_tutorial",
           level="INFO")


def set_single_values(r):
    """Set single key/value pairs."""
    r.set('ip_address', '0.0.0.0.')
    r.set('timestamp', int(time.time()))
    r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)')
    r.set('current_page', 'account', redis_expiration)
    logger.info(r.keys())


def set_nested_values(r):
    """Set a dictionary."""
    record = {
        "name": "Hackers and Slackers",
        "description": "Mediocre tutorials",
        "website": "https://hackersandslackers.com/",
        "github": "https://github.com/hackersandslackers"
    }
    r.hmset('business', record)
