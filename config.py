"""Construct Redis connection URI."""
from os import environ
from dotenv import load_dotenv


# Load environment variables
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

redis_host = environ.get('REDIS_HOST')
redis_password = environ.get('REDIS_PASSWORD')
redis_port = environ.get('REDIS_PORT')
redis_db = environ.get('REDIS_DATABASE')
redis_uri = f'redis://:{redis_host}@{redis_password}:{redis_port}/{redis_db}'

redis_expiration = 604800
