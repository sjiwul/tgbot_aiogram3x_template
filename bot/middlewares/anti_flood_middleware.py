from typing import Callable, Dict, Any, Awaitable

import cachetools
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(
            self,
            max_size: int = 100_000,
            ttl: int = 3
    ) -> None:
        self.ttlcache = cachetools.TTLCache(maxsize=max_size, ttl=ttl)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in self.ttlcache:
            return await event.delete()
        self.ttlcache[event.from_user.id] = None
        return await handler(event, data)
