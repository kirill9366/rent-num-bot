from aiogram import types

from keyboards.rent_num import get_country_keyboard


async def choose_country_handler(query: types.CallbackQuery):
    await query.message.edit_text(
        '''
Выберите страну:
        ''',
        reply_markup=await get_country_keyboard(),
    )
