"""Shared logger."""
import sys
from loguru import logger


logger.remove()
logger.add(
    sys.stderr,
    format="{message}",
    level="INFO"
)
