import asyncio
from aiogram import executor, types
import unittest
from unittest import TestCase
from unittest.mock import patch

# импорт текстов запросов и ответов бота
from textt_bot import *

# импорт обработчиков
from handlers import client, admin, other

# импорт обработчика клиента
from handlers.client import *
from handlers.other import *

from textt_bot import *

# тексты запросов
req_cmd = [start_c, learn_c, crypto_c]
# тексты ответов
bot_ans = [start_a, learn_a, crypto_a]

class TestBot(TestCase):

# Тестирует правильность обработки сценария, происходит проверка
# на количество ответов требуемому и что ответы соответствуют ожидаемым

    def test_scenario(self):
        # патчим, чтобы все сообщения бота собирались в send_messages
        with patch('aiogram.bot.Bot.send_message', return_value = None) as send_messages:
            # тестируем команду, которую бот не знает
            # message_mock =  unittest.mock.Mock(text = start_c)
            # asyncio.run(start_command(message_mock))
            # тестируем команду /start
            message_mock = unittest.mock.Mock(text = start_c)
            asyncio.run(start_command(message_mock))
            # тестируем команду "Наша история"
            message_mock = unittest.mock.Mock(text = learn_c)
            asyncio.run(w_command(message_mock))
            # тестируем команду "Расположение"
            # message_mock = unittest.mock.Mock(text = learn_in_my_c)
            # asyncio.run(fsm_start(message_mock))
            # тестируем команду "Часто задаваемые вопросы"
            message_mock = unittest.mock.Mock(text = crypto_c)
            asyncio.run(joke_command(message_mock))

        # здесь соберем все ответы бота
        test_ans = []
        # цикл по принятым сообщениям
        for args, kwargs in send_messages.call_args_list:
            test_ans.append(args[1])
        # проверка, что количество ответов бота соответствует заданному
        # ошибка, если количество не совпадает
        self.assertEqual(len(test_ans), len(bot_ans))
        # проверка ответов бота
        for t_ans, b_ans in zip(test_ans, bot_ans):
            # ошибка, если ответ не совпадает
            self.assertEqual(t_ans, b_ans)

if __name__ == '__main__':
    print('Тесты начались')
    unittest.main()




























# from aiogram.utils import executor
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from venv.config import tg_bot_token
#
# bot = Bot(token=tg_bot_token)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['ептстудей'])
# async def echo(message : types.Message):
#     await message.answer(message.text)
#
# @dp.message_handler(commands=['start'])
# async def command_start(message : types.Message):
#     await message.reply('Hello')
#
#
#
# @dp.message_handler()
# async def empty(message : types.Message):
#     await message.answer('Такой команды не бывает')
#     # await message.delete()
#
# executor.start_polling(dp)