#В данной папке находится код, который применяется в папке other(там уже все прописано)


from pprint import pprint
import datetime
from config import open_weather_token
import requests


def get_weather(city, open_weather_token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"Погода в городе: {city}\nТемпература: {cur_weather}C\n"
              f"Влажность: {humidity}%\nСкорость ветра: {wind}\n"
              f"Успехов!!!"
        )

    except Exception as ex:
        print(ex)
        print('Проверте, существует ли такой город')

def main():
    sity = input("Введите город, в котором хотите узнать погоду:")
    get_weather(sity, open_weather_token)

if __name__=='__main__':
    main()

