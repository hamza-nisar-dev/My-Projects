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
API_KEY = 'c1b66395ad7a9a99ca35e43edbe8df5376a6a33df74a27a5eb01f2ba8c899419'
API_SECRET = '9534C4f9Da52875D1b325Dd0685f9F299010F7204F650448d7664BcA71bd1458'
IPN_URL = 'http://t.me/BPTSubscription_bot'
BUTTON= range(1) 

def start(update, context):
    connection = sqlite3.connect("sql.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        conn = sqlite3.connect('sql.db')
        conn.execute("INSERT INTO COMPANY (ID,Trx,exp) \
            VALUES ({}, '{}','{}')".format(update.effective_user.id,"0","0"))
        conn.commit()
        conn.close()
    keyboard = [[InlineKeyboardButton("1 MONTH - $100.00 (USD)", callback_data='1')],[InlineKeyboardButton("6 MONTH - $500.00 (USD)", callback_data='2')],[InlineKeyboardButton("12 MONTH - $1000.00 (USD)", callback_data='3')]]  
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
  if a== '1':
    query.answer()
    keyboard = [[InlineKeyboardButton("Bitcoin", callback_data='4')],[InlineKeyboardButton("Ethereum", callback_data='44')],[InlineKeyboardButton("Tether", callback_data='444')],
                [InlineKeyboardButton("🔙 Back", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Subscription period: Monthly\n""No automatically recurring payments\n\n""INCLUDES:\n""- Premium Trade Channel\n""- Market Scanner\n""- Pro-Support & Chat Channel\n""- Custom News Scanner Channel\n""- ALPHA Suite Indicators",reply_markup=reply_markup)
    return BUTTON

  elif a== '2':
    query.answer()
    keyboard = [[InlineKeyboardButton("Bitcoin", callback_data='7')],[InlineKeyboardButton("Ethereum", callback_data='77')],[InlineKeyboardButton("Tether", callback_data='777')],
                [InlineKeyboardButton("🔙 Back", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Subscription period: Quarterly\n""No automatically recurring payments\n\n""INCLUDES:\n""- Premium Trade Channel\n""- Market Scanner\n""- Pro-Support & Chat Channel\n""- Custom News Scanner Channel\n""- ALPHA Suite Indicators",reply_markup=reply_markup)
    return BUTTON
  elif a== '3':
    query.answer()
    keyboard = [[InlineKeyboardButton("Bitcoin", callback_data='8')],[InlineKeyboardButton("Ethereum", callback_data='88')],[InlineKeyboardButton("Tether", callback_data='888')],
                [InlineKeyboardButton("🔙 Back", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Subscription period: 1 year\n""No automatically recurring payments\n\n""INCLUDES:\n""- Premium Trade Channel\n""- Market Scanner\n""- Pro-Support & Chat Channel\n""- Custom News Scanner Channel\n""- ALPHA Suite Indicators",reply_markup=reply_markup)
    return BUTTON
  elif a== '4' or a=='44' or a=="444":
    query.answer()
    if a=='4':
        ham="BTC"
    elif a=='44':
        ham="ETH"
    else:
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
            conn.execute("UPDATE COMPANY set exp='{}' where ID = {}".format(inv,update.effective_user.id))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below links to join paid channels",reply_markup=reply_markup)                       
            return BUTTON
    create_transaction_params = {
     'amount' : 50,
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
                [InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=+1)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}' where ID = {}".format(post,dat,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Amount: {} {}\n To Address:\n{}\n\n""Or click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation  and then click on 'I have Paid' button".format(am,ham,ad),reply_markup=reply_markup)
    return BUTTON
     
  elif a== '7' or a=='77' or a=="777":
    query.answer()
    if a=='7':
        ham="BTC"
    elif a=='77':
        ham="ETH"
    else:
        ham="USDT.ERC20"
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
            conn.execute("UPDATE COMPANY set exp='{}' where ID = {}".format(inv,update.effective_user.id))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below links to join paid channels",reply_markup=reply_markup)                       
            return BUTTON

    create_transaction_params = {
     'amount' : 130,
     'currency1' : 'USD',
     'currency2' : ham,
     'buyer_email': 'rhamza126@gmail.com'
           }
    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
    transaction = client.createTransaction(create_transaction_params)
    if transaction['error'] == 'ok':
        am= transaction['amount'] 
        ad=transaction['address']
        url=transaction['checkout_url']
    post = {
        'txid' : transaction['txn_id'],}
    post=post['txid']
    keyboard = [[InlineKeyboardButton("I have Paid", callback_data='9')],[InlineKeyboardButton("Make a Payment", url=url)],
                [InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=+6)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}' where ID = {}".format(post,dat,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Amount: {} {}\n To Address:\n{}\n\n""Or click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation  and then click on 'I have Paid' button".format(am,ham,ad),reply_markup=reply_markup)
    return BUTTON
  elif a== '8' or a=='88' or a=="888":
    query.answer()
    if a=='8':
        ham="BTC"
    elif a=='888':
        ham="ETH"
    else:
        ham="USDT.ERC20"
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
            conn.execute("UPDATE COMPANY set exp='{}' where ID = {}".format(inv,update.effective_user.id))
            conn.commit()
            conn.close()
            context.bot.send_message(chat_id=update.effective_user.id,text="Amount: {} {}\n To Address:\n{}\n\n""Or click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation  and then click on 'I have Paid' button".format(am,ham,ad),reply_markup=reply_markup)
            return BUTTON

    create_transaction_params = {
     'amount' : 450,
     'currency1' : 'USD',
     'currency2' : ham,
     'buyer_email': 'rhamza126@gmail.com'
           }
    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
    transaction = client.createTransaction(create_transaction_params)
    if transaction['error'] == 'ok':
        am= transaction['amount'] 
        ad=transaction['address']
        url=transaction['checkout_url']
   
    post = {
        'txid' : transaction['txn_id'],}
    post=post['txid']
    keyboard = [[InlineKeyboardButton("I have Paid", callback_data='9')],[InlineKeyboardButton("Make a Payment", url=url)],
                [InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=+12)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}' where ID = {}".format(post,dat,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Please send {} to {}\n\n""Or click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation  and then click on 'I have Paid' button".format(am,ad),reply_markup=reply_markup)
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
            keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_user.id,text="No transcation found yet. comeback later",reply_markup=reply_markup)                       
            return BUTTON
        elif c==1:
            keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_user.id,text="Your transcation is pending please come back again later",reply_markup=reply_markup)                       
            return BUTTON
        else:
            keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_user.id,text="error in transcation cotact admin",reply_markup=reply_markup)                       
            return BUTTON
    else:
        keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_user.id,text="No transcation found yet.",reply_markup=reply_markup)                       
        return BUTTON

  elif a== '6':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MONTH - $100.00 (USD)", callback_data='1')],[InlineKeyboardButton("6 MONTH - $500.00 (USD)", callback_data='2')],[InlineKeyboardButton("12 MONTH - $1000.00 (USD)", callback_data='3')]]  
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
        x=datetime.today().strftime('%Y-%m-%d')
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
  updater = Updater("1832733624:AAGbk-r715IgFgErM_icRRA0UhOZQvWC0O4", use_context=True)
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