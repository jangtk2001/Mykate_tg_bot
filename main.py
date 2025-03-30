
import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

def handle_message(update, context):
    user_text = update.message.text
    response = f"Kate 說：你剛剛說了『{user_text}』對吧？我記下來囉。"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
