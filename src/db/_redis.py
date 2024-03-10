import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_db() -> redis.Redis:
    try:
        return r
    finally:
        r.close()
