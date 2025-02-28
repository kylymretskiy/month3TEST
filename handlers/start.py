from aiogram import types , Dispatcher
from aiogram.types import (
    CallbackQuery
)

async def start_command(message: types.Message):
    user = message.from_user
    await message.answer(f"Hello , {user.first_name}")


async def about_us_handler(callback: CallbackQuery):
    await callback.answer("О нас", show_alert=True)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])