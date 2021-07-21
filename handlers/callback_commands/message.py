from aiogram import types


async def delete_message(query: types.CallbackQuery):
    await query.message.delete()
