from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


async def get_menu_keyboard():
    menu_keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,
    )
    menu_keyboard.add(
        KeyboardButton(
            'Главное меню'
        )
    )
    menu_keyboard.add(
        KeyboardButton(
            'Баланс'
        )
    )
    return menu_keyboard
