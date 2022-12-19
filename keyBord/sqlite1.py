# Создание инлайн клавиатуры


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

products_cb = CallbackData('pr', 'id', 'action')#шаблон для создания и отправки данных он будет являться экземпляром класса CfllbackData

# Импортируем кнопки инлайновские
def get_pr_ikb() -> InlineKeyboardMarkup:
    '''
    Эта функция служит для того, что бы была создана клавиатура под сообщением.
    :return: -> InlineKeyboardMarkup
    '''

    ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Просмотреть мои города', callback_data='get_all_pr')],[InlineKeyboardButton('Редактировать\Удалить/Добавить', callback_data='add_new_pr')]])

    return ikb
def get_cancel_kb():
    '''
     Эта функция служит для того, что бы была создана клавиатура из сообщений
    :return: -> ReplyKeyboardMarkup
    '''
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/cancel')]
    ], resize_keyboard=True)
    return kb

def edit_ikb(pr_id: int)->InlineKeyboardMarkup:
    '''
    Эта функция служит для того, что бы была создана клавиатура под сообщением
    :param pr_id: int
    :return: ->InlineKeyboardMarkup
    '''
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Редактировать город', callback_data=products_cb.new(pr_id, 'edit'))],
        [InlineKeyboardButton('Удалить город', callback_data=products_cb.new(pr_id, 'delete'))]

    ])
    return ikb
# import requests
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# btnBitcoin = InlineKeyboardButton(text="/Bitcoin", callback_data="cc/bitcoin")#cc=cripto curensy
# btnLitecoin = InlineKeyboardButton(text="/Litecoin", callback_data="cc/litecoin")#cc=cripto curensy
# btnDogecoin = InlineKeyboardButton(text="/Dogecoin", callback_data="cc/dogecoin")#cc=cripto curensy
#
# cripto_list = InlineKeyboardMarkup(row_width=1)
# cripto_list.insert(btnBitcoin)
# cripto_list.insert(btnLitecoin)
# cripto_list.insert(btnDogecoin)

#кнопки клавиатуры после добавления своего города

# b1 = KeyboardButton('/Добавить')
# b2 = KeyboardButton('/Удалить')
#
#
# sq_button_case = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)

