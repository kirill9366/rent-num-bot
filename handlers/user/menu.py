from aiogram import types

from loader import bot

from keyboards.menu import get_menu_keyboard


async def menu_handler(message: types.Message):

    await bot.send_message(
        message.chat.id,
        '''
Меню.
        ''',
        reply_markup=await get_menu_keyboard(),
    )
