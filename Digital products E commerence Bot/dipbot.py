import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

def start(update,context):
    
    keyboard =[[InlineKeyboardButton("Add New Token", callback_data="add_token")],[InlineKeyboardButton("Change Token settings", callback_data="token_settings")],[InlineKeyboardButton("Advertise on Buy the Dip", callback_data="advertisement")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Chose one of the following options",reply_markup=reply_markup)

def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    c=update.callback_query.message.message_id
    if a== 'add_token':
        keyboard =[[InlineKeyboardButton("Eth", callback_data="chain-eth")],[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please Chose one of the following chains:",reply_markup=reply_markup)
    
    elif "chain" in a:
      a=a.split("chain-")
      chain=a[1]
      keyboard =[[InlineKeyboardButton("Uniswap v2", callback_data="dex-uni")],[InlineKeyboardButton("Sushiswap", callback_data="dex-sush")],[InlineKeyboardButton("Shibaswap", callback_data="dex-shib")],[InlineKeyboardButton("Degenswap", callback_data="dex-degen")],[InlineKeyboardButton("Pancake", callback_data="dex-pan")],[InlineKeyboardButton("X7Finance", callback_data="chain-x7")],[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="Please Chose Your Dex:",reply_markup=reply_markup)
    elif a=="main_menu":
      keyboard =[[InlineKeyboardButton("Add New Token", callback_data="add_token")],[InlineKeyboardButton("Change Token settings", callback_data="token_settings")],[InlineKeyboardButton("Advertise on Buy the Dip", callback_data="advertisement")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="Please Chose one of the following options",reply_markup=reply_markup)
       
    elif "dex" in a:
      a=a.split("dex-")
      dex=a[1]
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="You choose {} Dex\n\nPlease send your token address".format(dex))
   
    


def main():
  updater = Updater("1919009832:AAHiauPUWVHGQ2ZAVPolfUepTPV0MaKDVwE", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CallbackQueryHandler(button))
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()