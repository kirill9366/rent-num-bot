from smsactivateru.models import ActionsModel
from smsactivateru import (
    SetStatus,
    SmsTypes,
    GetStatus,
)

import inspect

from loader import sms_activate_api

from loguru import logger


class GetCurrentPrices(ActionsModel):
    _name = 'getPrices'

    def __init__(self):
        super().__init__(inspect.currentframe())

    def __response_processing(self, response):
        return response

    def request(self, wrapper):
        """
        :rtype: dict
        """
        response = wrapper.request(self, response_format='json')
        return self.__response_processing(response)


class GetNumber(ActionsModel):
    _name = 'getNumber'

    def __init__(
        self,
        service,
        country=None,
        operator=None,
        forward=False,
        ref=None,
    ):
        self.service = service
        self.forward = int(forward)
        self.country = country
        super().__init__(inspect.currentframe())

    def __response_processing(self, response, wrapper):
        return response.split(':')

    def request(self, wrapper):
        """
        :rtype: smsactivateru.activations.SmsActivation
        """
        response = wrapper.request(self, response_format='json')
        return self.__response_processing(response, wrapper=wrapper)


async def get_current_country_prices(country_code):
    return GetCurrentPrices().request(sms_activate_api)[country_code]


async def create_order_number(
    country_code,
    social_network_code,
):
    result =  GetNumber(
        social_network_code,
        country=country_code,
    ).request(sms_activate_api)
    logger.info(result)
    return result


async def set_status_order(order_id, status='start'):
    if status == 'start':
        status = SmsTypes.Status.SmsSent
    elif status == 'end':
        status = SmsTypes.Status.End
    elif status == 'already_used':
        status = SmsTypes.Status.AlreadyUsed
    else:
        return False
    return SetStatus(
        id=order_id,
        status=status
    ).request(sms_activate_api)


async def get_status_order(order_id):
    return GetStatus(id=order_id).request(sms_activate_api)
