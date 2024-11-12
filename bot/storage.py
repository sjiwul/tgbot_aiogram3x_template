from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder

storage = RedisStorage(
    redis=Redis(),
    key_builder=DefaultKeyBuilder(
        with_bot_id=True,
        with_destiny=True
    )
)
