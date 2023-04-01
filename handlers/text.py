import random

from aiogram import types

import data.config
import handlers.start
import keyboards.keyboard
import modules.loader
import text.messages


@modules.loader.dp.message_handler(content_types=["text"])
async def send_mes(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    comment: str = f"{user_id} {random.randint(1111, 5000)}"
    id_check = True if len(text) <= 11 and len(text) >= 6 else False

    match text:
        case "❌ Отмена":
            return await handlers.start.start_message(message)
        
        case "◀️ В главное меню":
            return await handlers.start.start_message(message)
        

        case "🥝 QIWI":
            return await message.answer(
                text=text.messages.qiwi_message.format(
                    data.config.QIWI_ACCOUNT,
                    comment
                ),
                reply_markup=keyboards.keyboard.checkPayMenu,
            )

        case "💳 Банковская карта (ВРЕМЕННО НЕ ДОСТУПНО)":
            return await message.answer(
                text.messages.card_message.format(data.config.CARD_NUMBER, comment),
                reply_markup=keyboards.keyboard.checkPayMenu,
            )

        case "📀 BITCOIN (НЕ ДОСТУПНО)":
            return await message.answer(
                text.messages.btc_message.format(data.config.BTC_ADDRESS),
                reply_markup=keyboards.keyboard.checkPayMenu,
            )

        case "💎 Я оплатил":
            return await message.answer(
                text.messages.post_pay_message,
                reply_markup=keyboards.keyboard.checkPayMenu,
            )
            

    if id_check:
        if not isinstance(text, int):
            return await message.answer("Вы ввели некорректный ID, нажмите /start для возврата")

        if text:
            sec_user_id = int(text)
            return await message.answer(
                text=f"Теперь оплатите нужную сумму!\nПосле успешной оплаты"
                     f"ользователю {sec_user_id} отправится приглашение,"
                     f"перейдя по которому он сможет загрузить товар",
                reply_markup=keyboards.keyboard.paymentsMenu,
            )