import os

from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv

from storage import storage

load_dotenv(".env")

bot = Bot(
    os.getenv("TOKEN")
)

dp = Dispatcher(
    storage=storage
)

main_router = Router()
