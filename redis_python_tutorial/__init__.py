"""Application entry point."""
import sys
import redis
import json
from loguru import logger
import time
from config import (redis_host,
                    redis_password,
                    redis_port,
                    redis_db,
                    redis_expiration)

r = redis.StrictRedis(host=redis_host,
                      password=redis_password,
                      port=redis_port,
                      db=redis_db,
                      charset="utf-8",
                      decode_responses=True)


logger.add(sys.stderr,
           format="{time} {level} {message}",
           filter="redis_python_tutorial",
           level="INFO")


def main():
    """Create records in Redis."""
    set_single_values()
    set_nested_values()


def set_single_values():
    """Set single key/value pairs."""
    r.set('ip_address', '0.0.0.0.')
    r.set('timestamp', int(time.time()))
    r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)')
    r.set('current_page', 'account', redis_expiration)
    logger.info(r.keys())


def set_nested_values():
    """Set a nested dictionary."""
    record = {
        "name": "Hackers and Slackers",
        "type": "Mediocre tutorials",
        "address": {
            "street": "42 E 69th Street",
            "city": "New York",
            "state": "NY",
            "zip": 10009,
            },
        "profiles": {
            "website": "https://hackersandslackers.com/",
            "twitter": "https://twitter.com/hackersslackers",
            "facebook": "https://www.facebook.com/groups/hackersnslackers"
            },
        "owner": {
            "name": "Todd Birchard",
            "email": "todd@example.com"
            }
        }
    r.hmset('business', json.dumps(record))
