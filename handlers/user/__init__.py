from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from .start import (
    start_handler,
)
from .menu import (
    menu_handler,
)
from .balance import (
    balance_handler,
    top_up_balance_handler,
    check_payment_handler,
)
from .rent_num import (
    choose_country_handler,
    choose_social_network_handler,
    buy_confirm_handler,
    buy_number_handler,
    check_sms_handler,
    number_already_used_handler,
)


def setup(dp: Dispatcher):
    dp.register_message_handler(
        start_handler,
        CommandStart(),
    )
    dp.register_message_handler(
        menu_handler,
        text='Главное меню',
    )
    dp.register_message_handler(
        balance_handler,
        text='Баланс',
    )
    dp.register_callback_query_handler(
        top_up_balance_handler,
        text_contains='top_up_balance',
    )
    dp.register_callback_query_handler(
        choose_country_handler,
        text_contains='rent_num',
    )
    dp.register_callback_query_handler(
        choose_social_network_handler,
        text_contains='choose_social_network',
    ),
    dp.register_callback_query_handler(
        buy_confirm_handler,
        text_contains='buy_confirm',
    ),
    dp.register_callback_query_handler(
        buy_number_handler,
        text_contains='buy_number',
    ),
    dp.register_callback_query_handler(
        check_sms_handler,
        text_contains='check_sms',
    ),
    dp.register_callback_query_handler(
        number_already_used_handler,
        text_contains='number_already_used',
    ),
    dp.register_callback_query_handler(
        check_payment_handler,
        text_contains='check_payment',
    )
