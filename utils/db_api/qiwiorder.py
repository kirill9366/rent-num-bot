from database.models import (
    QiwiOrderModel,
    TGUserModel,
)

from loader import objects

from uuid import uuid4


async def get_qiwi_order(**kwargs):
    try:
        return await objects.get(
            QiwiOrderModel,
            **kwargs,
        )
    except QiwiOrderModel.DoesNotExist:
        return False


async def create_qiwi_order(user_id, signature=uuid4()):
    try:
        tguser = await objects.get(
            TGUserModel,
            user_id=user_id,
        )
    except TGUserModel.DoesNotExist:
        return False
    return await objects.create(
        QiwiOrderModel,
        tguser=tguser,
        signature=signature,
    )
