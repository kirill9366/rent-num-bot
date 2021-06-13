from aiogram import types

from loader import bot

from keyboards.start import get_menu_keyboard


async def start_handler(message: types.Message):

    await bot.send_message(
        message.chat.id,
        '''
Здравствуйте!
Если вам нужно быстро и легко арендовать номер телефона, то я смогу вам помочь!
        ''',
        reply_markup=await get_menu_keyboard(),
    )
