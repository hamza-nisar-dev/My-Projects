from flask import Flask, request, abort
import sqlite3
import paypalrestsdk
from paypalrestsdk import BillingAgreement
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Bot
import datetime as dt
app = Flask(__name__)
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "AQZOPuRug5f8YVWnodKfKW66HagDEw-8I_F5r-8HI7zmkGB90RWi9IsEewH7zRzDPVcx7M02gD_uggIU",
  "client_secret": "EPnax0sjn4INvphP-kLGaRYVP3VxkMsDaF4itJBkJXe9dQ9jtyGPiC2WOPR-bz0FfyGANWNS1dgPsbx3" })
bot=Bot("5456714021:AAGRaiRHwveqWyPRoh2uFx3HRA3yDkhAdOc")

@app.route('/subscribe', methods=['GET'])
def subscribe():
    try:
        rn(request.args.get('token'))
        return 'Success', 200 
    except Exception as e:
        rn(request.args.get('token'))
        return 'Success', 200

def rn(cn):
        print(cn)
        billing_agreement_response = BillingAgreement.execute(cn)
        id=billing_agreement_response.id
        print(id)
        conn = sqlite3.connect('paypal.db')  
        cursor = conn.execute("SELECT id,pkg FROM COMPANY where ptoken='{}'".format(cn))
        for names in cursor:
            ida=names[0]
            pkg=names[1]
        conn = sqlite3.connect('agreement.db')
        conn.execute("INSERT INTO COMPANY (ID,agree_id,pkg) \
            VALUES ('{}','{}','{}')".format(ida,id,pkg))
        conn.commit()
        exp=dt.datetime.now().utcnow() + dt.timedelta(days=7)
        c=bot.createChatInviteLink(chat_id= -1001573013348, expire_date=exp,member_limit=1)
        link=c['invite_link']
        keyboard = [[InlineKeyboardButton("Better Winnings Premium", url=link)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=ida,text="\n\n.Please click the button below to join Channel" 
                ,reply_markup=reply_markup)


if __name__ == '__main__':
    app.run()