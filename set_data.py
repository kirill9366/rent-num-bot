from utils.db_api.country import create_country_model
from utils.db_api.social_network import create_social_network

import asyncio

from database import setup

setup()


async def create_countries():
    countries = [
        ('Россия', 0),
        ('Украина', 1),
        ('Казахстан', 2),
        ('США', 187),
        ('Либерия', 135),
        ('Греция', 129),
    ]
    for country in countries:
        await create_country_model(
            country[0],
            country[1],
        )


async def create_social_networks():
    social_networks = [
        ('Вконтакте', 'vk'),
        ('Telegram', 'tg'),
        ('Facebook', 'fb'),
        ('Uber', 'ub'),
        ('Steam', 'mt'),
        ('Delivery Club', 'dt'),
        ('Netflix', 'nf'),
        ('Discord', 'ds'),
        ('TikTok', 'lf'),
        ('Faceit', 'qz'),
    ]
    for social_network in social_networks:
        await create_social_network(
            social_network[0],
            social_network[1],
        )


async def main():
    # await create_countries()
    await create_social_networks()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
