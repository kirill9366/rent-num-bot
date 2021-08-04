from aiogram import types

from loader import bot

from data import config

from uuid import uuid4

from loguru import logger

from keyboards.balance import (
    get_balance_keyboard,
    check_payment_keyboard,
)

from database import (
    qiwi_order_model,
    tg_user_model,
)


async def balance_handler(message: types.Message):
    user = await tg_user_model.get_object(user_id=message.chat.id)
    await bot.send_message(
        message.chat.id,
        f'''
Баланс: {user.get_field("balance")} р.
        ''',
        reply_markup=await get_balance_keyboard(),
    )


async def top_up_balance_handler(query: types.CallbackQuery):
    user = await tg_user_model.get_object(user_id=query.message.chat.id)
    signature = uuid4()
    qiwi_order = await qiwi_order_model.create_object(
        tguser=user.get_field('id'),
        signature=signature,
    )
    await query.message.edit_text(
        f"""
Вам нужно отправить деньги на номер <code>{config.QIWI_NUMBER}</code> с комментарием:
<code>{qiwi_order.get_field("signature")}</code>
После чего деньги поступят на ваш баланс.
        """,
        reply_markup=await check_payment_keyboard(signature),
    )


async def check_payment_handler(query: types.CallbackQuery):
    signature = query.data.replace('check_payment ', '')
    tguser = await tg_user_model.get_object(user_id=query.message.chat.id,)
    qiwi_order = await qiwi_order_model.get_object(
        signature=signature,
    )
    logger.info(qiwi_order.get_field('paid'))
    if qiwi_order.get_field('paid') == 1:
        tguser_balance = tguser.get_field('balance')
        await tguser.update_field(
            'balance',
            tguser_balance + qiwi_order.get_field('amount')
        )
        await query.message.edit_text(
            text=f'Баланс: {tguser.get_field("balance")} р.'
        )
    else:
        if qiwi_order.get_field('quantity_attempts') >= 5:
            await qiwi_order.delete()
            await query.message.edit_text(
                text='Слишком большое количество попыток!'
            )
        quantity_attempts = qiwi_order.get_field('quantity_attempts')
        await qiwi_order.update_field(
            'quantity_attempts',
            quantity_attempts + 1,
        )
        await bot.answer_callback_query(
            query.id,
            text='Оплата не пришла, попробуйте еще раз нажать на кнопку позже'
        )
