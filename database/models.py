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
