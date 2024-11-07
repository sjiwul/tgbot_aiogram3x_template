from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from decouple import config

from storage import storage

bot = Bot(
    token=config("BOT_TOKEN"),
    default=DefaultBotProperties(
        parse_mode="HTML"
    )
)

dp = Dispatcher(
    storage=storage
)

main_router = Router()
