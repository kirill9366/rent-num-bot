from aiogram import types

from loader import bot

from loguru import logger

from keyboards.start import get_menu_keyboard

from database import tg_user_model


async def start_handler(message: types.Message):
    user_id = message.chat.id
    if await tg_user_model.select_objects(
        where={
            'field': 'user_id',
            'operator': '==',
            'value': user_id,
        }
    ):
        logger.info('create user')
        await tg_user_model.create_object(user_id=user_id)

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
