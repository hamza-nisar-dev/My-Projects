from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import date
from dateutil.relativedelta import relativedelta
import sqlite3
from coinbase_commerce.client import Client
import datetime as dt
API = ["d8bee9ab-eaf8-4038-b0d8-66a003b239bb"]

BUTTON,VBNM= range(2) 

def start(update, context):
    userd = update.message.from_user
    userna=userd.username
    bnm=update.message.from_user
    try:
        ms=bnm.usernamee
    except: 
        ms=bnm.first_name
    user=int(update.effective_user.id)
    print(user)
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
                conn = sqlite3.connect('sql1.db')
                conn.execute("INSERT INTO COMPANY (ID,exp) \
                    VALUES ({}, '{}')".format(update.effective_user.id,"0"))
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
                keyboard = [[InlineKeyboardButton("VIP SPOT", callback_data='11'),InlineKeyboardButton("VIP FUTUROS", callback_data='22')],[InlineKeyboardButton("VIP ELITE", callback_data='44'),InlineKeyboardButton("VIP spot+ VIP Futuros", callback_data='33a')],[InlineKeyboardButton("Refferal", callback_data='qre')]]  
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                user = update.message.from_user
                usa=user.first_name
                msfa='hey '+usa
                context.bot.send_message(chat_id=update.effective_user.id,text=msfa)
                context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
                return BUTTON
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
                conn = sqlite3.connect('sql1.db')
                conn.execute("INSERT INTO COMPANY (ID,exp) \
                    VALUES ({}, '{}')".format(update.effective_user.id,"0"))
                conn.commit()
                conn.close()
            keyboard = [[InlineKeyboardButton("VIP SPOT", callback_data='11'),InlineKeyboardButton("VIP FUTUROS", callback_data='22')],[InlineKeyboardButton("VIP ELITE", callback_data='44'),InlineKeyboardButton("VIP spot+ VIP Futuros", callback_data='33a')],[InlineKeyboardButton("Refferal", callback_data='qre')]]  
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
  client = Client(api_key=API[0])
  if a== '50a' or a=='25a' or a=="70a" or a=='125a' or a=="200a":#or a== '48' or a=='95' or a=="120"or a=='210' or a=="360" or a== '50' or a=='100' or a=="135"or a=='240' or a=="450":
    query.answer()
    if a=='25a':
        dd=1
        pp=25
    elif a=='50a':
        dd=2
        pp=50
    elif a=='70a':
        dd=3
        pp=70
    elif a=='125a':
        dd=6
        pp=125
    elif a=='200a':
        dd=12
        pp=200
    ham="USDT.TRC20"
    charge = client.charge.create(name='Nation Forex Signals',
                          description="Nation Forex Signals",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pp,
                             "currency": "USD"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,"1")) 
    conn.commit()
    keyboard = [[InlineKeyboardButton("Make a Payment", url=linka)],
                [InlineKeyboardButton("🔙 Cancel", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=dd)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}',amount='{}' where ID = {}".format(coda,dat,pp,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation",reply_markup=reply_markup)
    return BUTTON

  elif a== '50b' or a=='25b' or a=="70b" or a=='125b' or a=="200b":#or a== '48' or a=='95' or a=="120"or a=='210' or a=="360" or a== '50' or a=='100' or a=="135"or a=='240' or a=="450":
    query.answer()
    if a=='25b':
        dd=1
        pp=25
    elif a=='50b':
        dd=2
        pp=50
    elif a=='70b':
        dd=3
        pp=70
    elif a=='125b':
        dd=6
        pp=125
    elif a=='200b':
        dd=12
        pp=200
    ham="BTC"
    charge = client.charge.create(name='Nation Forex Signals',
                          description="Nation Forex Signals",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pp,
                             "currency": "USD"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,"2")) 
    conn.commit()
    keyboard = [[InlineKeyboardButton("Make a Payment", url=linka)],
                [InlineKeyboardButton("🔙 Cancel", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=dd)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}',amount='{}' where ID = {}".format(coda,dat,pp,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation",reply_markup=reply_markup)
    return BUTTON
  elif  a== '50c' or a=='100c' or a=="135c" or a=='240c' or a=="450c":#or a== '48' or a=='95' or a=="120"or a=='210' or a=="360" or a== '50' or a=='100' or a=="135"or a=='240' or a=="450":
    query.answer()
    if a=='50c':
        dd=1
        pp=50
    elif a=='100c':
        dd=2
        pp=100
    elif a=='135c':
        dd=3
        pp=135
    elif a=='240c':
        dd=6
        pp=240
    elif a=='450c':
        dd=12
        pp=450
    ham="BTC"
    charge = client.charge.create(name='Nation Forex Signals',
                          description="Nation Forex Signals",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pp,
                             "currency": "USD"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,"3")) 
    conn.commit()
    keyboard = [[InlineKeyboardButton("Make a Payment", url=linka)],
                [InlineKeyboardButton("🔙 Cancel", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=dd)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}',amount='{}' where ID = {}".format(coda,dat,pp,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation",reply_markup=reply_markup)
    return BUTTON
 
  elif  a== '48f' or a=='95f' or a=="120f" or a=='210f' or a=="360f":#or a== '48' or a=='95' or a=="120"or a=='210' or a=="360" or a== '50' or a=='100' or a=="135"or a=='240' or a=="450":
    query.answer()
    if a=='48f':
        dd=1
        pp=48
    elif a=='95f':
        dd=2
        pp=95
    elif a=='120f':
        dd=3
        pp=120
    elif a=='210f':
        dd=6
        pp=210
    elif a=='360f':
        dd=12
        pp=360
    ham="BTC"
    charge = client.charge.create(name='Nation Forex Signals',
                          description="Nation Forex Signals",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pp,
                             "currency": "USD"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,"4")) 
    conn.commit()
    keyboard = [[InlineKeyboardButton("Make a Payment", url=linka)],
                [InlineKeyboardButton("🔙 Cancel", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user=int(update.effective_user.id)
    dat= date.today() + relativedelta(months=dd)
    conn = sqlite3.connect('sql.db')
    conn.execute("UPDATE COMPANY set Trx = '{}',exp='{}',amount='{}' where ID = {}".format(coda,dat,pp,user))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_user.id,text="Click on 'Make a Payment' button\n\n""After making payment wait for 30 minutes to wait for the confirmation of transcation",reply_markup=reply_markup)
    return BUTTON
  
  elif a== '6':
    query.answer()
    keyboard = [[InlineKeyboardButton("VIP SPOT", callback_data='11'),InlineKeyboardButton("VIP FUTUROS", callback_data='22')],[InlineKeyboardButton("VIP ELITE", callback_data='44'),InlineKeyboardButton("VIP spot+ VIP Futuros", callback_data='33a')],[InlineKeyboardButton("Refferal", callback_data='qre')]] 
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON
  elif a== 'qre':

    connection = sqlite3.connect("sql.db")  
    cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
    for names in cursor:
      da=names[1]  
    ab='https://t.me/CPMBOT_BOT?start={}'.format(str(update.effective_user.id))
    vfg="Your Refferal Link: {}\nTotal Refferals: {}\nTotal Referral Balance: {}USDT".format(ab,da,names[2])
    keyboard =[[InlineKeyboardButton("Withdraw", callback_data='69')],[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text=vfg,reply_markup=reply_markup)
  elif a== '69':

    connection = sqlite3.connect("sql.db")  
    cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
    for names in cursor:
        da=float(names[1]) 
        if da<=50:
            context.bot.send_message(chat_id=update.effective_user.id,text="Send your wallet address")
            return VBNM
        else:
            keyboard =[[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
            context.bot.send_message(chat_id=update.effective_user.id,text="Your balance is less than 50 USDT",reply_markup=reply_markup)
            return BUTTON
     
      
  elif a== '11':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (25 USDT)", callback_data='25a')],[InlineKeyboardButton("2 MESES (50 USDT)", callback_data='50a')],[InlineKeyboardButton("3 MESES (70 USDT)", callback_data='70a')],[InlineKeyboardButton("6 MESES (125 USDT)", callback_data='125a')],[InlineKeyboardButton("12 MESES (200 USDT)", callback_data='200a')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '22':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (25 USDT)", callback_data='25b')],[InlineKeyboardButton("2 MESES (50 USDT)", callback_data='50b')],[InlineKeyboardButton("3 MESES (70 USDT)", callback_data='70b')],[InlineKeyboardButton("6 MESES (125 USDT)", callback_data='125b')],[InlineKeyboardButton("12 MESES (200 USDT)", callback_data='200b')]]  
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
    keyboard = [[InlineKeyboardButton("1 MES (48 USDT)", callback_data='48f')],[InlineKeyboardButton("2 MESES (95 USDT)", callback_data='95f')],[InlineKeyboardButton("3 MESES (120 USDT)", callback_data='120f')],[InlineKeyboardButton("6 MESES (210 USDT)", callback_data='210f')],[InlineKeyboardButton("12 MESES (360 USDT)", callback_data='360f')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
  elif a== '44':
    query.answer()      
    keyboard = [[InlineKeyboardButton("1 MES (50 USDT)", callback_data='50c')],[InlineKeyboardButton("2 MESES (100 USDT)", callback_data='100c')],[InlineKeyboardButton("3 MESES (10% OFF) (135 USDT)", callback_data='135c')],[InlineKeyboardButton("6 MESES (20% OFF) (240 USDT)", callback_data='240c')],[InlineKeyboardButton("12 MESES (35% OFF) (450 USDT)", callback_data='450c')]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Select you package:",reply_markup=reply_markup)
    return BUTTON 
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
    msg=update.message.text
    connection = sqlite3.connect("sql.db")  
    cursor = connection.execute("SELECT id,tref,balance FROM COMPANY where id={}".format(update.effective_user.id))
    for names in cursor:
        da=float(names[1]) 
        keyboard =[[InlineKeyboardButton("Accept", callback_data='6ac'),InlineKeyboardButton("Reject", callback_data='6re')]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
        context.bot.send_message(chat_id=1553553750,text="Withdrawal Reqest:\nWallet Address: {}\nAmount: {}\nUserID: {}".format(msg,names[2],update.effective_user.id),reply_markup=reply_markup)
    keyboard =[[InlineKeyboardButton("🔙 Main Menu", callback_data='6')]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True) 
    context.bot.send_message(chat_id=update.effective_user.id,text="Withdrawl Request sent",reply_markup=reply_markup)
    return BUTTON


def callback_minut(context):
  
    connection = sqlite3.connect("sql1.db")  
    cursor = connection.execute("SELECT id,exp FROM COMPANY ")
    for names in cursor:
      da=names[1]
      idd=names[0]
    if da !="0":
        x= date.today() + relativedelta(months=0)
        y=da
        print(x)
        print(y)
        x=str(x)
        y=str(y)

        if x>y:
            conn = sqlite3.connect('sql1.db')
            conn.execute("UPDATE COMPANY set  exp= '0' where ID = {}".format(int(idd)))
            conn.commit()
            conn.close()
            vb=dt.datetime.now().utcnow() + dt.timedelta(minutes =2)
            try:
              context.bot.kick_chat_member(chat_id=-1001194157852,user_id=int(idd),until_date=vb)
            except:
                pass
            try:
              context.bot.kick_chat_member(chat_id=-1001314484558,user_id=int(idd),until_date=vb)
            except:
                pass

            context.bot.send_message(chat_id=int(idd),text="renew your subscription to join again")
        elif x==y:
          context.bot.send_message(chat_id=int(idd),text="today is last date of you subsription update it otherwise you will be remove tomorrow")

def main():#1295846107
  updater = Updater("5250391975:AAEWHIBHS-5f5Cwtxa5M9z_dwIB2o1VhCAY", use_context=True)
  dp = updater.dispatcher
  dp.job_queue.run_repeating(callback_minut, 10666)
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
        
            BUTTON: [CallbackQueryHandler(button)],
            VBNM: [MessageHandler(Filters.text, vbnm),CallbackQueryHandler(button)],
        },
        fallbacks=[CommandHandler('start', start)]
    )
  dp.add_handler(conv_handler)
  
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()