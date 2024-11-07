from typing import Any

from middlewares.anti_flood_middleware import AntiFloodMiddleware
from registers import main_register
from . import bot, dp, main_router


async def on_startup() -> Any:
    from aiogram.types import BotCommand
    await bot.delete_webhook(
        drop_pending_updates=True
    )
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start the bot.")
        ],
        language_code="en"
    )


async def on_shutdown() -> Any: pass


async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    main_router.message.middleware(AntiFloodMiddleware())
    dp.include_routers(main_router)
    main_register(main_router)
    await dp.start_polling(
        bot
    )


if __name__ == "__main__":
    import logging
    import sys
    import asyncio

    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout
    )
    asyncio.run(main())
