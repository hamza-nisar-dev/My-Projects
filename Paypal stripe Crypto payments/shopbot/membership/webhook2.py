import requests
from flask import Flask, request, abort
from coinbase_commerce.webhook import Webhook
import sqlite3
from datetime import  timedelta
from datetime import date
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram import Bot
import datetime as dt
app = Flask(__name__)
bot=Bot("5355429117:AAHlnPrVKP2pxApPQHGwvkcDJUb8M2h96AI")
@app.route('/crypto', methods=['POST'])
def crypto():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        request_sig = request.headers.get('X-CC-Webhook-Signature', None)
        event = Webhook.construct_event(request_data, request_sig,"db942c51-c0b3-45b5-a12e-fa26452f0aa8")
        et=event.type
        ko=event.data.id
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.execute("SELECT pkg,id FROM COMPANY where code='{}'".format(ko))
        for names in cursor:
            pkg=names[0]
            ida=names[1]
        if et=="charge:confirmed":
                print(ida)
                if pkg=="1":
                    b = date.today() + timedelta(days=30)

                elif pkg=="3":
                    b = date.today() + timedelta(days=180)

                elif pkg=="4":
                    b = date.today() + timedelta(days=365)
                conn = sqlite3.connect("kick.db")  
                conn.execute("UPDATE COMPANY set date='{}' where ID = '{}'".format(b,int(ida)))
                conn.commit()
                conn.close()
                exp=dt.datetime.now().utcnow() + dt.timedelta(days=7)
                c=bot.createChatInviteLink(chat_id=-1001694721234, expire_date=exp,member_limit=1)
                link=c['invite_link']
                keyboard = [[InlineKeyboardButton("CryptoNova ® (VIP)", url=link)]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.send_message(chat_id=ida,text="Thank you for your payment\n.Please click the button below to join Channel" 
                        ,reply_markup=reply_markup)
        elif et=="charge:pending":
            bot.send_message(chat_id=ida,text="Your transcation is pending will be added on confirmation") 
    return 'success', 200
if __name__ == '__main__':
    app.run()