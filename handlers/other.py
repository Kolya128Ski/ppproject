# Documentation

#1 Устанавливаем библиотеку requests именно благодаря ей будем получать данные погоды
#2 Создаем запрос спомощью этой библиотеке
#3 Создаем функцию, которая принимает 2 параметра
#4 В блоке try мы будем обрабатывать наш запрос, а если вылезет ошибка, то будем вызывать exept, который напишет 'Проверте пожалуйста, существует ли такой город'
#5 В переменной r формируем наш запрос
#6 Затем вытаскиваем, то что нам нужно
#7 Внесем разнообразие, те создадим словарь(code_to_smile)
#8 Импортируем все самое необходимое



from aiogram import types, Dispatcher
import requests
import datetime
from venv.config import open_weather_token
from venv.create_bot import dp
# @dp.message_handler()
async def get_message(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"

    }
###test moc
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json() # Модуль json позволяет кодировать и декодировать данные в удобном формате.
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри, что происходит за окном!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]) - datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C°{wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nСкорость ветра: {wind}м/с\nВосход солнца: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
              f"Приятного дня!"
              )

    except:
        await message.reply('Проверте пожалуйста, существует ли такой город')

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(get_message)