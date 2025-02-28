from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from bot_config import database , STAFF


# from db import main_db


class OrderFSM(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    number = State()
    submit = State()



async def start_fsm_order(message: types.Message):
    await OrderFSM.product_id.set()
    await message.answer('Введите артикул товара: ')


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await OrderFSM.next()
    await message.answer('Отправьте размер товара:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await OrderFSM.next()
    await message.answer('Кол-во товара:')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await OrderFSM.next()
    await message.answer('Введите номер телефона:')


async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text

    await OrderFSM.submit.set()
    await message.answer('Верный ли данные ?'
                                       f'Артикул - {data["product_id"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Кол-во - {data["quantity"]}\n'
                                       f'Номер - {data["number"]}\n'
                                       )

async def submit_load(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            database.add_order(data)
            await message.answer('Ваши данные в базе!')
        await state.finish()
    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm,
                                Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_order, commands=['order'])
    dp.register_message_handler(load_product_id, state=OrderFSM.product_id)
    dp.register_message_handler(load_size, state=OrderFSM.size)
    dp.register_message_handler(load_quantity, state=OrderFSM.quantity)
    dp.register_message_handler(load_number, state=OrderFSM.number)
    dp.register_message_handler(submit_load, state=OrderFSM.submit)