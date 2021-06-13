from database.models import CountryModel

from loader import objects


async def create_country_model(
    title,
    code,
):
    await objects.create(
        CountryModel,
        title=title,
        code=code,
    )


async def get_all_countries():
    return await objects.execute(
        CountryModel.select()
    )
