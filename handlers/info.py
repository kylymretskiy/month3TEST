from aiogram import types , Dispatcher

# @dp.message_handler(commands=['myinfo'])
async def myinfo_command(message: types.Message):
    info = (
        "Я бот для добавления товаров и оформления заказов.\n"
        "Доступные команды:\n"
        "/info - информация обо мне\n"
        "/products - показать все товары\n"
        "/store - запись товаров"
    )
    await message.reply(info)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(myinfo_command, commands=['info'])