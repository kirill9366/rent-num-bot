from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def get_menu_keyboard():
    lesson_keyboard = InlineKeyboardMarkup(
        row_width=1,
    )
    lesson_keyboard.add(
        InlineKeyboardButton(
            'Арендовать номер',
            callback_data=f'choose_country',
        )
    )
    lesson_keyboard.add(
        InlineKeyboardButton(
            'О боте',
            callback_data=f'about_bot',
        )
    )
    return lesson_keyboard
