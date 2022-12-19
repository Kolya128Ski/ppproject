import pytest
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from TEST.moked_bot import MockedBot


@pytest.fixture(scope='session')#настраиваем storage
async def storage():
    tmp_storage = MemoryStorage()
    try:
        yield tmp_storage
    finally:
        await tmp_storage.close()

@pytest.fixture()
def bot():
    bot = MockedBot()
    token = Bot.set_current(bot)
    try:
        yield bot
    finally:
        Bot.reset_current(token)


@pytest.fixture()
async def dispatcher():
    dp = Dispatcher()
    await dp.emit_startup()
    try:
        yield dp
    finally:
        await dp.emit_shutdown()