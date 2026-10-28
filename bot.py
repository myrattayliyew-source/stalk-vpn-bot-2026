import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]

keyboard = ReplyKeyboardMarkup(
    [
        ["🔑 Получить VPN-ключ"],
        ["💳 Тарифы", "ℹ️ Помощь"],
    ],
    resize_keyboard=True,
)

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "🛡️ STALK VPN\n\nВыбери действие:",
        reply_markup=keyboard,
    )

async def menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = update.message.text

    if text == "🔑 Получить VPN-ключ":
        reply = (
            "🔑 Выдача ключей пока настраивается.\n"
            "VPN-сервер ещё не подключён."
        )
    elif text == "💳 Тарифы":
        reply = "💳 Тарифы STALK VPN пока настраиваются."
    elif text == "ℹ️ Помощь":
        reply = "ℹ️ Выбери действие в меню."
    else:
        reply = "Используй кнопки меню."

    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
