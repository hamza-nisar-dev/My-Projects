import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import sqlite3
import random
import sqlite3 as sql
import os
from sqlite3 import Error
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
from coinbase_commerce.client import Client
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
API_KEY = "c9ae131d-76b5-46dd-8023-a1a01226d818"
client = Client(api_key=API_KEY)
wc=["Welcome to Botshop.\nSelect the products and receive at your door step.\nCheck our Instock and also Pre-Order products.\n\nSHOP ONLNE.STAY HOME. STAY SAFE"]
BUTTON,QW,CRED,VAL,PRII,SH,UCR,UCCR,DESCR,FILA,PD,MODF,MODFF,CH,DELETE,EPR,DESCRW,FILAW,PRIIW,REM,REMM,RRT,FG= range(23) 
man=[]
price=['1']
valu=['50']
token=["1919009832:AAFU60jJpERbTNCCZ1zGKK3ENfIWugplnfg"]
logger = logging.getLogger(__name__)

def start(update, context):
  bnm=update.message.from_user
  global ms
  ms=bnm.first_name
  user=update.effective_user.id
  connection = sqlite3.connect("users.db")  
  cursor = connection.cursor()  
  cursor.execute("SELECT id FROM COMPANY where id= {}".format(int(user))) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
      cursor.execute("INSERT INTO COMPANY (ID) \
        VALUES ({})".format(int(user)))
      connection.commit()
      connection.close()
      connection = sqlite3.connect("wallet.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,balance ,link,code,credit) \
        VALUES ({}, '{}','{}','{}','{}')".format(int(user),"0.0","0","0","0"))
      connection.commit()
      connection.close()
  print(update.effective_user.id)
  user = update.message.from_user
  usa=str(update.effective_user.id)
  if usa ==  "1394902938" or usa=="807516030" or usa=="618918372" or usa in man:
    keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],[InlineKeyboardButton("⚙️ Edit Product", callback_data="90")],[InlineKeyboardButton("🙋‍♂️ Welome message", callback_data="912"),InlineKeyboardButton("Remove Credit", callback_data="3000")],[InlineKeyboardButton("⚙️Modify the Product's file", callback_data="3344"),InlineKeyboardButton("➕ Credit to account", callback_data="300")],[InlineKeyboardButton("  Check Products", callback_data="390")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
    return BUTTON
  else:   
    keyboard = [[InlineKeyboardButton("📝️ Buy license key", callback_data='11')],[InlineKeyboardButton("💳 Add Credit", callback_data='919'),InlineKeyboardButton("💳 Wallet", callback_data='920')]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text=wc[0],reply_markup=reply_markup)
    return BUTTON
def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    if a== '1':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send name of product",reply_markup=reply_markup) 
        return QW
    elif a=='3344':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Product ID to mofidy the Product;s file",reply_markup=reply_markup)
        return MODF

    elif a=='2':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Product ID to delete the Product",reply_markup=reply_markup)
        return DELETE
    elif a=='390':
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name, de, pr,fi,pid  from COMPANY")
        for row in cursor:   
          invv=row[3]
          iffd=row[4]
          if invv!="0":
            fname = '{}.txt'.format(iffd)
            count = 0 
            with open(fname, 'r') as f:
                for line in f:
                    count += 1
                m="𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐍𝐚𝐦𝐞:  "+row[0]+"\n𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  "+row[1]+"\n𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐈𝐃:  "+row[4]+"\n𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬:  "+row[2]+"\n𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬:  "+str(count)+"\n\n"
            keyboard =[[InlineKeyboardButton("🔙 Cancel", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=m,reply_markup=reply_markup)
    elif a=="912":
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Welcome message",reply_markup=reply_markup)   
        return SH
    elif a=="300":
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send amount of Credit to send",reply_markup=reply_markup)   
        return UCR
    elif a=="3000":
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send User's ID to remove Credit",reply_markup=reply_markup)   
        return REM
    elif a=="90":
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Product ID to modify the product",reply_markup=reply_markup)
        return FG
    elif a=="920":
          user=update.callback_query.message.from_user
          usa=user.first_name
          connection = sqlite3.connect("wallet.db")  
          cursor = connection.cursor()  
          cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
          for names in cursor:
            inv=names[0]
          keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
          reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
          context.bot.send_message(chat_id=update.effective_user.id,text="Wallet ID:  "+str(update.effective_user.id)+"\nCredits:  "+inv,reply_markup=reply_markup)                  
   
    elif a== '32':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send value of 1 credit in USD\nfor example send 1 to set 1credit=1USD ',reply_markup=reply_markup)
        return VAL
    elif a== '90':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send price of account in credit ',reply_markup=reply_markup)
        return PRII
    elif a=='110000':
      
    elif a=='110000':
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name, de, pr,fi,pid  from COMPANY")
        for row in cursor:   
          invv=row[3]
          iffd=row[4]
          if invv!="0":
            fname = '{}.txt'.format(iffd)
            count = 0 
            with open(fname, 'r') as f:
                for line in f:
                    count += 1
                m="𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐍𝐚𝐦𝐞:  "+row[0]+"\n𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  "+row[1]+"\n𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐈𝐃:  "+row[4]+"\n𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬:  "+row[2]+"\n𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬:  "+str(count)+"\n\n"
            keyboard =[[InlineKeyboardButton("Buy", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=m,reply_markup=reply_markup)

    elif a=='919':
            keyboard =[[InlineKeyboardButton("Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Send the amount of credit you want to add in your wallet as 1 credit ={}USD\n example (1000)".format(price[0]),reply_markup=reply_markup)
            return CRED
    elif a== '995':
      cc=update.callback_query.message.text
      connection = sqlite3.connect("wallet.db")  
      cursor = connection.cursor()  
      cursor.execute("SELECT code,balance,credit FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
      for names in cursor:
        inv=names[0]
        jjaa=names[1]
        jjaa=float(jjaa)
        crr=names[2]
        crr=float(crr)
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
            conn = sqlite3.connect("wallet.db")  
            conn.execute("UPDATE COMPANY set link = '0', code='0',balance='{}' where ID = {}".format(crr,int(update.effective_user.id)))
            conn.commit()
            conn.close()
            asdd=jjaa-fo 
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Credit added to your wallet",reply_markup=reply_markup)
            return BUTTON
      elif a==2:
        keyboard =[[InlineKeyboardButton("Check again", callback_data="995")]]
        context.bot.send_message(chat_id=update.effective_user.id,text="Transcation is pending come back later then click 'check again'")
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=cc,reply_markup=reply_markup)
        return BUTTON
      elif a==3:
        conn = sqlite3.connect("wallet.db")  
        conn.execute("UPDATE COMPANY set link = '0', code='0' where ID = {}".format(int(update.effective_user.id)))
        conn.commit()
        conn.close()
        keyboard =[[InlineKeyboardButton("Main Menu", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Transcation Expired!",reply_markup=reply_markup)
        return button
      else:
        keyboard =[[InlineKeyboardButton("Check again", callback_data="995")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Transcation is not detected yet")
        context.bot.send_message(chat_id=update.effective_user.id,text=cc,reply_markup=reply_markup)
        return BUTTON
    elif a=='200':
        keyboard = [[InlineKeyboardButton("📝️ Buy Account", callback_data='11')],[InlineKeyboardButton("💳 Add Credit", callback_data='919'),InlineKeyboardButton("💳 Wallet", callback_data='920')]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=wc[0],reply_markup=reply_markup)
        return BUTTON
    elif a=='100':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],[InlineKeyboardButton("Set credit Value  ", callback_data="32"),InlineKeyboardButton("⚙️ Edit Product", callback_data="90")],[InlineKeyboardButton("🙋‍♂️ Welome message", callback_data="912"),InlineKeyboardButton("Remove Credit", callback_data="3000")],[InlineKeyboardButton("⚙️Modify the Product's file", callback_data="3344"),InlineKeyboardButton("➕ Credit to account", callback_data="300")],[InlineKeyboardButton("  Check Products", callback_data="390")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
    elif a== '16':
      cc=update.callback_query.message.text
      cf=update.callback_query.message.message_id
      ddd=update.callback_query.message.chat.first_name
      x=cc.split("𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐍𝐚𝐦𝐞:  ")
      x=x[1]
      x=x.split("𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  ")
      x=x[0]
      x=x.strip()
      xr=cc.split("𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬:  ")
      xr=xr[1]
      xr=xr.split("𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬:  ")
      xr=xr[0]
      xr=xr.strip()
      xrf=cc.split("𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐈𝐃:  ")
      xrf=xrf[1]
      xrf=xrf.split("𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐂𝐫𝐞𝐝𝐢𝐭𝐬:  ")
      xrf=xrf[0]
      xrf=xrf.strip()
      eo=float(xr)
      connection = sqlite3.connect("wallet.db")
      cursor = connection.cursor()  
      cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
      for names in cursor:
          inv=float(names[0])
          if eo>inv:
              keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
              reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
              context.bot.send_message(chat_id=update.effective_user.id,text="Sorry, You dont have enough balance for this purchase. Add Credit to your Wallet and try again.",reply_markup=reply_markup)
              return BUTTON
          else:
            f = open( '{}.txt'.format(xrf), 'r' )
            lines = f.readlines()
            vv=lines[0]
            vv=str(vv)

            f.close()
            f = open( '{}.txt'.format(xrf),'w' )
            f.write( ''.join( lines[1:] ) )
            f.close()
            fname = '{}.txt'.format(xrf)
            count = 0  
            with open(fname, 'r') as f:
                for line in f:
                    count += 1
                if count==0:
                  conn = sqlite3.connect('shop.db')
                  cursor = conn.execute("UPDATE COMPANY set fi='0' where pid= '{}'".format(xrf))
                  conn.commit()
                  context.bot.send_message(chat_id=1394902938,text="Update file for product where productID is:  "+x)
                  v= random.randint (0,999999)
                  
                  conn = sqlite3.connect('orders.db')
                  conn.execute("INSERT INTO COMPANY (ID,oid,pr,name) \
                          VALUES ('{}', '{}','{}', '{}')".format(str(update.effective_user.id),v,xr,x)) 
                  conn.commit()
                  connection = sqlite3.connect("wallet.db")
                  cursor = connection.cursor()  
                  cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
                  for names in cursor:
                      inv=float(names[0])
                      zd=float(xr)
                      oq=inv-zd
                      cursor.execute("UPDATE COMPANY set balance ='{}'  where ID = {}".format(oq,int(update.effective_user.id)))
                      conn.commit()
                      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
                      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                      context.bot.send_message(chat_id=update.effective_user.id,text="Here is your delivery\n"+vv,reply_markup=reply_markup)
                      return BUTTON
                else:
                      v= random.randint (0,999999)
                      
                      conn = sqlite3.connect('orders.db')
                      conn.execute("INSERT INTO COMPANY (ID,oid,pr,name) \
                          VALUES ('{}', '{}','{}', '{}')".format(str(update.effective_user.id),v,xr,x)) 
                      conn.commit()
                      connection = sqlite3.connect("wallet.db")
                      cursor = connection.cursor()  
                      cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
                      for names in cursor:
                          inv=float(names[0])
                          zd=float(xr)
                          oq=inv-zd
                          cursor.execute("UPDATE COMPANY set balance ='{}'  where ID = {}".format(oq,int(update.effective_user.id)))
                          connection.commit()
                      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
                      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                      context.bot.send_message(chat_id=update.effective_user.id,text="Here is your delivery\n"+vv,reply_markup=reply_markup)
                      return BUTTON
def modf(update,context):
    msg=update.message.text
    global mpd
    mpd=msg
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT pid  from COMPANY where pid='{}'".format(msg))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Send Product;s file",reply_markup=reply_markup)
      return MODFF
    else:
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="ProductID is wrong Send valid Product ID",reply_markup=reply_markup)
      return MODF
def modff(update,context):
    sd=update.message.document.file_id
    filef = context.bot.getFile(update.message.document.file_id)
    filef.download('{}.txt'.format(mpd))
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("UPDATE COMPANY set fi='{}' where pid='{}'".format(sd,mpd))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Done",reply_markup=reply_markup)
    return BUTTON
def ch(update,context):
    a=update.message.text
    myfile = "cata.txt"
    with open(myfile, "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", a))
        f.truncate()
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Category Changed",reply_markup=reply_markup)
    return BUTTON
def pd(update,context):
    msg=update.message.text
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT name from COMPANY where name='{}'".format(msg))
    conn.commit()
    for names in cursor:
      inv=names[0]
      if inv in msg:
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name, de, pr,fi,pid from COMPANY where name= '{}'".format(inv))
        for row in cursor:   
          invv=row[3]
          inf=row[4]
          if invv!="0":
            fname = '{}.txt'.format(invf)
            count = 0 
            with open(fname, 'r') as f:
                for line in f:
                    count += 1
                m="Account Name:  "+row[0]+"\nAccount Description:  "+row[1]+"\nProduct ID:  "+row[4]+"\nAccount Price:  "+row[2]+"$"+"\nAvailable Accounts:  "+str(count)+"\n\n"
            keyboard =[[InlineKeyboardButton("Buy", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=m,reply_markup=reply_markup)
          else:
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Sorry accounts not available. Try again later",reply_markup=reply_markup)
        break
    return BUTTON
def cred(update,context):
  msg=update.message.text
  try:
        msg=float(msg)
        fg=float(price[0])
        credit=fg*msg 
        charge = client.charge.create(name='Telegram botShop',
                          description='Payment for the product',
                          pricing_type= 'fixed_price',
                          local_price= {
                          "amount": str(credit),
                          "currency": "USD"})
        linka=charge["hosted_url"]
        coda=charge["id"]
        print(coda)
        conn = sqlite3.connect("wallet.db")  
        conn.execute("UPDATE COMPANY set link = '{}', code='{}',credit='{}' where ID = {}".format(linka,coda,credit,int(update.effective_user.id)))
        conn.commit()
        conn.close()
        keyboard =[[InlineKeyboardButton("Make a Payment", url=linka)],[InlineKeyboardButton("I have paid", callback_data="995")],[InlineKeyboardButton("🔙 Back", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Total Amount= "+str(credit)+"$" ,reply_markup=reply_markup)
        return BUTTON
  except:
        keyboard =[[InlineKeyboardButton("Back", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format send again.\nSend the amount of credit you want to add in your wallet\n example (1000)",reply_markup=reply_markup)
        return CRED

def val(update,context):
  msg=update.message.text
  try:
    msg=float(msg)
    price.pop(0)
    price.append(msg)
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Value Updated",reply_markup=reply_markup)
    return BUTTON
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend value of 1 credit in USD\nfor example send 1 to set 1credit=1USD",reply_markup=reply_markup)
    return VAL
def ucr(update,context):
  msg=update.message.text
  try:
    msg=int(msg)
    global accc
    accc=msg
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send User ID to send Credit",reply_markup=reply_markup)
    return UCCR 
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend amount of credit",reply_markup=reply_markup)
    return UCR
def uccr(update,context):
  msg=update.message.text
  try:
    msg=int(msg)
    conn = sqlite3.connect("wallet.db")  
    cursor=conn.execute("SELECT ID from COMPANY where id={}".format(int(msg)) )
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      cursor=conn.execute("SELECT ID,balance from COMPANY where id={}".format(int(msg)) )
      conn.commit()
      for names in cursor:
        inv=names[0] 
        inv1=names[1]
        inv1=float(inv1)
        fnm=float(accc)
        dk=fnm+inv1
        conn.execute("UPDATE COMPANY set balance='{}' where ID= {}".format(dk,int(msg)) )
        conn.commit()
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Credit Sent",reply_markup=reply_markup)
    else:
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="User's ID not found",reply_markup=reply_markup)
        return UCCR
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend User ID ",reply_markup=reply_markup)
    return UCCR

def rem(update,context):
  msg=update.message.text
  global wr
  wr=msg
  try:
    msg=int(msg)
    conn = sqlite3.connect("wallet.db")  
    cursor=conn.execute("SELECT ID from COMPANY where id={}".format(int(msg)) )
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      cursor=conn.execute("SELECT ID,balance from COMPANY where id={}".format(int(msg)) )
      conn.commit()
      for names in cursor:
        inv=names[0] 
        inv1=names[1]
        dk="User ID:  "+str(inv)+"\nCredits:  "+str(inv1)+"\nSend Credits you want to remove"
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=dk,reply_markup=reply_markup)
        return REMM
    else:
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="User's ID not found",reply_markup=reply_markup)
        return REM
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend User ID ",reply_markup=reply_markup)
    return REM
def remm(update,context):
  msg=update.message.text
  try:
    msg=int(msg)
    conn = sqlite3.connect("wallet.db")  
    cursor=conn.execute("SELECT ID from COMPANY where id={}".format(int(wr)) )
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      cursor=conn.execute("SELECT ID,balance from COMPANY where id={}".format(int(wr)) )
      conn.commit()
      for names in cursor:
        inv=names[0] 
        inv1=names[1]
        inv1=float(inv1)
        ffg=float(msg)
        drt=inv1-ffg
        conn.execute("UPDATE COMPANY set balance='{}' where ID= {}".format(drt,int(wr)) )
        conn.commit()
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=str(msg)+" Credits removed",reply_markup=reply_markup)
    else:
        keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="User's ID not found",reply_markup=reply_markup)
        return REMM
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend User ID ",reply_markup=reply_markup)
    return REMM
def prii(update,context):
  msg=update.message.text
  try:
    msg=float(msg)
    global tp
    tp=msg
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send text file of account",reply_markup=reply_markup)
    return FILA
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend price of account in credit",reply_markup=reply_markup)
    return PRII
def priiw(update,context):
  msg=update.message.text
  try:
    msg=float(msg)
    global tpw
    tpw=msg
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send text file of account",reply_markup=reply_markup)
    return FILAW
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend price of account in credit",reply_markup=reply_markup)
    return PRIIW


def qw(update,context):
    msg=update.message.text
    global nm
    nm =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send Description of Account" ,reply_markup=reply_markup)
    return DESCR
def fg(update,context):
    msg=update.message.text
    global fl
    fl=msg
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT pid  from COMPANY where pid='{}'".format(msg))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Send name of product",reply_markup=reply_markup)
      return EPR
    else:
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="ProductID is wrong Send valid Product ID",reply_markup=reply_markup)
      return FG
def epr(update,context):
    msg=update.message.text
    global nmw
    nmw =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send Description of Account" ,reply_markup=reply_markup)
    return DESCRW
def descr(update,context):
  msg=update.message.text
  global dsr
  dsr=msg
  keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Send Special product ID" ,reply_markup=reply_markup)
  return RRT
def rrt(update,context):
  msg=update.message.text
  global pid
  pid=msg
  keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Send price of 1 Account" ,reply_markup=reply_markup)
  return PRII
def descrw(update,context):
  msg=update.message.text
  global dsrw
  dsrw=msg
  keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Send price of 1 Account" ,reply_markup=reply_markup)
  return PRIIW
def fila(update,context):
    vc=update.message.document.file_id
    global fill
    fill="0"
    file1 = context.bot.getFile(update.message.document.file_id)
    file1.download('{}.txt'.format(pid))
    yu= random.randint (0,999999)
    conn = sqlite3.connect('shop.db')
    conn.execute("INSERT INTO COMPANY (ID,oid,de,pr,fi,name,pid) \
                      VALUES ('{}', '{}','{}', '{}','{}', '{}', '{}')".format(str(update.effective_user.id),yu,dsr,tp,"1",nm,pid))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Account added" ,reply_markup=reply_markup)
    return BUTTON
def filaw(update,context):
    vc=update.message.document.file_id
    global fill
    fill="0"
    file1 = context.bot.getFile(update.message.document.file_id)
    file1.download('{}.txt'.format(nmw))
    yu= random.randint (0,999999)
    conn = sqlite3.connect('shop.db')
    conn.execute("UPDATE COMPANY set oid='{}',de='{}',pr='{}',fi='{}',pid='{}',name='{}' where pid='{}'".format(yu,dsrw,tpw,"1",fl,nmw,fl))

    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Product Edited" ,reply_markup=reply_markup)
    return BUTTON
def delete(update,context):
    msg=update.message.text
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT pid  from COMPANY where pid='{}'".format(msg))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
      cursor = conn.execute("DELETE  from COMPANY where pid='{}'".format(msg))
      conn.commit()
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Product Deleted",reply_markup=reply_markup)
      return BUTTON
    else:
      keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="ProductID is wrong Send valid Product ID",reply_markup=reply_markup)
      return delete
def sh(update,context):
       a=update.message.text
       wc.pop(0)
       wc.append(a)
       keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
       reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
       context.bot.send_message(chat_id=update.effective_user.id,text="Welcome message updated",reply_markup=reply_markup)
       return BUTTON
def main():
  updater = Updater(token[0], use_context=True)
  dp = updater.dispatcher
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            
        BUTTON: [CallbackQueryHandler(button),MessageHandler(Filters.text, pd)],
        QW: [MessageHandler(Filters.text, qw),CallbackQueryHandler(button)],
        EPR: [MessageHandler(Filters.text, epr),CallbackQueryHandler(button)],
        CRED: [MessageHandler(Filters.text, cred),CallbackQueryHandler(button)],
        VAL: [MessageHandler(Filters.text, val),CallbackQueryHandler(button)],
        PRII: [MessageHandler(Filters.text, prii),CallbackQueryHandler(button)],
        PRIIW: [MessageHandler(Filters.text, priiw),CallbackQueryHandler(button)],
        SH: [MessageHandler(Filters.text, sh),CallbackQueryHandler(button)],
        UCR: [MessageHandler(Filters.text, ucr),CallbackQueryHandler(button)],
        UCCR: [MessageHandler(Filters.text, uccr),CallbackQueryHandler(button)],
        DESCR: [MessageHandler(Filters.text, descr),CallbackQueryHandler(button)],
        DESCRW: [MessageHandler(Filters.text, descrw),CallbackQueryHandler(button)],
        PD: [MessageHandler(Filters.text, pd),CallbackQueryHandler(button)],
        CH: [MessageHandler(Filters.text, ch),CallbackQueryHandler(button)],
        MODF: [MessageHandler(Filters.text, modf),CallbackQueryHandler(button)],
        MODFF: [MessageHandler(Filters.document, modff),CallbackQueryHandler(button)],
        DELETE: [MessageHandler(Filters.text, delete),CallbackQueryHandler(button)],
        REM: [MessageHandler(Filters.text, rem),CallbackQueryHandler(button)],
        FG: [MessageHandler(Filters.text, fg),CallbackQueryHandler(button)],
        REMM: [MessageHandler(Filters.text, remm),CallbackQueryHandler(button)],
        FILA: [MessageHandler(Filters.document, fila),CallbackQueryHandler(button)],
        RRT: [MessageHandler(Filters.text, rrt),CallbackQueryHandler(button)],
        FILAW: [MessageHandler(Filters.document, filaw),CallbackQueryHandler(button)],

        },  
        fallbacks=[CommandHandler('start', start)]
    )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()