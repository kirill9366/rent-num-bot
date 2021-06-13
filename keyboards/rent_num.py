from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from utils.db_api.country import get_all_countries


async def get_country_keyboard():
    country_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    countries = await get_all_countries()
    for country in countries:
        country_keyboard.add(
            InlineKeyboardButton(
                country.title,
                callback_data=f'choose_country {country.code}',
            )
        )
    return country_keyboard
