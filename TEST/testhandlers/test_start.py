from unittest.mock import AsyncMock
import pytest
from aiogram.dispatcher import FSMContext

from handlers.client import start_command, cb_add_new_pr
from keyBord import clientkaa


@pytest.mark.asyncio
async def test_start_command_handlers():
    message = AsyncMock()
    await start_command(message)

    message.answer.assert_called_with('Здравствуйте! Что Вы хотите узнать?', reply_markup=clientkaa)




# @pytest.mark.asyncio
# async def test_start_cb_add_new_pr_handler(storage, bot):
#     call = AsyncMock()
#     state = FSMContext(
#         bot=bot,
#         storage=storage
#         key=StorageKey(bot_id=bot.id, user_id=123, chat_id=123)
#     )
#     await cb_add_new_pr(call=call, state=FSMContext)

