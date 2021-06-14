from database.models import SocialNetworkModel

from loader import objects


async def create_social_network(title, code):
    await objects.create(
        SocialNetworkModel,
        title=title,
        code=code,
    )


async def get_all_social_networks():
    return await objects.execute(
        SocialNetworkModel.select()
    )
