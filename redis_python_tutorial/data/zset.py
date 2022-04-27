"""Working with sorted set values."""
from redis import Redis

from redis_python_tutorial.logger import LOGGER


def sorted_set_values_demo(r: Redis):
    """
    Create Redis sorted sets and manipulate the contents.

    :param Redis r: Remote Redis instance.
    """
    # Initialize sorted set with 3 values
    r.zadd(
        "top_songs_set",
        {"Never Change - Jay Z": 1, "Rich Girl - Hall & Oats": 2, "The Prayer - Griz": 3},
    )
    LOGGER.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")

    # Add item to set with conflicting value
    r.zadd("top_songs_set", {"Can't Figure it Out - Bishop Lamont": 3})
    LOGGER.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")

    # Shift index of a value
    r.zincrby("top_songs_set", 3, "Never Change - Jay Z")
    LOGGER.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")
