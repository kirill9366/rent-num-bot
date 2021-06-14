from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from utils.db_api.country import get_all_countries
from utils.db_api.social_network import get_all_social_networks


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


async def get_social_network_keyboard():
    social_network_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    social_networks = await get_all_social_networks()
    for social_network in social_networks:
        social_network_keyboard.add(
            InlineKeyboardButton(
                social_network.title,
                callback_data=f'choose_social_network {social_network.code}',
            )
        )
    return social_network_keyboard
