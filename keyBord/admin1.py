# Создание инлайн клавиатуры


import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnBitcoin = InlineKeyboardButton(text="/Bitcoin", callback_data="cc/bitcoin")#cc=cripto curensy
btnLitecoin = InlineKeyboardButton(text="/Litecoin", callback_data="cc/litecoin")#cc=cripto curensy
btnDogecoin = InlineKeyboardButton(text="/Dogecoin", callback_data="cc/dogecoin")#cc=cripto curensy

cripto_list = InlineKeyboardMarkup(row_width=1)
cripto_list.insert(btnBitcoin)
cripto_list.insert(btnLitecoin)
cripto_list.insert(btnDogecoin)





