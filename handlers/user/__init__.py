from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from .start import (
    start_handler,
)


def setup(dp: Dispatcher):
    dp.register_message_handler(
        start_handler,
        CommandStart(),
    )
