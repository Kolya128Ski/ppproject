# Основной файл с хендлерами. Именно в этом файле прописываем машину состояний и много другое.
# Импортируем все необходимое
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from venv.config import tg_bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
from aiogram import types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#from venv.create_bot import dp,bot
from venv.create_bot import dp, bot
from keyBord import clientkaa
from keyBord import get_pr_ikb, products_cb, get_cancel_kb, edit_ikb
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from venv.create_bot import dp
from aiogram import types
from keyBord import get_pr_ikb, products_cb
from data_base import sqlite_db

dp = Dispatcher(bot, storage=storage)



async def show_all_pr(callback: types.CallbackQuery, pr: list) -> None:#в данном случае pr является списком кортежей
    '''
    В данной функции реализуется вывод фотографии вместе с названием города
    :param callback: types.CallbackQuery
    :param pr: list
    :return: None
    '''
    for prod in pr:
        await bot.send_photo(chat_id=callback.message.chat.id, photo=prod[2], caption=prod[1], reply_markup=edit_ikb(prod[0]))



# from keyBord.sqlite1 import ikb
from keyBord import sqlite1
storage = MemoryStorage()
#Создание класса
class FSMma(StatesGroup):
    title = State()
    photo = State()
    # name = State()

#не забудь импортировать в будущем dp из config
# @dp.message_handler(commands='Узнатьпогодувмоёмгороде', state=None)ccc
async def fsm_start(message: types.Message):
    '''
    Данная функция принимает сообщзение и отвечает
    :param message: types.Message
    :return: message
    '''
    # await FSMma.title.set()#запуск машины состояний
    await message.reply("Нажмите на одну из кнопок", reply_markup=get_pr_ikb())#ответ на сообщение

async def close_command(message: types.Message, state=FSMContext):
    '''
        Данная функция принимает сообщзение и отвечает и запускается машина состояний
        :param message: types.Message
        :state: FSMContext
        :return: message
        '''
    if state is None:
        return

    # await state.finish()
    await message.answer('Вы вернулись',

                         reply_markup=clientkaa)

# @dp.callback_query_handler(text='get_all_pr')#обработчик, который обрабатывает
async def cb_get_all_pr(callback: types.CallbackQuery):
    '''
        Данная функция принимает сообщзение и отвечает
        :param message: types.Message
        :return: message
        '''
    pr = await sqlite_db.get_all_pr()

    if not pr:
        await callback.message.answer("Ваших городов пока нет")
        return await callback.answer()#завершаем наш запрос
    # await callback.message.answer(pr)
    # await callback.message.answer(pr)
    await show_all_pr(callback, pr)#в данной функции мы передаем запрос от телеграмма, когда человек нажимает на кнопку. мы его здесь обработаем
    await callback.answer()

# @dp.callback_query_handler(command="Посмотреть мои города")
async def cb_add_new_pr(callback: types.CallbackQuery) -> None:
    '''
        Данная функция принимает сообщзение и отвечает
        :param message: types.Message
        :return: message
        '''
    await callback.message.delete()
    await callback.message.answer('Отправь название города', reply_markup=get_cancel_kb())
    await FSMma.title.set()#устанавливаем состояние для нашего алгоритма

    # sqlite_db.create_new_pr()
    #ecnfyfdkbdftv cjcjzybt(важно)
async def handle_title(message: types.Message, state: FSMContext) -> None:
    '''
        Данная функция принимает сообщзение и отвечает
        :param message: types.Message
        :return: message
        '''
    async with state.proxy() as data:#тут мы работаем с контекстом(сохраняем фотографию)data будет являться словарем, который хранит значение
        '''
            Данная функция принимает сообщзение и отвечает
            :param message: types.Message
            :return: message
            '''
        data['title']=message.text

    await message.reply('Отправь фотогрфию города')
    await FSMma.next()


# @dp.message_handler(lambda message: not message.photo, state=FSMma.photo)#проверка является ли фотография фотографией
async def check_photo(message: types.Message):
    '''
        Данная функция принимает сообщзение и отвечает
        :param message: types.Message
        :return: message
        '''
    await message.reply('Это не фотография')

