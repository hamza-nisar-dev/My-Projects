
import telegram.ext
from paypalrestsdk import Payment
import telegram.ext
from telegram import LabeledPrice, ShippingOption
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt
import paypalrestsdk
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
from datetime import datetime
from paypalrestsdk import BillingPlan, ResourceNotFound
from paypalrestsdk import BillingAgreement
from datetime import datetime, timedelta
import sqlite3
from paypalrestsdk import BillingAgreement
from datetime import date
from dateutil import parser
import telegram.ext
from paypalrestsdk import Payment
import telegram.ext
from telegram import LabeledPrice, ShippingOption
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt
import paypalrestsdk
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
from datetime import datetime
from paypalrestsdk import BillingPlan, ResourceNotFound
from paypalrestsdk import BillingAgreement
from datetime import datetime, timedelta
import sqlite3
from paypalrestsdk import BillingAgreement
from datetime import date
from dateutil import parser
def start(update, context):
  conn = sqlite3.connect('kick.db')
  cursor = conn.cursor()
  cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
    conn = sqlite3.connect('kick.db')
    conn.execute("INSERT INTO COMPANY (ID,date,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),"0","0")) 
    conn.commit()
  keyboard = [[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 $20", callback_data='1')],[InlineKeyboardButton("🔑 Humans Crypto Free 🔑", url='https://t.me/humans_crypto')]]  
  text='<b>Welcome to Humans Crypto 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n✅ Quality signals \n✅ Weekly report\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply Click status.\n\nPlease select your subscription plan:'
  key=[["Plans","Status"],["Affiliation Programe"]]
  user = update.message.from_user
  usa=user.first_name
  reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
  user = update.message.from_user
  usa=user.first_name
  context.bot.send_message(chat_id=update.effective_user.id,text="Hey {}!".format(usa),reply_markup=reply_marku)
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,parse_mode=telegram.ParseMode.HTML)
  context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)

def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  if a=="1":
    keyboard = [[InlineKeyboardButton("Credit/Debit Card", callback_data='2')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    text= "Your benefits:\n✅ Humans Crypto Signals VIP (✅)\n\nPrice: 20 $\nBilling period: 1 Month\nBilling mode: recurring"
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup)
  elif a=="2":
    title = "Humans Crypto Signals"
    description = "🔑 1 MONTH VIP ACCESS 🔑"
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    provider_token = "350862534:LIVE:ZDNiYTBkZDM1ZDFk"
    currency = "USD"
    price = 20
    prices = [LabeledPrice("Humans Crypto Signals", price * 100)]
    c=context.bot.send_invoice(
       update.effective_user.id,  title, description, payload, provider_token, currency, prices
    )
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set pkg ='{}' where ID = '{}'".format("1",int(update.effective_user.id)))
    conn.commit()
    conn.close()
def main():
  updater = Updater("5378291523:AAETQQi6D4kZY1kU30H6cptHnD6R1XnSgmE", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CallbackQueryHandler(button))
#  dp.job_queue.run_repeating(callback_minute, 86400)
#  dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
#  dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
#  dp.add_handler(MessageHandler(Filters.regex('^(Plans|Status|Affiliation Program)$'), gender))
 
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()