"""Application entry point."""
import redis
from config import redis_uri, redis_expiration

r = redis.StrictRedis(url=redis_uri,
                      charset="utf-8",
                      decode_responses=True)


def main():
    r.set('name', 'todd')
    r.set('ip_address', '0.0.0.0.')
    r.set('entry_page', 'dashboard')
    r.set('current_page', 'account')
    r.set('name', 'todd', redis_expiration)
    r.set('name', 'todd', redis_expiration)
    r.set('name', 'todd', redis_expiration)
