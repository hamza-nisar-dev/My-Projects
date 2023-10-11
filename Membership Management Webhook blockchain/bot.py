import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import KeyboardButton
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from datetime import date
from dateutil.relativedelta import relativedelta
import sqlite3
import random
import string
from pyCoinPayments import CryptoPayments
API_KEY = '818c36f7f454fc9c8c2d3a624805dca1f90014bedffd93187632c95a87a4d3f4'
API_SECRET = 'c400B8c1C845eb78962074e29c2d9a244B074cff29540bD8E970544AE69433Eb'
IPN_URL = 'http://t.me/CPMBOT_BOT'
BUTTON= range(1) 

def start(update, context):
    connection = sqlite3.connect("sql.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        conn.execute("INSERT INTO COMPANY (ID,Trx,exp) \
            VALUES ({}, '{}','{}')".format(update.effective_user.id,"0","0"))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('sql1.db')
        conn.execute("INSERT INTO COMPANY (ID,exp) \
            VALUES ({}, '{}')".format(update.effective_user.id,"0"))
        conn.commit()
        conn.close()
    keyboard = [[InlineKeyboardButton("VIP SPOT", callback_data='11')],[InlineKeyboardButton("VIP FUTUROS", callback_data='22')],[InlineKeyboardButton("VIP ELITE", callback_data='33')],[InlineKeyboardButton("VIP spot+ VIP Futuros", callback_data='33a')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    user = update.message.from_user
    usa=user.first_name
    msfa='hey '+usa
    context.bot.send_message(chat_id=update.effective_user.id,text=msfa)
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON

def button(update, context):
  query = update.callback_query
  a=query.data
  if a== '50' or a=='25' or a=="70"or a=='125' or a=="200" or a== '48' or a=='95' or a=="120"or a=='210' or a=="360" or a== '50' or a=='100' or a=="135"or a=='240' or a=="450":
    query.answer()
    ham="USDT.ERC20"
    conn = sqlite3.connect('sql.db')
    cursor = conn.execute("SELECT Trx from COMPANY where ID= {}".format(update.effective_user.id))
    for names in cursor:
        inv=names[0]
    if inv !='0':
        client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
        post = {
            'txid' : inv,} 
        transactionInfo = client.getTransactionInfo(post) 
        c=transactionInfo['status']
        if c==2:
            keyboard = [[InlineKeyboardButton("Trading Signal Channel", url="https://t.me/joinchat/xUwPOWpj-Lc3YWNk")],
                [InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]    
            reply_markup = InlineKeyboardMarkup(keyboard)
            conn = sqlite3.connect('sql.db')
            cursor = conn.execute("SELECT exp from COMPANY where ID= {}".format(update.effective_user.id))
            for names in cursor:
               inv=names[0]
            conn = sqlite3.connect('sql.db')
            conn.execute("UPDATE COMPANY set Trx='0' where ID = {}".format(update.effective_user.id))
            conn.commit()
            conn.close()
            conn = sqlite3.connect('sql1.db')
            conn.execute("UPDATE COMPANY set exp='{}' where ID = '{}".format(inv,update.effective_user.id))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below links to join paid channels",reply_markup=reply_markup)                       
            return BUTTON
    create_transaction_params = {
     'amount' : int(a),
     'currency1' : 'USD',
     'currency2' : ham,
     'buyer_email': 'rhamza126@gmail.com'
           }
    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
    transaction = client.createTransaction(create_transaction_params)
    print(transaction)
    if transaction['error'] == 'ok':
        am= transaction['amount'] 
        ad=transaction['address']
        url=transaction['checkout_url']

    post = {
        'txid' : transaction['txn_id'],}
    post=post['txid']
    keyboard = [[InlineKeyboardButton("I have Paid", callback_data='9')],[InlineKeyboardButton("Make a Payment", url=url)],
                [InlineKeyboardButton("🔙 Cancel", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=+1)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}' where ID = {}".format(post,dat,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Amount: {} {}\n To Address:\n{}\n\n""Or click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation  and then click on 'I have Paid' button".format(am,ham,ad),reply_markup=reply_markup)
    return BUTTON
     

  elif a== '9':
    query.answer()
    conn = sqlite3.connect('sql.db')
    cursor = conn.execute("SELECT Trx from COMPANY where ID= {}".format(update.effective_user.id))
    for names in cursor:
        inv=names[0]
    if inv !='0':
        client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
        post = {
            'txid' : inv,}
        transactionInfo = client.getTransactionInfo(post) 
        c=transactionInfo['status']
        if c==2:
            keyboard = [[InlineKeyboardButton("Main Trading Signal Channel", url="https://t.me/joinchat/wi52yUl2FQ9kNWFk")],[InlineKeyboardButton("Chat and Trade support channel", url="https://t.me/joinchat/TGDbcHqGMm99pnTk")],[InlineKeyboardButton("market scanner channel", url="https://t.me/joinchat/R4nToekkL124bqkf")],[InlineKeyboardButton("Newsfeed Channel", url="https://t.me/joinchat/TG3UgXLZDve5_qfD")],
                [InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]    
            reply_markup = InlineKeyboardMarkup(keyboard)
            conn = sqlite3.connect('sql.db')
            cursor = conn.execute("SELECT exp from COMPANY where ID= {}".format(update.effective_user.id))
            for names in cursor:
               inv=names[0]
            conn = sqlite3.connect('sql.db')
            conn.execute("UPDATE COMPANY set Trx='0' where ID = {}".format(update.effective_user.id))
            conn.commit()
            conn.close()
            conn = sqlite3.connect('sql1.db')
            conn.execute("UPDATE COMPANY set exp='{}' where ID = {}".format(inv,update.effective_user.id))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below links to join paid channels",reply_markup=reply_markup)                       
            return BUTTON
        elif c==0:
            
            context.bot.send_message(chat_id=update.effective_user.id,text="No transcation found yet. comeback later")                       
            return BUTTON
        elif c==1:
            context.bot.send_message(chat_id=update.effective_user.id,text="Your transcation is pending please come back again later")                       
            return BUTTON
        else:
            keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_user.id,text="error in transcation cotact admin",reply_markup=reply_markup)                       
            return BUTTON
    else:
        context.bot.send_message(chat_id=update.effective_user.id,text="No transcation found yet.")                       
        return BUTTON

  elif a== '6':
    query.answer()
    keyboard = [[InlineKeyboardButton("VIP SPOT", callback_data='11')],[InlineKeyboardButton("VIP FUTUROS", callback_data='22')],[InlineKeyboardButton("VIP ELITE", callback_data='33')],[InlineKeyboardButton("VIP spot+ VIP Futuros", callback_data='33a')]] 
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON
    
  elif a== '11':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (25 USDT)", callback_data='25')],[InlineKeyboardButton("2 MESES (50 USDT)", callback_data='50')],[InlineKeyboardButton("3 MESES (70 USDT)", callback_data='70')],[InlineKeyboardButton("6 MESES (125 USDT)", callback_data='125')],[InlineKeyboardButton("12 MESES (200 USDT)", callback_data='200')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '22':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (25 USDT)", callback_data='25')],[InlineKeyboardButton("2 MESES (50 USDT)", callback_data='50')],[InlineKeyboardButton("3 MESES (70 USDT)", callback_data='70')],[InlineKeyboardButton("6 MESES (125 USDT)", callback_data='125')],[InlineKeyboardButton("12 MESES (200 USDT)", callback_data='200')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '33':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (48 USDT)", callback_data='48')],[InlineKeyboardButton("2 MESES (95 USDT)", callback_data='95')],[InlineKeyboardButton("3 MESES (120 USDT)", callback_data='120')],[InlineKeyboardButton("6 MESES (210 USDT)", callback_data='210')],[InlineKeyboardButton("12 MESES (360 USDT)", callback_data='360')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '33a':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (48 USDT)", callback_data='48')],[InlineKeyboardButton("2 MESES (95 USDT)", callback_data='95')],[InlineKeyboardButton("3 MESES (120 USDT)", callback_data='120')],[InlineKeyboardButton("6 MESES (210 USDT)", callback_data='210')],[InlineKeyboardButton("12 MESES (360 USDT)", callback_data='360')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '44':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (50 USDT)", callback_data='50')],[InlineKeyboardButton("2 MESES (100 USDT)", callback_data='100')],[InlineKeyboardButton("3 MESES (10% OFF) (135 USDT)", callback_data='135')],[InlineKeyboardButton("6 MESES (20% OFF) (240 USDT)", callback_data='240')],[InlineKeyboardButton("12 MESES (35% OFF) (450 USDT)", callback_data='450')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
def callback_minut(context):
  try:
    connection = sqlite3.connect("sql1.db")  
    cursor = connection.execute("SELECT id,exp FROM COMPANY ")
    for names in cursor:
      da=names[1]
      idd=names[0]
    if da !="0":
        x=date.today()
        date=str(da)
        y=date
        print(x)
        print(y)
        if x>y:
            conn = sqlite3.connect('sql1.db')
            conn.execute("UPDATE COMPANY set  exp= '0' where ID = {}".format(int(idd)))
            conn.commit()
            conn.close()
            try:
              context.bot.kick_chat_member(chat_id=-1001365936441,user_id=int(idd))
            except:
                v=1
            context.bot.send_message(chat_id=int(idd),text="renew your subscription to join again")
        elif x==y:
          context.bot.send_message(chat_id=int(idd),text="today is last date of you subsription update it otherwise you will be remove tomorrow")

      
  except:
    c=0


def main():
  updater = Updater("5250391975:AAHm7eWueKgbHRK6fmswjFsg71Z70M4ra-E", use_context=True)
  dp = updater.dispatcher
  dp.job_queue.run_repeating(callback_minut, 10)
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
        
            BUTTON: [CallbackQueryHandler(button)],
        },
        fallbacks=[CommandHandler('start', start)]
    )
  dp.add_handler(conv_handler)
  
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()