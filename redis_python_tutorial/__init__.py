"""Set and manipulate data in Redis."""
from redis_python_tutorial.client import r
from redis_python_tutorial.data import init_db_with_values
from redis_python_tutorial.data.hash import hash_values_demo
from redis_python_tutorial.data.list import list_values_demo
from redis_python_tutorial.data.set import set_values_demo
from redis_python_tutorial.data.string import string_values_demo
from redis_python_tutorial.data.zset import sorted_set_values_demo


def init_app():
    """Entry point function."""
    r.flushdb()
    init_db_with_values(r)
    string_values_demo(r)
    hash_values_demo(r)
    list_values_demo(r)
    set_values_demo(r)
    sorted_set_values_demo(r)
