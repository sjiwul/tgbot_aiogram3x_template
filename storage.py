from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

storage = RedisStorage(
    Redis()
)
