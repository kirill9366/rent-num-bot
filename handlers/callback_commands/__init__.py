from aiogram import Dispatcher

from .message import (
    delete_message,
)


def setup(dp: Dispatcher):

    dp.register_callback_query_handler(
        delete_message,
        text_contains='delete_message',
    )
