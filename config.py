"""Construct Redis connection URI."""
from os import getenv, path

from dotenv import load_dotenv

# Load environment variables
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Redis config
REDIS_HOST = getenv("REDIS_HOST")
REDIS_USERNAME = getenv("REDIS_USERNAME")
REDIS_PASSWORD = getenv("REDIS_PASSWORD")
REDIS_PORT = getenv("REDIS_PORT")
REDIS_DB = getenv("REDIS_DB")
REDIS_URI = f"redis://:{REDIS_HOST}@{REDIS_USERNAME}:{REDIS_PORT}/{REDIS_DB}"

REDIS_EXPIRATION = 604800

# Logging
PERSIST_LOG_FILES = True
