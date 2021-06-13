from utils.db_api.country import create_country_model

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


async def main():
    await create_countries()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
