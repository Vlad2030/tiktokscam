from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

backMenu_btn = KeyboardButton("◀️ В главное меню")
reviewBtn = InlineKeyboardMarkup(resize_keyboard=True).add(
    InlineKeyboardButton(
        "🚀 Отзывы!", url="t.me/tiktokgarant"
    )
)

# Меню выбора оплаты
qiwi_btn = KeyboardButton("🥝 QIWI")
btc_btn = KeyboardButton("📀 BITCOIN (НЕ ДОСТУПНО)")
card_btn = KeyboardButton(
    "💳 Банковская карта (ВРЕМЕННО НЕ ДОСТУПНО)"
)
paymentsMenu = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(qiwi_btn)
    .add(btc_btn)
    .add(card_btn)
    .add(backMenu_btn)
)

# Меню проверки оплаты
checkPay_btn = KeyboardButton("💎 Я оплатил")
cancelPay_btn = KeyboardButton("❌ Отмена")
checkPayMenu = (
    ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    .add(checkPay_btn)
    .add(cancelPay_btn)
)
