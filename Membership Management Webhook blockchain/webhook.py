from flask import Flask, request, abort
from coinbase_commerce.webhook import Webhook
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Bot

app = Flask(__name__)

bot=Bot("5250391975:AAEWHIBHS-5f5Cwtxa5M9z_dwIB2o1VhCAY")

@app.route('/crypto', methods=['POST'])
def crypto():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        request_sig = request.headers.get('X-CC-Webhook-Signature', None)
        event = Webhook.construct_event(request_data, request_sig,"ea9d1d36-95ec-4be1-84b2-9c4ec20999dd")
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
                  cc="VIP SPOT"
                  ff="https://t.me/+TECfU89pyqZmODlh"
                elif pkg=="2":

                  cc="VIP futuros"
                  ff="https://t.me/+etQDXTrpLTsyZTcx"

                elif pkg=="3":
                  cc="VIP ELITE"
                  ff="https://t.me/+NLkItvDdJXI0YWIx"
                elif pkg=="4":
                  cc="Trading Signal Channel"
                  ff="https://t.me/+TECfU89pyqZmODlh"
       
                conn = sqlite3.connect('sql.db')
                cursor = conn.execute("SELECT exp,refby,amount from COMPANY where ID= {}".format(ida))
                for names in cursor:
                    inv=names[0]
                    asf=names[1]
                    cds=float(names[2])
                    fgh=10/100
                    fgh=cds*fgh  
                    fgh=float(fgh)
                    cursor = conn.execute("SELECT balance from COMPANY where ID={}".format(int(asf)))
                    conn.commit() 
                    for row in cursor:
                        bn=float(row[0])
                        bn=bn+fgh
                        cursor = conn.execute("UPDATE COMPANY set balance='{}' where ID='{}' ".format(bn,asf))
                        conn.commit() 
                conn = sqlite3.connect('sql.db')
                conn.execute("UPDATE COMPANY set Trx='0' where ID = {}".format(ida))
                conn.commit()
                conn.close()
                conn = sqlite3.connect('sql1.db')
                conn.execute("UPDATE COMPANY set exp='{}' where ID = {}".format(inv,ida))
                conn.commit()
                conn.close()
                keyboard = [[InlineKeyboardButton(cc, url=ff)]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.send_message(chat_id=ida,text="Thank you for your payment\n.Please click the button below to join Channel" 
                        ,reply_markup=reply_markup)

        elif et=="charge:pending":
            bot.send_message(chat_id=ida,text="Your transcation is pending will be added on confirmation")

            

 
    return 'success', 200
if __name__ == '__main__':
    app.run()