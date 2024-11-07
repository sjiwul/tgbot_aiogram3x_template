from aiogram import Router
from aiogram.filters.command import CommandStart

from commands.start import start


def main_register(
        router: Router
) -> None:
    router.message.register(start, CommandStart())
