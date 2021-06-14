from loader import qiwi_api


async def get_transactions():
    return qiwi_api.history()['transactions']
