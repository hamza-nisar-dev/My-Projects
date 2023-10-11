
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta
import sqlite3
from coinbase_commerce.client import Client
#CryptoNovaBot
API = ["52ce4b82-6739-494e-a953-d254f7343fd5"]
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
    
    keyboard = [[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 1 Month 🔑", callback_data='p1')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 6 Month 🔑", callback_data='p3')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) Lifetime 🔑", callback_data='p4')],[InlineKeyboardButton("💰 CryptoNova ® (Free) 💰", url='https://t.me/+hL9N96iCSXFlYzFk')]]  
    text='Welcome to CryptoNova ®\n\nPlease select your subscription plan:'
    key=[["Plans 🔑"],["STATUS 📌"]]

    user = update.message.from_user

    usaa=user.first_name
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    user = update.message.from_user
    usa=user.first_name
    context.bot.send_message(chat_id=update.effective_user.id,text="Hey {}!".format(usaa),reply_markup=reply_marku)
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,parse_mode=telegram.ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)


def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  client = Client(api_key=API[0])  
  if a=="p1"  or a=="p3" or a=="p4":
    if a=="p1":
        x=199
        y="1 Month"

    elif a=="p3":
        x=699 
        y="6 MONTHS"
    elif a=="p4":
        x=999
        y="LifeTime"
  
    keyboard = [[InlineKeyboardButton("Crypto", callback_data='b-{}'.format(x))]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    text= "Your benefits:\n✅ Crypto Nova  Signal ACCESS (✅)\n\nPrice: {} $\nBilling period: {}\nBilling mode: recurring".format(x,y)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup)
  
  
  elif a=="b-199" or a=="b-699" or a=="b-999":  
    if a=="b-199":
        pkg=1
        pr=199
    elif a=="b-699":
        pkg=3
        pr =699
    elif a=="b-999":
        pkg=4
        pr =999
    charge = client.charge.create(name='Crypto Nova Signal Bot',
                          description="Crypto Nova  ACCESS",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pr,
                             "currency": "USD"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,pkg)) 
    conn.commit()
    keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    c=context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below button to make payment",reply_markup=reply_markup)
    context.job_queue.run_once(callback_minut, 200, context=c)
  elif a=="1":      
        keyboard = [[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 1 Month 🔑", callback_data='p1')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 6 Month 🔑", callback_data='p3')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) Lifetime 🔑", callback_data='p4')],[InlineKeyboardButton("💰 CryptoNova ® (Free) 💰", url='https://t.me/+hL9N96iCSXFlYzFk')]]
        text='Welcome to CryptoNova ®\n\nPlease select your subscription plan:'
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
def gender(update, context):
  
    c=update.message.text
    if c=="Plans 🔑":
        
         
        keyboard = [[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 1 Month 🔑", callback_data='p1')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) 6 Month 🔑", callback_data='p3')],[InlineKeyboardButton("🔑 CryptoNova ® (VIP) Lifetime 🔑", callback_data='p4')],[InlineKeyboardButton("💰 CryptoNova ® (Free) 💰", url='https://t.me/+hL9N96iCSXFlYzFk')]]
        text='Welcome to CryptoNova ®\n\nPlease select your subscription plan:'
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
   
   
    elif c=="STATUS 📌":
        connection = sqlite3.connect("kick.db")  
        cursor = connection.execute("SELECT date FROM COMPANY where id='{}'".format(update.effective_user.id))
        for names in cursor:
            da=names[0]
        if da !="0":
           
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
            text='Your subscription will expire the:\n\n<b>{}</b>\n\n'.format(da)

            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
        else:
            keyboard = [[InlineKeyboardButton("ACTIVATE YOUR PLAN", callback_data='1')],[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
            text='Dear user, you do not have any active subscriptions at this time.\n\nTo activate your VIP ROOM subscription, select the "ACTIVATE YOUR PLAN" button 🔑\n\n\n'
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)

def callback_minut(context):
    job = context.job
    updat=job.context
    aa=updat['message_id']
    ab=updat['chat']['id']
    context.bot.delete_message(chat_id=ab,
                  message_id=aa)
def callback_minute(context: telegram.ext.CallbackContext):
    connection = sqlite3.connect("kick.db")  
    cursor = connection.execute("SELECT ID,date FROM COMPANY ")
    connection.close()
    for names in cursor:
        da=names[0]
        dy=names[1]
        try:
            x=datetime.today().strftime('%Y-%m-%d')
            a=str(dy) #date
            y=a.split(" ")
            y=y[0]
            if x>y:
                conn = sqlite3.connect("kick.db")  
                conn.execute("DELETE COMPANY  where ID = '{}'".format(int(da)))
                conn.commit()
                conn.close()
                print(da)
                vb=datetime.datetime.now().utcnow() + datetime.timedelta(minutes =2)
                try:
                    context.bot.kick_chat_member(chat_id=-1001323251186,user_id=int(da),until_date=vb)
                except:
                    pass
                context.bot.send_message(chat_id=str(da),text="you are removed from group. Click on below button to renew the service")            
            elif x==y:
              context.bot.send_message(chat_id=str(da),text="today is last date of your subsription. Update it otherwise you will be removed tomorrow\n\nClick on below button to renew the service")
        except:
          pass  

def main():
  updater = Updater("5355429117:AAHlnPrVKP2pxApPQHGwvkcDJUb8M2h96AI", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CallbackQueryHandler(button))
  dp.job_queue.run_repeating(callback_minute, 86400)
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(MessageHandler(Filters.regex('^(STATUS 📌|Plans 🔑|Change Language)$'), gender))
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()