# Что бы не ... скачаем cmd-  pip install pycoingecko
# Пока сложно возможно придеться удалять лишнее
import logging
from aiogram import Bot,Dispatcher, executor, types
from pycoingecko import CoinGeckoAPI

from venv.create_bot import dp, bot
from keyBord import cripto_list

logging.basicConfig(level=logging.INFO)

cg = CoinGeckoAPI()

# @dp.message_handler(command=['    dp.register_message_handler(cr_start, commands=['rypto.rates'])    dp.register_message_handler(cr_start, commands=['rypto.rates'])'])
async def cr_start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Выберите криптовалюту:", reply_markup=cripto_list)

# @dp.callback_query_handler(text_contains="cc_")
async def crupto(call: types.CallbackQuery):
    await bot.send_message('подумать')
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies = 'usd')
    # print(result)
    await bot.send_message(call.from_user.id, f"Криптовалюта: {currency} \nСтоимость сейчас: {result[currency]['usd']}$", reply_markup=cripto_list)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cr_start, commands=['Cryptorates'])
    dp.callback_query_handler(crupto, text_contains="cc/")


















# from aiogram.utils import executor
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from venv.config import tg_bot_token
#
# bot = Bot(token=tg_bot_token)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])
# async def command_start(message : types.Message):
#     await message.reply('Hello')
#
# @dp.message_handler(commands=['команда']):
# async def echo(message : types.Message):
#     await message.answer(message.text)
#
# @dp.message_handler()
# async def empty(message : types.Message):
#     await message.answer('Такой команды не бывает')
#     await message.delete()
#
# executor.start_polling(dp, skip_updates=True)
