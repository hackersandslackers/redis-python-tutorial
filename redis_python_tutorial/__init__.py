from redis_python_tutorial.client import r
from redis_python_tutorial.data import set_single_values, set_nested_values


def main():
    """Create records in Redis."""
    set_single_values(r)
    set_nested_values(r)
