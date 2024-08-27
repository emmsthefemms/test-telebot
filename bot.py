import telegram
import telegram.ext as ext
import logging
import os

from telegram.ext import MessageHandler

import commands

token = os.environ["testbot"]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# async def reply(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("nya!~ I'm EmmaBot!")

if __name__ == '__main__':
    application = ext.ApplicationBuilder().token(token).build()
    # application.add_handler(MessageHandler(ext.filters.ALL, reply, False))
    application.add_handler(commands.start_command)
    application.add_handler(commands.list_command)
    application.add_handler(commands.list_handler)
    application.run_polling()
    print("running")