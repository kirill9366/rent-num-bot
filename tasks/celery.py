from celery import Celery

from database import (
    qiwi_order_model,
)
from utils.qiwi_api import get_transactions

import asyncio

import time

import requests


app = Celery(
    'rentnumbot',
)


@app.task
def check_payments():
    loop = asyncio.get_event_loop()
    while True:
        try:
            transactions = loop.run_until_complete(
                get_transactions()
            )
        except requests.exceptions.SSLError:
            time.sleep(5)
            continue
        for transaction in transactions:
            if not transaction.comment:
                continue
            qiwi_order = qiwi_order_model.get_object(
                signature=transaction.comment
            )
            if qiwi_order:
                qiwi_order.amount = transaction.sum.amount
                qiwi_order.paid = True
                qiwi_order.save()
        time.sleep(5)
