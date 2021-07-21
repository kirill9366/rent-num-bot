from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from data import config

from peewee_async import (
    Manager,
    MySQLDatabase,
)
from playhouse.migrate import MySQLMigrator
from playhouse.shortcuts import ReconnectMixin

import pyqiwi

from smsactivateru import Sms

import requests

import simplejson


bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.MARKDOWN, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
qiwi_api = pyqiwi.Wallet(
    token=config.QIWI_API_KEY,
    number=config.QIWI_NUMBER,
)


class SmsActivateWrapper(Sms):

    def request(self, action, response_format='string'):
        try:
            params = {**{'api_key': self.key}, **action.data}
            response = requests.get(self.url, params)

            if response_format == 'string':
                return response.text
            elif response_format == 'json':
                try:
                    return response.json()
                except simplejson.errors.JSONDecodeError:
                    return response.text
            else:
                return 'BAD_FORMAT'
        except (ConnectionError, TimeoutError):
            return 'NO_CONNECTION'


sms_activate_api = SmsActivateWrapper(config.SMS_API_KEY)


class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass


database = ReconnectMySQLDatabase(
    database=config.DB_NAME,
    user=config.DB_USERNAME,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    charset=config.DB_CHARSET,
)
migrator = MySQLMigrator(database)
objects = Manager(database)
