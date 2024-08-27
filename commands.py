from tokenize import group

import telegram.ext as ext
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telegram.ext import CallbackQueryHandler

from groups import groups
from users import users


# start
async def start_handler(update: telegram.Update, context: ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hi, {update.effective_sender.name}! I'm EmmaBot!~ Nice to meet you!")

start_command = ext.CommandHandler("start", start_handler, block=False)

# inline keyboard
list_user_keyboard = [InlineKeyboardButton("List Users", callback_data="list_users"), InlineKeyboardButton("List Groups", callback_data="list_groups")]

# list users or groups
async def list_handler(update: telegram.Update, context: ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What would you like to do?", reply_markup=InlineKeyboardMarkup.from_column(list_user_keyboard))

list_command = ext.CommandHandler("list", list_handler, block=False)

# callback handler to list users or groups
async def list_callback(update: telegram.Update, context: ext.ContextTypes.DEFAULT_TYPE):
    match update.callback_query.data:
        case "list_users":
            await context.bot.send_message(update.callback_query.message.chat.id, f"Users: {users}")
        case "list_groups":
            await context.bot.send_message(update.callback_query.message.chat.id,
                                   "Press any button to list users in that group.\nGroups:",
                                   reply_markup=InlineKeyboardMarkup.from_column(
                                       [InlineKeyboardButton(key, callback_data=f"group {key}") for key in groups.keys()]))
        case update.callback_query.data if "group" in update.callback_query.data:
            await context.bot.send_message(update.callback_query.message.chat.id,
                                   f"Users: {[user for user in groups[update.callback_query.data.split(" ")[1]]]}")
    await update.callback_query.answer()


list_handler = CallbackQueryHandler(list_callback, block=False)