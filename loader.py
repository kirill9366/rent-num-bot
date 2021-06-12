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


bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


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
