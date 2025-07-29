from aiogram import types, Dispatcher
from keyboards import get_main_menu
from sheets import save_to_sheet

async def start_handler(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=get_main_menu())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])