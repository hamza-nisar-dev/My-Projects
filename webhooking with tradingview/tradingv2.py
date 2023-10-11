import requests
from flask import Flask, request, abort
from coinbase_commerce.webhook import Webhook
import sqlite3
import datetime
from datetime import date
from datetime import datetime, timedelta
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import Bot
app = Flask(__name__)
bot=Bot("5122807155:AAF_lbNoN-iASPQkmYdkzw8vd7Jxt7mnj34")
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        request_sig = request.headers.get('X-CC-Webhook-Signature', None)
        event = Webhook.construct_event(request_data, request_sig,"7bc8a810-e8ae-45b0-8d9f-77de729bcb55")
        et=event.type
        ko=event.data.id
        am=event.data.payments
        d=am[0]
        em=d['net']["local"]["amount"]
        et=str(et)
        print(em)
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.execute("SELECT pkg,id FROM COMPANY where code='{}'".format(ko))
        for names in cursor:
            pkg=names[0]
            ida=names[1]
        if et=="charge:confirmed":
                if pkg=="1":
                  b = date.today() + timedelta(days=30)
                elif pkg=="2":
                  b = date.today() + timedelta(days=90)
                else:
                  b = date.today() + timedelta(days=365)
            
                conn = sqlite3.connect("kick.db")  
                conn.execute("UPDATE COMPANY set date='{}', where ID = '{}'".format(b,int(ida)))
                conn.commit()
                conn.close()
                exp=datetime.datetime.now().utcnow() + datetime.timedelta(days=7)
                c=bot.createChatInviteLink(chat_id= -1001365652718, expire_date=exp,member_limit=1)
                link=c['invite_link']
                keyboard = [[InlineKeyboardButton("Le cercle (Signaux) - Premium", url=link)]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.send_message(chat_id=ida,text="Thank you for your payment\n.Please click the button below to join Channel" 
                        ,reply_markup=reply_markup)
        else:
            bot.send_message(chat_id=ida,text="Your transcation is pending will be added on confirmation")

            

 
    return 'success', 200

if __name__ == '__main__':
    app.run()