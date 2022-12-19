# Основной файл из которого запускается бот
# Импортируем все необходимое из библиотек и файлов для дальнейшего применения

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from venv.config import tg_bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data_base import sqlite_db
from aiogram.utils import executor
from create_bot import dp

storage = MemoryStorage()
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot, storage=storage)



async def on_startup(_):
    '''
    Запускает бота и активирует базу данных
    :return:->>'Бот в онлайне', 'Подключение к базе выполнено'
    '''
    await sqlite_db.dp_connect()
    print('Бот в онлайне')
    # sqlite_db.sqlite_start()
    print('Подключение к базе выполнено')

# Связываем хендлеры.
from handlers import admin,client,other


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)

#Для постоянного отслеживания и пропуска ранних сообщений
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)














# 1 что я делаю. Устанавливая библеотеку Requests

