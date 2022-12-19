#Создание кнопок на место клавиатуры

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#  , ReplyKeyboardRemove # from aiogram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('/Узнатьпогоду')
b2 = KeyboardButton('/Узнатьпогодувмоёмгороде')
b3 = KeyboardButton('/Cryptorates')

clientkaa = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

clientkaa.add(b1).add(b2).insert(b3)  #лучше всего row(b1, b2, b3)



