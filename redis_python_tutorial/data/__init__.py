"""Set and manipulate data in Redis."""
from time import time

from config import REDIS_EXPIRATION


def init_db_with_values(r):
    """Set single key/value pairs."""
    r.set("ip_address", "0.0.0.0.")
    r.set("timestamp", int(time()))
    r.set("user_agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)")
    r.set("current_page", "account", REDIS_EXPIRATION)
    return r.keys()
