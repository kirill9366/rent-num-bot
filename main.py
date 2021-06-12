from aiohttp import web
import aiohttp_jinja2
import jinja2

import aiojobs

from loguru import logger

from typing import List

import base64

import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

# locale imports
import loader

from data import config

from handlers import setup

import database

import web_handlers
from web_handlers.middleware.session import request_user_middleware

import os


async def on_startup(app: web.Application):

    setup(loader.dp)
    database.setup()

    if config.BOT_PLACE == 'locale':
        await loader.dp.start_polling()
    else:
        await loader.dp.bot.delete_webhook()
        await loader.dp.bot.set_webhook(
            config.WEBHOOK_URL + config.PROJECT_PATH + '/bot/'
        )

    logger.info(
        f'Configure Webhook URL to: {config.WEBHOOK_URL + config.PROJECT_PATH + "/bot/"}'  # noqa E501
    )


async def on_shutdown(app: web.Application):
    app_bot = app['bot']
    await app_bot.close()


async def init():

    # initialize web-app
    app = web.Application()

    fernet_key = b'GA61UkHuur1qPiMCEjLuo1SlBp8TNU0h7Hgusas6uZ0='
    secret_key = base64.urlsafe_b64decode(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))

    app.middlewares.append(request_user_middleware)

    aiohttp_jinja2.setup(
        app,
        context_processors=[aiohttp_jinja2.request_processor],
        loader=jinja2.FileSystemLoader('./web_handlers/templates/'),
    )
    # initialize subapps
    subapps: List[str, web.Application] = [
        (f'{config.PROJECT_PATH}/bot/', web_handlers.bot_app),
    ]

    env = aiohttp_jinja2.get_env(app)
    env.globals.update(str=str)

    scheduler = await aiojobs.create_scheduler()
    for prefix, subapp in subapps:
        subapp['bot'] = loader.bot
        subapp['dp'] = loader.dp
        subapp['scheduler'] = scheduler

        app.add_subapp(prefix, subapp)

    # add static
    path = os.path.join(os.path.dirname(__file__), 'web_handlers/static')
    app.router.add_static('/static/', path, name='static')

    app.on_shutdown.append(on_shutdown)
    app.on_startup.append(on_startup)

    return app

if __name__ == '__main__':
    web.run_app(init(), host=config.HOST, port=config.PORT)
