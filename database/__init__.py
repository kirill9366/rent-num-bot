from .models import (
    CountryModel,
    SocialNetworkModel,
    TGUserModel,
    QiwiOrderModel,
)


def setup():
    if not CountryModel.table_exists():
        CountryModel.create_table()
    if not SocialNetworkModel.table_exists():
        SocialNetworkModel.create_table()
    if not TGUserModel.table_exists():
        TGUserModel.create_table()
    if not QiwiOrderModel.table_exists():
        QiwiOrderModel.create_table()
