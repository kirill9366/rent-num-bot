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


async def check_payment_keyboard(signature):
    check_payment_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    check_payment_keyboard.add(
        InlineKeyboardButton(
            'Проверить платеж',
            callback_data=f'check_payment {signature}',
        )
    )
    return check_payment_keyboard
