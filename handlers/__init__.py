from aiogram import Dispatcher

from . import (
    user,
    callback_commands,
)


def setup(dp: Dispatcher):
    user.setup(dp)
    callback_commands.setup(dp)
