import telegram.ext
import telegram.ext
from telegram import LabeledPrice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt
from datetime import datetime, timedelta
import sqlite3
from datetime import date
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
    ref_id = update.message.text
    ref_id=ref_id.split()
    if len(ref_id) > 1:
            asf=str(ref_id[1]).strip()
            print(update.effective_user.id)
            connection = sqlite3.connect("sql.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
            jobs = cursor.fetchall()
            if len(jobs) ==0:
                conn = sqlite3.connect('sql.db')
                conn.execute("INSERT INTO COMPANY (ID,Trx,exp,tref,balance,refby,amount) \
                    VALUES ({}, '{}','{}','{}','{}','{}','{}')".format(update.effective_user.id,"0","0","0","0",asf,"0"))
                conn.commit()
                conn.close()
                conn = sqlite3.connect('sql.db')
                cursor = conn.execute("SELECT ID,tref from COMPANY where ID={}".format(int(asf)))
                conn.commit() 
                for row in cursor:
                    bn=int(row[1])
                    bn=bn+1
                    cursor = conn.execute("UPDATE COMPANY set tref='{}' where ID='{}' ".format(bn,asf))
                    conn.commit() 
    else:
            connection = sqlite3.connect("sql.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
            jobs = cursor.fetchall()
            if len(jobs) ==0:
                conn = sqlite3.connect('sql.db')
                conn.execute("INSERT INTO COMPANY (ID,Trx,exp,tref,balance,refby,amount) \
                    VALUES ({}, '{}','{}','{}','{}','{}','{}')".format(update.effective_user.id,"0","0","0","0","0","0"))
                conn.commit()
                conn.close()
    keyboard = [[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 $59", callback_data='1')],[InlineKeyboardButton("🔑 Humans Crypto Free 🔑", url='https://t.me/humans_crypto')]]  
    text='<b>Welcome to Humans Crypto 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n✅ Quality signals \n✅ Weekly report\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply Click status.\n\nPlease select your subscription plan:'
    key=[["Plans 🔑","STATUS 📌"],["Affiliation Program"]]
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
    text= "Your benefits:\n✅ Humans Crypto Signals VIP (✅)\n\nPrice: 59 $\nBilling period: 1 Month\nBilling mode: recurring"
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup)
  elif a=="2":
    title = "Humans Crypto Signals"
    description = "🔑 1 MONTH VIP ACCESS 🔑"
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    provider_token = "350862534:LIVE:ZDNiYTBkZDM1ZDFk"
    currency = "USD"
    price = 59
    prices = [LabeledPrice("Humans Crypto Signals", price * 100)]
    c=context.bot.send_invoice(
       update.effective_user.id,  title, description, payload, provider_token, currency, prices
    )
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set pkg ='{}' where ID = '{}'".format("1",int(update.effective_user.id)))
    conn.commit()
    conn.close()
  elif a== '69':

    connection = sqlite3.connect("sql.db")  
    cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
    for names in cursor:
        da=float(names[2]) 
        if da >=50:
            context.bot.send_message(chat_id=update.effective_user.id,text="Send your wallet address")
        else:
            context.bot.send_message(chat_id=update.effective_user.id,text="Your balance is less than 50 USDT")
  elif a=='6ac':
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("Amount: ")
        df=df[1]
        df=df.strip()
        df=df.split("UserID: ")
        df=df[0]
        df=df.strip()
        dd=cc.split("UserID: ")
        dd=dd[1]
        df=float(df)
        connection = sqlite3.connect("sql.db")  
        cursor = connection.execute("SELECT balance FROM COMPANY where id={}".format(dd))
        for names in cursor:
            da=float(names[0]) 
            da=da-df
            conn = sqlite3.connect('sql.db')
            conn.execute("UPDATE COMPANY set balance='{}' where ID = {}".format(da,dd))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=dd,text="Withdrawl Request has been accepted by the admin. Check your Wallet")
        context.bot.send_message(chat_id=update.effective_user.id,text="Withdrawl Request has been accepted")
  elif a=='6re':
        c=update.callback_query.message.message_id
        cc=update.callback_query.message.text
        d=cc
        df=cc.split("Amount: ")
        df=df[1]
        df=df.strip()
        df=df.split("UserID: ")
        df=df[0]
        df=df.strip()
        dd=cc.split("UserID: ")
        dd=dd[1]

        context.bot.send_message(chat_id=dd,text="Withdrawl Request has been rejected by the admin. \n Send request again, Please send valid wallet address")
        context.bot.send_message(chat_id=update.effective_user.id,text="Withdrawl Request has been rejected")
def vbnm(update,context):
    connection = sqlite3.connect("sql.db")  
    cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        da=float(names[2]) 
        if da >=50:
            msg=update.message.text
            connection = sqlite3.connect("sql.db")  
            cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
            for names in cursor:
                da=float(names[1]) 
                keyboard =[[InlineKeyboardButton("Accept", callback_data='6ac'),InlineKeyboardButton("Reject", callback_data='6re')]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
                context.bot.send_message(chat_id=5181149016,text="Withdrawal Reqest:\nWallet Address: {}\nAmount: {}\nUserID: {}".format(msg,names[2],update.effective_user.id),reply_markup=reply_markup)
            context.bot.send_message(chat_id=update.effective_user.id,text="Withdrawl Request sent",reply_markup=reply_markup)
def gender(update, context):
    c=update.message.text
    if c=="Plans 🔑":
        keyboard = [[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 $59", callback_data='1')],[InlineKeyboardButton("🔑 Humans Crypto Free 🔑", url='https://t.me/humans_crypto')]]  
        text='<b>Welcome to Humans Crypto 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n✅ Quality signals \n✅ Weekly report\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply Click status.\n\nPlease select your subscription plan:'
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
    elif c=="Affiliation Program":
        connection = sqlite3.connect("sql.db")  
        cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
        for names in cursor:
         da=names[1]  
        ab='https://t.me/humans_crypto_bot?start={}'.format(str(update.effective_user.id))
        vfg="Your Refferal Link: {}\nTotal Refferals: {}\nTotal Referral Balance: {}USDT".format(ab,da,names[2])
        keyboard =[[InlineKeyboardButton("Withdraw", callback_data='69')]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
        context.bot.send_message(chat_id=update.effective_user.id,text=vfg,reply_markup=reply_markup)
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        query.answer(ok=True)
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
                        context.bot.kick_chat_member(chat_id=-1001588953161,user_id=int(da),until_date=vb)
                    except:
                        pass
                    context.bot.send_message(chat_id=str(da),text="you are removed from group. Click on below button to renew the service")            
                elif x==y:
                 context.bot.send_message(chat_id=str(da),text="today is last date of your subsription. Update it otherwise you will be removed tomorrow\n\nClick on below button to renew the service")
            except:
             pass  
def successful_payment_callback(update, context):
    b=b = date.today() + timedelta(days=30)
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set date='{}' where ID = '{}'".format(b,int(update.effective_user.id)))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('sql.db')
    cursor = conn.execute("SELECT refby from COMPANY where ID= {}".format(update.effective_user.id))
    for names in cursor:
        asf=names[0]
        cursor = conn.execute("SELECT balance from COMPANY where ID={}".format(int(asf)))
        conn.commit() 
        for row in cursor:
            bn=float(row[0])
            bn=bn+20
            cursor = conn.execute("UPDATE COMPANY set balance='{}' where ID='{}' ".format(bn,asf))
            conn.commit() 
    exp=dt.datetime.now().utcnow() + dt.timedelta(days=7)
    c=context.bot.createChatInviteLink(chat_id= -1001588953161, expire_date=exp,member_limit=1)
    link=c['invite_link']
    keyboard = [[InlineKeyboardButton("Humans Crypto Premium", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Thank you for your payment\n.Please click the button below to join Channel" 
            ,reply_markup=reply_markup)
def main():
  updater = Updater("5378291523:AAETQQi6D4kZY1kU30H6cptHnD6R1XnSgmE", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CallbackQueryHandler(button))
  dp.job_queue.run_repeating(callback_minute, 86400)
  dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
  dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
  dp.add_handler(MessageHandler(Filters.regex('^(Plans 🔑|STATUS 📌|Affiliation Program)$'), gender))
  dp.add_handler(MessageHandler(Filters.text, vbnm))
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()