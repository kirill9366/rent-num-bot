from aiogram import types

from loader import bot

from data import config

from keyboards.balance import (
    get_balance_keyboard,
    check_payment_keyboard,
)

from utils.db_api.tguser import get_or_create_tguser
from utils.db_api.qiwiorder import (
    get_qiwi_order,
    create_qiwi_order,
)


async def balance_handler(message: types.Message):
    user = await get_or_create_tguser(message.chat.id)
    await bot.send_message(
        message.chat.id,
        f'''
Баланс: {user.balance} р.
        ''',
        reply_markup=await get_balance_keyboard(),
    )


async def top_up_balance_handler(query: types.CallbackQuery):
    qiwi_order = await create_qiwi_order(query.message.chat.id)
    await query.message.edit_text(
        f"""
Вам нужно отправить деньги на номер ```{config.QIWI_NUMBER}``` с комментарием:
```{qiwi_order.signature}```
После чего деньги поступят на ваш баланс.
        """,
        reply_markup=await check_payment_keyboard(),
    )


async def check_payment_handler(query: types.CallbackQuery):
    tguser = await get_or_create_tguser(
        query.message.chat.id,
    )
    qiwi_order = await get_qiwi_order(tguser=tguser)
    if qiwi_order.paid:
        tguser.balance += qiwi_order.amount
        tguser.save()
        await query.message.edit_text(
            text=f'Баланс: {tguser.balance} р.'
        )
    else:
        if qiwi_order.quantity_attempts >= 5:
            qiwi_order.delete_instance()
            await query.message.edit_text(
                text='Слишком большое количество попыток!'
            )
        qiwi_order.quantity_attempts += 1
        qiwi_order.save()
        await bot.answer_callback_query(
            query.id,
            text='Оплата не пришла, попробуйте еще раз нажать на кнопку позже'
        )
