import redis
from config import (redis_host,
                    redis_password,
                    redis_port,
                    redis_db)

r = redis.StrictRedis(host=redis_host,
                      password=redis_password,
                      port=redis_port,
                      db=redis_db,
                      charset="utf-8",
                      decode_responses=True)
