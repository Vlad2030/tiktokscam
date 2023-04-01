from aiogram import executor

import handlers.start
import handlers.text
import modules.loader
import utils

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=modules.loader.dp,
        skip_updates=True,
        on_startup=utils.on_startup,
        on_shutdown=utils.on_shutdown,
    )
