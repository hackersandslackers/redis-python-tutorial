"""Shared logger."""
import sys
from loguru import logger


logger.add(sys.stderr,
           format="{message}",
           filter="redis_python_tutorial",
           level="INFO")
