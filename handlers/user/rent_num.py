from aiogram import types

from keyboards.rent_num import (
    get_country_keyboard,
    get_social_network_keyboard,
)


async def choose_country_handler(query: types.CallbackQuery):
    await query.message.edit_text(
        '''
Выберите страну:
        ''',
        reply_markup=await get_country_keyboard(),
    )


async def choose_social_network_handler(query: types.CallbackQuery):
    await query.message.edit_text(
        '''
Выберите социальную сеть, для которой вам нужен номер:
        ''',
        reply_markup=await get_social_network_keyboard(),
    )
