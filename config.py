"""Construct Redis connection URI."""
from os import environ

redis_host = environ.get('REDIS_HOST')
redis_password = environ.get('REDIS_PASSWORD')
redis_port = environ.get('REDIS_PORT')
redis_db = environ.get('REDIS_DATABASE')
redis_uri = f'redis://:{redis_host}@{redis_password}:{redis_port}/{redis_db}'

redis_expiration = 604800
