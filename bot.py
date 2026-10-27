from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8242418418:AAFHsuGnQNUhyTbk6hCB7j7J38Zy-M6zvrk"   # ← BotFather token

# Question & answers
QUESTION = "KARTHIK YEDDI PUKODA?"
OPTIONS = {
    "red": "YEDDI HUKODU",
    "blue": "GANDU HUKODU",
    "green": "MANCHI HUKODU"
}

# Choose chesina tarvata pampalsina text & video
RESPONSE_TEXT = "YOUR WRONG VADU DHONGA PUKODU"
VIDEO_URL = "https://graph.org/file/08f07836530775bba87a4-a4774c61b67c442681.mp4"  # ← Nee video link pettu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(OPTIONS["red"], callback_data="red")],
        [InlineKeyboardButton(OPTIONS["blue"], callback_data="blue")],
        [InlineKeyboardButton(OPTIONS["green"], callback_data="green")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(QUESTION, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chosen = query.data
    chosen_text = OPTIONS.get(chosen, "Unknown")

    # 1. Text message
    await query.edit_message_text(text=f"Mee choice: {chosen_text}\n\n{RESPONSE_TEXT}")

    # 2. Video pampadam
    await context.bot.send_video(
        chat_id=query.message.chat_id,
        video=VIDEO_URL,
        caption=f"developed by VAMSI)"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot start ayyindi...")
    app.run_polling()

if __name__ == "__main__":
    main()
