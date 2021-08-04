from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from database import (
    social_network_model,
    country_model,
)
from utils.price import increase_number_price

from data.config import PERCENT_OF_INCREASE_PRICE


async def get_country_keyboard():
    country_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    countries = await country_model.select_objects()
    for country in countries:
        country_code = country.get_field('code')
        country_keyboard.add(
            InlineKeyboardButton(
                country.get_field('title'),
                callback_data=f'choose_social_network {country_code}',
            )
        )
    return country_keyboard


async def get_social_network_keyboard(country_code, prices_dict=None):
    social_network_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    social_networks = await social_network_model.select_objects()
    for social_network in social_networks:
        price = ''
        if country_code in prices_dict:
            country_prices = prices_dict[country_code]
            if social_network.get_field('code') not in country_prices:
                continue
            price = prices_dict[country_code][social_network.get_field('code')]["cost"]
            price = await increase_number_price(
                price,
                PERCENT_OF_INCREASE_PRICE,
            )
            social_network_keyboard.add(
                InlineKeyboardButton(
                    social_network.get_field("title") + f' {price} р.',
                    callback_data='buy_confirm {} {} {}'.format(
                        country_code,
                        social_network.get_field('code'),
                        price,
                    ),
                )
            )
    social_network_keyboard.add(
        InlineKeyboardButton(
            'Назад',
            callback_data='rent_num',
        )
    )
    return social_network_keyboard


async def get_buy_confirm_keyboard(
    country_code,
    social_network_code,
    price,
):
    buy_confirm_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    buy_confirm_keyboard.add(
        InlineKeyboardButton(
            'Подтвердить ✅',
            callback_data='buy_number ' + ' '.join([
                country_code,
                social_network_code,
                price,
            ])
        )
    )
    buy_confirm_keyboard.add(
        InlineKeyboardButton(
            'Отмена ❌',
            callback_data='delete_message'
        )
    )
    return buy_confirm_keyboard


async def get_buy_number_keyboard(
    order_id,
    price,
):
    buy_number_keyboard = InlineKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
    )
    buy_number_keyboard.add(
        InlineKeyboardButton(
            'Проверить сообщение',
            callback_data=f'check_sms {order_id}'
        )
    )
    buy_number_keyboard.add(
        InlineKeyboardButton(
            'Номер уже был использован',
            callback_data=f'number_already_used {order_id} {price}'
        )
    )
    return buy_number_keyboard
