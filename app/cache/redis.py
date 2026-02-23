import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_cache(key: str):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key: str, value, expire: int = 3600):
    redis_client.set(key, json.dumps(value), ex=expire)