from aiogram import types

from loader import bot

from keyboards.balance import get_balance_keyboard


async def balance_handler(message: types.Message):

    await bot.send_message(
        message.chat.id,
        '''
Баланс: 0 р.
        ''',
        reply_markup=await get_balance_keyboard(),
    )


async def top_up_balance_handler(query: types.CallbackQuery):
    await query.message.edit_text(
        '''
Вам нужно отправить деньги на номер 239423 с комментарием:
sdl2-2ldk-232l-ljkd
        ''',
    )
