from database.models import TGUserModel

from loader import objects


async def get_or_create_tguser(user_id):
    return (await objects.get_or_create(
        TGUserModel,
        user_id=user_id,
    ))[0]
