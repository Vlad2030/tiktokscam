from aiogram import types

import keyboards.keyboard
import modules.loader
import text.messages


@modules.loader.dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer(
        text.messages.start_message,
        reply_markup=keyboards.keyboard.reviewBtn
    )