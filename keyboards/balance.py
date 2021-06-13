from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def get_balance_keyboard():
    lesson_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    lesson_keyboard.add(
        InlineKeyboardButton(
            'Пополнить баланс',
            callback_data=f'top_up_balance',
        )
    )
    return lesson_keyboard
