from aiogram import types

from loader import bot

from keyboards.start import get_menu_keyboard

from utils.db_api.tguser import get_or_create_tguser


async def start_handler(message: types.Message):
    await get_or_create_tguser(message.chat.id)
    await bot.send_message(
        message.chat.id,
        '''
Здравствуйте!
Если вам нужно быстро и легко арендовать номер телефона, то я смогу вам помочь!
Код данного бота можно посмотреть по ссылке:
https://github.com/kirill9366/rent-num-bot
        ''',
        reply_markup=await get_menu_keyboard(),
    )
