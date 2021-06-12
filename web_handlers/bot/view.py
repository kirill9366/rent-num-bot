from aiogram import Bot, Dispatcher, types

from aiohttp import web


async def proceed_update(req: web.Request):
    upds = [types.Update(**(await req.json()))]
    Bot.set_current(req.app['bot'])
    Dispatcher.set_current(req.app['dp'])
    await req.app['dp'].process_updates(upds)


async def execute(req: web.Request) -> web.Response:
    await req.app['scheduler'].spawn(proceed_update(req))
    return web.Response()

bot_app = web.Application()
bot_app.router.add_routes([web.post('/', execute)])
