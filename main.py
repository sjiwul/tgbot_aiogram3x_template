import asyncio
import logging

from __init__ import bot, dp, main_router
from middlewares.anti_flood_middleware import AntiFloodMiddleware
from registers import main_register


async def on_startup():
    from aiogram.types import BotCommand
    await bot.delete_webhook(
        drop_pending_updates=True,
        request_timeout=10
    )
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start the bot.")
        ],
        language_code="en",
        request_timeout=10
    )


async def on_shutdown(): pass


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    main_router.message.middleware(AntiFloodMiddleware())
    dp.include_routers(main_router)
    main_register(main_router)
    await dp.start_polling(
        bot,
        polling_timeout=10
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG
    )
    asyncio.run(main())
