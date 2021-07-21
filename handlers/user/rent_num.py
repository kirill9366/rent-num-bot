from aiogram import types

from keyboards.rent_num import (
    get_country_keyboard,
    get_social_network_keyboard,
    get_buy_confirm_keyboard,
    get_buy_number_keyboard,
)

from utils.sms_activate.api import (
    GetCurrentPrices,
    create_order_number,
    set_status_order,
    get_status_order,
)
from utils.db_api.tguser import (
    get_or_create_tguser,
)
from utils.db_api.country import (
    get_country_model,
)
from utils.db_api.social_network import (
    get_social_network_model,
)

from loader import (
    sms_activate_api,
    bot,
)

from loguru import logger


async def choose_country_handler(query: types.CallbackQuery):
    await query.message.edit_text(
        '''
Выберите страну:
        ''',
        reply_markup=await get_country_keyboard(),
    )


async def choose_social_network_handler(query: types.CallbackQuery):
    country_code = query.data.replace('choose_social_network ', '')
    currency_prices = GetCurrentPrices().request(sms_activate_api)

    await query.message.edit_text(
        '''
Выберите социальную сеть, для которой вам нужен номер:
        ''',
        reply_markup=await get_social_network_keyboard(
            country_code,
            prices_dict=currency_prices,
        ),
    )


async def buy_confirm_handler(query: types.CallbackQuery):
    country_code, social_network_code, price = (
        query
        .data
        .replace('buy_confirm ', '')
        .split()
    )
    country = await get_country_model(code=int(country_code))
    social_network = await get_social_network_model(code=social_network_code)
    await query.message.edit_text(
        f'''
Вы хотите арендовать номер:
Страна: {country.title}
Социальная сеть: {social_network.title}
Цена: {price} р.
        ''',
        reply_markup=await get_buy_confirm_keyboard(
            country_code,
            social_network_code,
            price,
        )
    )


async def buy_number_handler(query: types.CallbackQuery):
    logger.info('buy_number')
    country_code, social_network_code, price = (
        query
        .data
        .replace('buy_number ', '')
        .split()
    )
    user_id = query.message.chat.id
    user = await get_or_create_tguser(user_id)
    if user.balance >= int(price):
        user.balance -= int(price)
        user.save()
        status, order_id, phone_number = await create_order_number(
            country_code,
            social_network_code,
        )
        await set_status_order(order_id)
        country = await get_country_model(code=int(country_code))
        social_network = await get_social_network_model(
            code=social_network_code,
        )
        await query.message.edit_text(
            f'''
Вы арендовали номер:
Страна: {country.title}
Социальная сеть: {social_network.title}
Номер телефона: {phone_number}
            ''',
            reply_markup=await get_buy_number_keyboard(
                order_id,
                price,
            )
        )
    else:
        await bot.answer_callback_query(
            query.message.chat.id,
            text='У вас не достаточно средств'
        )


async def check_sms_handler(query: types.CallbackQuery):
    order_id = query.data.replace('check_sms ', '')
    logger.info(query.data)
    try:
        order_status = await get_status_order(order_id)
    except Exception as e:
        logger.warning(e)
        return await query.message.edit_text(
            f'Время получения сообщения вышло'
        )
    logger.info(order_status)
    if order_status['code']:
        await query.message.edit_text(
            f'Код из смс: {order_status["code"]}'
        )
        await set_status_order(
            order_id,
            status='end'
        )
    else:
        await bot.answer_callback_query(
            query.id,
            text='Сообщение не пришло'
        )


async def number_already_used_handler(query: types.CallbackQuery):
    order_id, price = query.data.replace('number_already_used ', '').split()
    await set_status_order(
        order_id,
        status='already_used'
    )
    user = await get_or_create_tguser(
        user_id=query.message.chat.id,
    )
    user.balance += int(price)
    user.save()
    await query.message.edit_text(
        'Средства были возвращены на ваш баланс!'
    )
