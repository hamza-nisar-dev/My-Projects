import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt
import paypalrestsdk
from datetime import datetime
from paypalrestsdk import BillingAgreement
from datetime import datetime, timedelta
import sqlite3
from paypalrestsdk import BillingAgreement
from dateutil import parser
GEND= range(1)
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "AQZOPuRug5f8YVWnodKfKW66HagDEw-8I_F5r-8HI7zmkGB90RWi9IsEewH7zRzDPVcx7M02gD_uggIU",
  "client_secret": "EPnax0sjn4INvphP-kLGaRYVP3VxkMsDaF4itJBkJXe9dQ9jtyGPiC2WOPR-bz0FfyGANWNS1dgPsbx3" })
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

    user = update.message.from_user
    usa=user.first_name
    key=[["Plans 🔑"],["STATUS 📌"]]
    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Hey {}!".format(usa),reply_markup=reply_markup) 
    text='WELCOME TO BETTER WINNINGS BOT\n\nPLEASE SELECT YOUR SUBSCRIPTION PLAN:'
    keyboard = [[InlineKeyboardButton("🔑 1 MONTH VIP ACCESS 🔑  £11.99", callback_data='p1')],[InlineKeyboardButton("🔑 3 MONTH VIP ACCESS 🔑  £30.00", callback_data='p2')]] 
    reply_marku = reply_marku = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text=text 
                    ,reply_markup=reply_marku)
def cagree(pid):
 
    a=(datetime.now()+ timedelta(hours=1)).replace(microsecond=0).isoformat()
    a=a+"Z"
    billing_agreement = BillingAgreement({
        "name": "Better Winnings Bo",
        "description": "Agreement for Better Winnings Bo",
        "start_date": a,
        "plan": {
            "id": pid
        },
        "payer": {
            "payment_method": "paypal"
        }
    })
    if billing_agreement.create():
        for link in billing_agreement.links:
            if link.rel == "approval_url":
                approval_url = link.href
                return approval_url
    else:
        print(billing_agreement.error)

