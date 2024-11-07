from typing import Any

from aiogram.types import Message


async def start(
        message: Message
) -> Any:
    await message.answer(
        "<b>Hello, world!</b>"
    )
