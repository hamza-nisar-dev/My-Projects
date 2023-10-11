import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import KeyboardButton
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import sqlite3
import re
import os
import sqlite3 as sql
from coinbase_commerce.client import Client
import csv
API_KEY = "6341eff5-3f5c-4d52-872e-4980faa6e851"
client = Client(api_key=API_KEY)
BAS,AAA,BBB,CCC,DDD,EE= range(6)
wc=["welcome to bot shop"]
help=["not set by admin yet"]
pr=[2.0]
def start(update, context):
  user=update.effective_user.id
  print(user)
  connection = sqlite3.connect("wallet.db")  
  cursor = connection.cursor()  
  cursor.execute("SELECT ID FROM COMPANY where ID= {}".format(int(user))) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
    
      connection = sqlite3.connect("wallet.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,balance,link,code) \
        VALUES ({}, '{}','{}','{}')".format(int(user),"0","0","0"))
      connection.commit()
      connection.close()
  user = update.message.from_user
  usa=user.first_name
  if update.effective_user.id==807516030:
    loc_keyboard = KeyboardButton(text="Add key")
    loc_keyboard2 = KeyboardButton(text="Delete Key")
    lo5 = KeyboardButton(text="Update Welcome Message")
    lo6 = KeyboardButton(text="Update Support Message")
    lo7 = KeyboardButton(text="Set license price")
    lo8 = KeyboardButton(text="Key Statictics")
    keyboard = [[loc_keyboard,loc_keyboard2],[lo5,lo6],[lo7,lo8]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard:",reply_markup=reply_markup)

  else: 
    loc_keyboard = KeyboardButton(text="Buy license key")
    loc_keyboard2 = KeyboardButton(text="Wallet")
    loc_keyboard3 = KeyboardButton(text="Add Credit")
    lo4 = KeyboardButton(text="Help and Support")
    keyboard = [[loc_keyboard],[loc_keyboard2,loc_keyboard3],[lo4]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Hello <b>{}</b> {}".format(usa,wc[0]),parse_mode=telegram.ParseMode.HTML,reply_markup=reply_markup)

def USER(update, context):
    msg=update.message.text
    if  msg =="Buy license key":
        loc_keyboard = KeyboardButton(text="ACTIVE CODE")
        loc_keyboard3 = KeyboardButton(text="M3U")
        loc_keyboard2 = KeyboardButton(text="XTREAM API")
        lo4 = KeyboardButton(text="Main Menu")
        keyboard = [[loc_keyboard],[loc_keyboard3],[loc_keyboard2],[lo4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the license Type:",reply_markup=reply_markup)
    elif msg=="Wallet":
          user=update.message.from_user
          usa=user.first_name
          connection = sqlite3.connect("wallet.db")  
          cursor = connection.cursor()  
          cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
          for names in cursor:
            inv=names[0]
          context.bot.send_message(chat_id=update.effective_user.id,text="Wallet ID:   {}\n\nName:   {}\nBalance:   ${}".format(update.effective_user.id,usa,inv)) 
    elif msg=="ACTIVE CODE" or msg=="M3U" or msg=="XTREAM API":
        lo1= KeyboardButton(text="FREE TEST 2 DAYS")
        lo2= KeyboardButton(text="1 MONTH")
        lo3 = KeyboardButton(text="3 MONTH")
        lo4= KeyboardButton(text="6 MONTH")
        lo5 = KeyboardButton(text="12 MONTH")
        lo6 = KeyboardButton(text="Main Menu")
        keyboard = [[lo1,lo2],[lo3,lo4],[lo5,lo6]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the license Period:",reply_markup=reply_markup)


    elif msg=="Main Menu":
      user = update.message.from_user
      usa=user.first_name
      loc_keyboard = KeyboardButton(text="Buy license key")
      loc_keyboard2 = KeyboardButton(text="Wallet")
      loc_keyboard3 = KeyboardButton(text="Add Credit")
      lo4 = KeyboardButton(text="Help and Support")
      keyboard = [[loc_keyboard],[loc_keyboard2,loc_keyboard3],[lo4]]
      reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Hello <b>{}</b> {}".format(usa,wc[0]),parse_mode=telegram.ParseMode.HTML,reply_markup=reply_markup) 
    elif msg=="Add Credit":
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT code,link FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
        for names in cursor:
          inv=names[0]
          inv1=names[1]
        if inv=="0":
          charge = client.charge.create(name='Telegram botShop',
                            description='Pay to add credit to your wallet',
                            pricing_type='no_price',
                            local_price={ 
                        })
          linka=charge["hosted_url"]
          coda=charge["id"]
          conn = sqlite3.connect("wallet.db")  
          conn.execute("UPDATE COMPANY set link = '{}', code='{}' where ID = {}".format(linka,coda,int(update.effective_user.id)))
          conn.commit()
          conn.close()
          keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)],[InlineKeyboardButton("I have paid", callback_data="927")]]
          reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
          context.bot.send_message(chat_id=update.effective_user.id,text="Click on below button to make payment and after making payment wait for few minutes then come back and click on i have paid.",reply_markup=reply_markup) 
        else:
          aa=client.charge.retrieve(inv)
          b=aa['timeline']
          a=0
          for names in b:
            ax=names['status']
            if ax=="NEW":
              a=4
          for names in b:
            ax=names['status']
            if ax=="EXPIRED":
              a=3
          for names in b:
            ax=names['status']
            if ax=="PENDING":
              a=2
          for names in b:
            ax=names['status']
            if ax=="COMPLETED":
              a=1
          if a==1:
            cv=aa['payments']
            for names in cv:
              vb=names['value']['local']['amount']
              vb=float(vb)
              vb=round(vb,5)
              print(vb)
              connection = sqlite3.connect("wallet.db")  
              cursor = connection.cursor()  
              cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
              for names in cursor:
                inv=float(names[0])
              bn=vb+inv
              bn=str(bn)
              conn = sqlite3.connect("wallet.db")  
              conn.execute("UPDATE COMPANY set balance = '{}' where ID = {}".format(bn,int(update.effective_user.id)))
              conn.commit()
              conn.close()
              conn = sqlite3.connect("wallet.db")  
              conn.execute("UPDATE COMPANY set link = '0', code='0' where ID = {}".format(int(update.effective_user.id)))
              conn.commit()
              conn.close()
              keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
              reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
              context.bot.send_message(chat_id=update.effective_user.id,text="${} added to your wallet".format(vb),reply_markup=reply_markup)
              
          elif a==2:
            keyboard =[[InlineKeyboardButton("Check Again", callback_data="927")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Your previous transcation is pending please wait for its completion",reply_markup=reply_markup)
            
          elif a==3:
              charge = client.charge.create(name='Telegram botShop',
                            description='Pay to add credit to your wallet',
                            pricing_type='no_price',
                            local_price={ 
                            })
              linka=charge["hosted_url"]
              coda=charge["id"]
              conn = sqlite3.connect("wallet.db")  
              conn.execute("UPDATE COMPANY set link = '{}', code='{}' where ID = {}".format(linka,coda,int(update.effective_user.id)))
              conn.commit()
              conn.close()
              keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)],[InlineKeyboardButton("I have paid", callback_data="927")]]
              reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
              context.bot.send_message(chat_id=update.effective_user.id,text="Click on below button to make payment and after making payment wait for few minutes then come back and click on i have paid.",reply_markup=reply_markup)
          else:
            connection = sqlite3.connect("wallet.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT link FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
            for names in cursor:
              inv1=names[0]
            keyboard =[[InlineKeyboardButton("Make a Payment",url=inv1)],[InlineKeyboardButton("I have paid", callback_data="927")],[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Click on below button to make payment and after making payment wait for few minutes then come back and click on i have paid.",reply_markup=reply_markup)
    elif msg=="1 MONTH" or msg=="3 MONTH" or msg =="6 MONTH" or msg=="12 MONTH":
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
        for names in cursor:
          inv=float(names[0])
        if inv>pr[0]:
            nb=inv-pr[0]
            nb=str(nb)
            connection = sqlite3.connect("key.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT serial_key FROM COMPANY where period= '{}' AND status='un_used'".format(msg))
            for names in cursor:
              inv=names[0]
            context.bot.send_message(chat_id=update.effective_user.id,text="Here is Your license key:\n{}".format(inv))
            conn = sqlite3.connect("key.db")  
            conn.execute("UPDATE COMPANY set status = 'used' where serial_key = '{}'".format(inv))
            conn.commit()
            conn.close()
            conn = sqlite3.connect("wallet.db")  
            conn.execute("UPDATE COMPANY set balance = '{}' where ID = {}".format(nb,int(update.effective_user.id)))
            conn.commit()
            conn.close()
            connection = sqlite3.connect("key.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT serial_key FROM COMPANY where period= '{}' AND status='un_used'".format(msg))
            jobs = cursor.fetchall()
            st=len(jobs)
            if st<10:
              context.bot.send_message(chat_id="1508891126" ,text="{} Period is low in stock")
              context.bot.send_message(chat_id="1251252160" ,text="{} Period is low in stock")
            


        else:
            context.bot.send_message(chat_id=update.effective_user.id,text="You Don't have enough balance in your account to purchase the license key\n\nPlease Click Add Crdit button to add Balance To your Wallet")
    elif msg=="FREE TEST 2 DAYS":
            connection = sqlite3.connect("key.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT serial_key FROM COMPANY where period= '{}' AND status='un_used'".format(msg) )
            for names in cursor:
              inv=names[0]
            context.bot.send_message(chat_id=update.effective_user.id,text="Here is Your license key:\n{}".format(inv))
            conn = sqlite3.connect("key.db")  
            conn.execute("UPDATE COMPANY set status = 'used' where serial_key = '{}'".format(inv))
            conn.commit()
            conn.close()
            connection = sqlite3.connect("key.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT serial_key FROM COMPANY where period= '{}' AND status='un_used'".format(msg))
            jobs = cursor.fetchall()
            st=len(jobs)
            if st<10:
              context.bot.send_message(chat_id="1508891126" ,text="{} Period is low in stock")
              context.bot.send_message(chat_id="1251252160" ,text="{} Period is low in stock")
    elif msg=="Help and Support":
      context.bot.send_message(chat_id=update.effective_user.id,text=help[0])
def ADMIN(update, context):
    msg=update.message.text
    if  msg =="Add key":
        context.bot.send_message(chat_id=update.effective_user.id,text="send all the keys seperated by comma(,) that you want to add")
        return BAS
    elif msg=="Delete Key":
      context.bot.send_message(chat_id=update.effective_user.id,text="send all the keys seperated by comma(,) that you want to delete")
      return BBB
    elif msg=="Main Menu.":
      loc_keyboard = KeyboardButton(text="Add key")
      loc_keyboard2 = KeyboardButton(text="Delete Key")
      lo5 = KeyboardButton(text="Update Welcome Message")
      lo6 = KeyboardButton(text="Update Support Message")
      lo7 = KeyboardButton(text="Set license price")
      lo8 = KeyboardButton(text="Key Statictics")
      keyboard = [[loc_keyboard,loc_keyboard2],[lo5,lo6],[lo7,lo8]]
      reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard:",reply_markup=reply_markup)
    elif msg=="Update Welcome Message":
      context.bot.send_message(chat_id=update.effective_user.id,text="Send the welcome message for shop")
      return CCC
    elif msg=="Update Support Message":
      context.bot.send_message(chat_id=update.effective_user.id,text="Send the welcome message for help")
      return DDD
    elif msg=="Set license price":
      context.bot.send_message(chat_id=update.effective_user.id,text="Send the price for the license")
      return EE
    elif msg=="Key Statictics":
      conn=sql.connect('key.db')
      cur = conn.cursor()
      cur.execute('''SELECT * FROM COMPANY''')
      rows = cur.fetchall()    
      cursor = conn.cursor()
      cursor.execute("select * from COMPANY")
      with open("statictics.csv", "w") as csv_file:
          csv_writer = csv.writer(csv_file, delimiter="\t")
          csv_writer.writerow([i[0] for i in cursor.description])
          csv_writer.writerows(cursor)
      dirpath = os.getcwd() + "/statictics.csv"
      conn.close()
      context.bot.send_document(chat_id=update.effective_user.id,document=open('statictics.csv', 'rb'))

def bas(update, context):
    global lis
    msg=update.message.text
    lis=msg
    lo1= KeyboardButton(text="FREE TEST 2 DAYS")
    lo2= KeyboardButton(text="1 MONTH")
    lo3 = KeyboardButton(text="3 MONTH")
    lo4= KeyboardButton(text="6 MONTH")
    lo5 = KeyboardButton(text="12 MONTH")
    lo6 = KeyboardButton(text="Main Menu.")
    keyboard = [[lo1,lo2],[lo3,lo4],[lo5,lo6]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the license Type:",reply_markup=reply_markup)
    return AAA
def bbb(update, context):
    msg=update.message.text
    ls=lis.split(",")
    for name in ls:
      connection = sqlite3.connect("key.db")  
      cursor = connection.execute("DELETE  from COMPANY where serial_key='{}'".format(name))
      connection.commit()
      connection.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="keys deleted successfully")


def aaa(update, context):
    msg=update.message.text
    ls=lis.split(",")
    for name in ls:
      connection = sqlite3.connect("key.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (serial_key,status,period) \
        VALUES ('{}', '{}','{}')".format(name,"un_used",msg))
      connection.commit()
      connection.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="keys added successfully")
def ee(update, context):
    try:
      msg=update.message.text
      msg=float(msg)
      pr.pop(0)
      pr.append(msg)
      context.bot.send_message(chat_id=update.effective_user.id,text="price updated successfully")
    except:
      context.bot.send_message(chat_id=update.effective_user.id,text="invalid amount!")
      return EE
def ccc(update, context):
    msg=update.message.text
    wc.pop(0)
    wc.append(msg)
    context.bot.send_message(chat_id=update.effective_user.id,text="welcome message updated successfully")
def ddd(update, context):
    msg=update.message.text
    help.pop(0)
    help.append(msg)
    context.bot.send_message(chat_id=update.effective_user.id,text="help message updated successfully")

def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    if a=="927":
      connection = sqlite3.connect("wallet.db")  
      cursor = connection.cursor()  
      cursor.execute("SELECT code FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
      for names in cursor:
        inv=names[0]
      aa=client.charge.retrieve(inv)
      b=aa['timeline']
      a=0
      for names in b:
        ax=names['status']
        if ax=="NEW":
          a=4
      for names in b:
        ax=names['status']
        if ax=="EXPIRED":
          a=3
      for names in b:
        ax=names['status']
        if ax=="PENDING":
          a=2
      for names in b:
        ax=names['status']
        if ax=="COMPLETED":
          a=1
      if a==1:
        cv=aa['payments']
        for names in cv:
          vb=names['value']['local']['amount']
          vb=float(vb)
          connection = sqlite3.connect("wallet.db")  
          cursor = connection.cursor()  
          cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
          for names in cursor:
            inv=float(names[0])
          bn=vb+inv
          bn=str(bn)
          conn = sqlite3.connect("wallet.db")  
          conn.execute("UPDATE COMPANY set balance = '{}' where ID = {}".format(bn,int(update.effective_user.id)))
          conn.commit()
          conn.close()
          conn = sqlite3.connect("wallet.db")  
          conn.execute("UPDATE COMPANY set link = '0', code='0' where ID = {}".format(int(update.effective_user.id)))
          conn.commit()
          conn.close()
          context.bot.send_message(chat_id=update.effective_user.id,text="${} is added to your wallet".format(vb))
      elif a==2:
        context.bot.send_message(chat_id=update.effective_user.id,text="Your Transcation is detected please wait for confirmation and then click i have paid button")
      elif a==3:
          conn = sqlite3.connect("wallet.db")  
          conn.execute("UPDATE COMPANY set link = '0', code='0' where ID = {}".format(int(update.effective_user.id)))
          conn.commit()
          conn.close()
          context.bot.send_message(chat_id=update.effective_user.id,text="Transcation Expired!")
      else:
        context.bot.send_message(chat_id=update.effective_user.id,text="No Transcation is detected yet")
       
def main():
    updater = Updater('1919009832:AAFU60jJpERbTNCCZ1zGKK3ENfIWugplnfg',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Add key|Delete Key|Update Welcome Message|Update Support Message|Set license price|Key Statictics|Main Menu.)$'), ADMIN)],

        states={
            
            BAS: [MessageHandler(Filters.text, bas)],
            AAA: [MessageHandler(Filters.regex('^(1 MONTH|3 MONTH|6 MONTH|12 MONTH|FREE TEST 2 DAYS)$'), aaa)],
            BBB: [MessageHandler(Filters.text, bbb)],
            CCC: [MessageHandler(Filters.text, ccc)],
            DDD: [MessageHandler(Filters.text, ddd)],
            EE: [MessageHandler(Filters.text, ee)],

            
                                               
        },
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
    dp.add_handler(conv_handler) 
    dp.add_handler(MessageHandler(Filters.regex('^(Buy license key|Wallet|Add Credit|Help and Support|1 MONTH|3 MONTH|6 MONTH|12 MONTH|FREE TEST 2 DAYS|Main Menu)$'), USER))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