# @dp.message_handler(content_types=["photo"], state=FSMma.photo)
async def handle_photo(message: types.Message, state: FSMContext) -> None:#именно тут будет(в этой функции) завершатся состояние
    '''
        Данная функция принимает сообщзение и отвечает
        :param message: types.Message
        :return: message
        '''
    async with state.proxy() as data:#тут мы работаем с контекстом(сохраняем фотографию)data будет являться словарем, который хранит значение
        data['photo']=message.photo[0].file_id

    await sqlite_db.create_new_pr(state)
    await message.reply('Я запомнил Ваш город. Спасибо!')

    await state.finish()


products_cb.filter(action='delete')
async def del_pr(callback: types.CallbackQuery, callback_data: dict):#dictionary types
    '''
    Данная функция удаляет из базы фотографию и название города
    :param callback: types.CallbackQuery
    :param callback_data: dist
    :return:
    '''
    await sqlite_db.delete_pr(callback_data['id'])

    await callback.message.reply('Успешно удалён')
    await callback.answer()

# @dp.message_handler(state = FSMma.name)
async def load_name(message: types.Message, state: FSMContext):
    '''
        Данная функция сохраняет себя и название нового города
        :param callback: types.CallbackQuery
        state: FSMContext
        :return: message
        '''
    async with state.proxy() as data:
        data['name'] = message.text
        #воткнуть базу данных и сбросить состояния
        await FSMma.next()
        await message.reply("Я запомнил Ваш город. Спасибо!", reply_markup=get_pr_ikb())
        #добавить фото, айди и название города
        await sqlite_db.sql_add_command(state)
        await state.finish()

# @dp.message_handler(commands=['start'])

# @dp.message_handler(commands=['start'])       #если в чат кто-то написал это событие будет отображено
async def start_command(message: types.Message):  # это специальная асинхронная
    '''
    Принимает и возвращает сообщение
    :param message: message
    :return: message
    '''
    await bot.send_message(message.from_user.id, 'Здравствуйте! Что Вы хотите узнать?', reply_markup=clientkaa)  # Бот отвечает на наше сообщение /start


# @dp.message_handler(commands=['Погода'])       #если в чат кто-то написал это событие будет отображено
async def w_command(message: types.Message):  # это специальная асинхронная
    '''
        Принимает и возвращает сообщение
        :param message: message
        :return: message
        '''
    await bot.send_message(message.from_user.id, 'Здравствуйте! Введите город, в котором хотите узнать погоду', reply_markup=clientkaa)


# @dp.message_handler(lambga message: 'шутки'in message.text)
async def joke_command(message: types.Message):
    '''
    Принимает и возвращает сообщение
    :param message: message
    :return: message
    '''


    await bot.send_message(message.from_user.id, 'В сторону шутки. Я погоду предсказываю!', reply_markup=clientkaa)

#pytest-asyncio
# @dp.message_handler(commands=['Любимые города'])
async def like_command(message: types.Message):
    '''
        Принимает и возвращает сообщение
        :param message: message
        :return: message
        '''
    await message.answer('Как только вы добавите ваш город, он будет отобржатся здесь.', reply_markup=clientkaa)
    await message.answer('Введите Ваш город')

# запускаем хендлер
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(w_command, commands=['Узнатьпогоду'])
    dp.register_message_handler(fsm_start, commands=['Узнатьпогодувмоёмгороде'], state=None)
    dp.register_message_handler(handle_title, state=FSMma.title)
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=FSMma.photo)
    dp.register_message_handler(handle_photo, content_types=["photo"], state=FSMma.photo)
    dp.register_callback_query_handler(cb_get_all_pr, text='get_all_pr')
    dp.register_callback_query_handler(cb_add_new_pr, text='add_new_pr')
    dp.register_message_handler(load_name, state=FSMma.title)
    dp.register_callback_query_handler(del_pr, products_cb.filter(action='delete'))
    dp.register_message_handler(close_command, commands=['cancel'], state='*')
    dp.register_message_handler(joke_command, commands=['Cryptorates'])
    # dp.register_message_handler(like_command, lambga message: 'шутки'in message.text))
