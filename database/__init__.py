from .models import (
    CountryModel,
)


def setup():
    if not CountryModel.table_exists():
        CountryModel.create_table()
