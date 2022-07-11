from aiogram import types
from create_bot import dp


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        await message.answer('Давайте знакомиться. Как вы уже поняли, мы занимается инвестициями в криптовалюты.\n'
                             ' Наша команда создала этот Бот для удобства работы с подписчиками. \n'
                             'Ниже вы видите ключевые разделы нашего проекта. \n'
                             'Советуем продолжить знакомство с истории нашей команды')


def register_handlers_other(dp):
    dp.register_message_handler(echo_send)
