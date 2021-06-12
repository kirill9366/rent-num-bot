from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import bot

from loguru import logger


async def start_handler(message: types.Message):

    await bot.send_message(
        message.chat.id,
        'message_all_ok_bro!',
    )
