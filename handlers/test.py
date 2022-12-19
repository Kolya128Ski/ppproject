import pytest

from unittest.mock import AsyncMock
from client import start_command

@pytest.mark.asyncio
async def test_start_handler():
    # test_mock = "test123"
    message_mock = AsyncMock(text='start')
    await start_command(message=message_mock)
    message_mock.answer.assert_called_with('Здравствуйте! Что Вы хотите узнать?')

# from unittest.async_case import pytest
# import requests
# import json
# def test_f():
#     requests.get = Mock()
#     requests.get.return_value = requests.Response()
#     requests.get.return_value._content = b'{"coord": {"lon": 37.6156, "lat": 55.7522}, "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}], "base": "stations", "main": {"temp": -3.58, "feels_like": -8.68, "temp_min": -4.19, "temp_max": -2.25, "pressure": 1021, "humidity": 91, "sea_level": 1021, "grnd_level": 1002}, "visibility": 10000, "wind": {"speed": 4, "deg": 263, "gust": 9.16}, "clouds": {"all": 99}, "dt": 1671181771, "sys": {"type": 2, "id": 2000314, "country": "RU", "sunrise": 1671170036, "sunset": 1671195375}, "timezone": 10800, "id": 524901, "name": "Moscow", "cod": 200}'
#     # f()
#
#     requests.get.assert_called_with('https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')


# @pytest.mark.asyncio
# async def test_some_asyncio_code():
#     res = await library.do_something()
#     assert b"expected result" == res



