async def increase_number_price(price, percent_of_increase):
    if not isinstance(price, int):
        price = int(price)
    if not isinstance(percent_of_increase, int):
        percent_of_increase = int(percent_of_increase)

    return int(price * (1 + percent_of_increase / 100))
