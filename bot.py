from aiogram import Bot, Dispatcher, executor, types
import logging
import random

import config
import messages as mes
import keyboards as kb

# Подключаем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GARANTBOT')

# Авторизуем бота
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message):
	await message.answer(mes.start_message, reply_markup=kb.reviewBtn)

@dp.message_handler(content_types=["text"])
async def send_mes(message: types.Message):
	user_id = message.from_user.id
	text = message.text

	if text == '❌ Отмена' or text == '◀️ В главное меню':
		await start_message(message)
		return
	
	if text == '🥝 QIWI':
		comment = str(user_id) + '_' + str(random.randint(1111, 5000))
		await message.answer(mes.qiwi_message.format(config.QIWI_ACCOUNT, comment), reply_markup=kb.checkPayMenu)
		return
	
	if text == '💳 Банковская карта (ВРЕМЕННО НЕ ДОСТУПНО)':
		comment = str(user_id) + '_' + str(random.randint(11111, 99999))
		await message.answer(mes.card_message.format(config.CARD_NUMBER, comment), reply_markup=kb.checkPayMenu)
		return

	if text == '📀 BITCOIN (НЕ ДОСТУПНО)':
		await message.answer(mes.btc_message.format(config.BTC_ADDRESS), reply_markup=kb.checkPayMenu)
		return

	if text == '💎 Я оплатил':
		await message.answer(mes.post_pay_message, reply_markup=kb.checkPayMenu)
		return

	if len(text) <= 11 and len(text) >= 6:
		try:
			sec_user_id = int(text)
			await message.answer(f'Теперь оплатите нужную сумму!\nПосле успешной оплаты пользователю {sec_user_id} отправится приглашение, перейдя по которому он сможет загрузить товар', reply_markup=kb.paymentsMenu)
		except Exception as e:
			await message.answer('Вы ввели некорректный ID')
	else:
		await message.answer('Вы ввели некорректный ID или Неизвестная команда, нажмите /start для возврата')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)