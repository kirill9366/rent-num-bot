from .models import (
    CountryModel,
    SocialNetworkModel,
)


def setup():
    if not CountryModel.table_exists():
        CountryModel.create_table()
    if not SocialNetworkModel.table_exists():
        SocialNetworkModel.create_table()
