from aiogram import Bot, Dispatcher, types

import data.env

bot = Bot(token=data.env.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)