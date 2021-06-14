import peewee

from loader import database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class CountryModel(BaseModel):
    title = peewee.CharField(max_length=100)
    code = peewee.IntegerField()


class SocialNetworkModel(BaseModel):
    title = peewee.CharField(max_length=100)
    code = peewee.CharField(max_length=10)


class TGUserModel(BaseModel):
    user_id = peewee.CharField(max_length=20)
    balance = peewee.IntegerField(default=0)


class QiwiOrderModel(BaseModel):
    tguser = peewee.ForeignKeyField(TGUserModel)
    signature = peewee.CharField(max_length=50)
    quantity_attempts = peewee.IntegerField(default=0)
    amount = peewee.IntegerField(null=True)
    paid = peewee.BooleanField(default=False)
