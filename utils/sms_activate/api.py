from smsactivateru.models import ActionsModel
from smsactivateru.errors import error_handler

import inspect

from loader import sms_activate_api


class GetCurrentPrices(ActionsModel):
    _name = 'getPrices'

    def __init__(self):
        super().__init__(inspect.currentframe())

    @error_handler
    def __response_processing(self, response):
        return response

    def request(self, wrapper):
        """
        :rtype: dict
        """
        response = wrapper.request(self)
        return self.__response_processing(response)


async def get_current_prices():
    return GetCurrentPrices().request(sms_activate_api)