def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  print(a)
  if a=="p1" or a=="p2":
    if a=="p1":
        x=11.99
        y="1 Month"
    elif a=="p2":
        x=30.00
        y="3 MONTH"
   
  
    keyboard = [[InlineKeyboardButton("Paypal", callback_data='p-{}'.format(x))]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    text= "Your benefits:\n✅ BETTER WINNINGS VIP ACCESS ✅\n\nPrice: £{}\nBilling period: {}\nBilling mode: recurring".format(x,y)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup)
  
  elif a=="p-11.99" or a=="p-30.00":  
    if a=="p-11.99":
        pkg=1
        bs="P-7SV311048B408771BBY4YPQI"
    elif a=="p-30.00":
        pkg=2
        bs="P-5WW03328AF8816028BY5KELY"

    ad=cagree(bs)
    link=ad
    ass=ad.split("&token=")
    ass=ass[1].split("]")
    ass=ass[0].strip()
    conn = sqlite3.connect('paypal.db')
    conn.execute("INSERT INTO COMPANY (ID,ptoken ,pkg) \
        VALUES ('{}','{}','{}')".format(update.effective_user.id,ass,pkg))
    conn.commit()
    print(ass)
    print(ad)
    
    
    keyboard = [[InlineKeyboardButton("Make a Payment", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    c=context.bot.send_message(chat_id=update.effective_user.id,text="Please click the button below:" 
                    ,reply_markup=reply_markup)
    context.job_queue.run_once(callback_minut, 200, context=c)
  
  
def gender(update, context):
    c=update.message.text
    if c=="Plans 🔑":
            text='WELCOME TO BETTER WINNINGS BOT\n\nPLEASE SELECT YOUR SUBSCRIPTION PLAN:'
            keyboard = [[InlineKeyboardButton("🔑 1 MONTH VIP ACCESS 🔑  £11.99", callback_data='p1')],[InlineKeyboardButton("🔑 3 MONTH VIP ACCESS 🔑  £30.99", callback_data='p2')]]
            reply_marku = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=text 
                            ,reply_markup=reply_marku)
                
   
    elif c=="STATUS 📌":
        connection = sqlite3.connect("kick.db")  
        cursor = connection.execute("SELECT date FROM COMPANY where id='{}'".format(update.effective_user.id))
        for names in cursor:
            da=names[0]
        if da=="0":
            conn = sqlite3.connect('agreement.db')
            cursor = conn.cursor()
            cursor.execute("SELECT agree_id,pkg FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
            jobs = cursor.fetchall()
            print(jobs)
            if len(jobs) !=0:
                for nm in jobs:
                        billing_agreement = BillingAgreement.find(nm[0])
                        exp=billing_agreement['agreement_details']['next_billing_date']
                        da=parser.parse(exp)
        if da !="0":
                
            text='Your subscription will expire the:\n\n<b>{}</b>\n\n'.format(da)
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
        else:
            text='Dear user, you do not have any active subscriptions at this time.\n\nTo activate your VIP ROOM subscription, select the "PLAN" button 🔑\n\n\n'
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)

def callback_minut(context):
    job = context.job
    updat=job.context
    aa=updat['message_id']
    ab=updat['chat']['id']
    context.bot.delete_message(chat_id=ab,
                  message_id=aa)

def callb(context: telegram.ext.CallbackContext):
    conn = sqlite3.connect('agreement.db')
    cursor = conn.cursor()
    cursor.execute("SELECT agree_id,pkg FROM COMPANY") 
    jobs = cursor.fetchall()
    print(jobs)
    for nm in jobs:
            billing_agreement = BillingAgreement.find(nm[0])

            st=billing_agreement["state"]
            if st=="Cancelled" or st =="Suspended":
                conn = sqlite3.connect('paypal.db')  
                cursor = conn.execute("SELECT id FROM COMPANY where ptoken='{}'".format(nm[0]))
                for names in cursor:
                    ida=names[0]
                exp=billing_agreement['agreement_details']['next_billing_date']
                da=parser.parse(exp)
                conn = sqlite3.connect("kick.db")  
                conn.execute("UPDATE COMPANY set date='{}', where ID = '{}'".format(da,ida))
                conn.commit()
                conn.close()

def callback_minute(context: telegram.ext.CallbackContext):
    connection = sqlite3.connect("kick.db")
    cursor = connection.execute("SELECT ID,date FROM COMPANY ")
    for names in cursor:
        da=names[0]
        dy=names[1]
        if dy!="0":
            try:
                x=datetime.today().strftime('%Y-%m-%d')
                a=str(dy) #date
                y=a.split(" ")
                y=y[0]
                if x>y:
                    connection.execute("UPDATE COMPANY set date='0', pkg='0' where ID = '{}'".format(int(da)))
                    connection.commit()
                    print(da)
                    vb=dt.datetime.now().utcnow() + dt.timedelta(minutes =2)
                    try:
                        context.bot.kick_chat_member(chat_id=-1001573013348,user_id=int(da),until_date=vb)
                    except:
                        pass
                    context.bot.send_message(chat_id=str(da),text="you are removed from group. Click on below button to renew the service")
                elif x==y:
                 context.bot.send_message(chat_id=str(da),text="today is last date of your subsription. Update it otherwise you will be removed tomorrow\n\nClick on below button to renew the service")
            except:
                pass

def broadcast(update, context):
    bn=str(update.effective_user.id)
    if bn=="1370233655":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send your message to broadcast")
        return GEND
def gend(update, context):
    print(update)
    if update.message.photo:
        conn = sqlite3.connect('kick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM COMPANY") 
        jobs = cursor.fetchall()
        for names in jobs:
            ida=names[0]
            try:
                context.bot.send_photo(chat_id=ida,photo=update.message.photo[-1].file_id,caption=update.message.caption)
            except:
                pass
    else:
        conn = sqlite3.connect('kick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM COMPANY") 
        jobs = cursor.fetchall()
        for names in jobs:
            ida=names[0]
            try:
                context.bot.send_message(chat_id=ida,text=update.message.text)
            except:
                pass
    context.bot.send_message(chat_id=update.effective_user.id,text="Message send sucessfully.")
    return ConversationHandler.END
def main():
  updater = Updater("5456714021:AAGRaiRHwveqWyPRoh2uFx3HRA3yDkhAdOc", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CallbackQueryHandler(button))
  dp.job_queue.run_repeating(callback_minute, 86400)
  dp.job_queue.run_repeating(callb, 86400)
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(MessageHandler(Filters.regex('^(STATUS 📌|Plans 🔑)$'), gender))
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler('broadcast', broadcast)],
        states={

            GEND: [MessageHandler(Filters.text|Filters.photo, gend)],
  
        },
        fallbacks=[CommandHandler('broadcast', broadcast)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()