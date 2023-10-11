import logging

from telegram import LabeledPrice, ShippingOption
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
import telegram.ext
import sqlite3
import os  
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
import datetime
from datetime import date
from datetime import datetime, timedelta
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from coinbase_commerce.client import Client
API = ["5290b02a-b0f1-416b-ab43-3873cce15a32"]

def start(update, context):
  user = update.message.from_user
  usa=user.first_name
  keyboard = [[InlineKeyboardButton("Abonnement 1 mois 50€", callback_data='1')],[InlineKeyboardButton("- Abonnement 3 mois 120€", callback_data='2')],[InlineKeyboardButton("- Abonnement 1 an 400€", callback_data='3')],[InlineKeyboardButton("Le Cercle (Signaux) - Free", url='https://t.me/lecerclefx')]]  
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
  key=[["Acheter un accès","Mon profil"],['À propos du Cercle','Contactez-nous']]
  reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Hello {}\nBienvenue sur le bot du Cercle. Ici tu pourras acheter ton abonnement afin de recevoir tous mes signaux Forex !".format(usa),reply_markup=reply_marku)
#  context.bot.send_message(chat_id=update.effective_user.id,text="Bienvenue sur le bot du Cercle. Ici tu pourras acheter ton abonnement afin de recevoir tous mes signaux Forex !",reply_markup=reply_markup)
  conn = sqlite3.connect('kick.db')
  cursor = conn.cursor()
  cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
    conn = sqlite3.connect('kick.db')
    conn.execute("INSERT INTO COMPANY (ID,date,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),"0","0")) 
    conn.commit()
 
 

def gender(update, context):
    c=update.message.text
    if c=="Acheter un accès":
      keyboard = [[InlineKeyboardButton("Abonnement 1 mois 50€", callback_data='1')],[InlineKeyboardButton("- Abonnement 3 mois 120€", callback_data='2')],[InlineKeyboardButton("- Abonnement 1 an 400€", callback_data='3')]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Bienvenue sur le bot du Cercle. Ici tu pourras acheter ton abonnement afin de recevoir tous mes signaux Forex !",reply_markup=reply_markup)
    elif c=="Contactez-nous":
      context.bot.send_message(chat_id=update.effective_user.id,text="Pour toute question technique ou autre concernant le projet, veuillez me contacter @lecerclesupport")
    elif c=='À propos du Cercle':
      context.bot.send_message(chat_id=update.effective_user.id,text="A propos de nous :\n➡️Ce Bot de signaux fournit tous mes trades, y compris toutes les mises à jour sur mes trades. Je poste également des analyses techniques et fondamentales. \n💯Tous les trades et analyses sont pris uniquement par moi (mon instagram est @lecerclefx) et restent entièrement authentiques. \n‼️Veuillez ne PAS partager/transférer les messages de ce Bot, car ce Bot suit tous les messages renvoyés et si vous le faites, vous serez bloqué, alors aucun remboursement ne sera possible. \n💸Estimation du nombre de transactions : 5-20 trades par semaine. \n📈 Habituellement, nous gagnons 2000-4000 pips par mois.\n🚀Bienvenue dans la communauté du Cercle🚀\n\nLES REMBOURSEMENTS NE SONT PAS DISPONIBLES\nComme notre service est un type de conseil et nous opérons avec les marchés à haut risque, veuillez accepter le fait que le remboursement de l’abonnement n’est pas possible.\n\nPAIEMENTS RÉCURRENTS\nAprès avoir effectué le paiement par carte, vous vous inscrivez automatiquement au paiement récurrent de votre abonnement. Vous pouvez annuler les paiements récurrents en appuyant sur votre bouton Profil dans @bot, après Paiements récurrents, choisissez l'abonnement et annulez-le ! Si vous avez des questions, veuillez contacter le support à @lecerclesupport\n\nACCORD DE PAIEMENT - DÉNI DE RESPONSABILITÉ\nEn acceptant le paiement, chaque Client doit estimer que le service est prévu d'être fourni lors de l'ajout au Canal. \nLes résultats des signaux précédents ne signifient pas le succès des signaux futurs. Tous les signaux de trading sont fournis à titre de suggestions. Veuillez trader à vos propres risques !")
    
    else:
        connection = sqlite3.connect("kick.db")  
        cursor = connection.execute("SELECT date FROM COMPANY where id='{}'".format(update.effective_user.id))
        for names in cursor:
            da=names[0]
        if da !="0":
          keyboard = [[InlineKeyboardButton("Abonnement 1 mois 50€", callback_data='1')],[InlineKeyboardButton("- Abonnement 3 mois 120€", callback_data='2')],[InlineKeyboardButton("- Abonnement 1 an 400€", callback_data='3')],[InlineKeyboardButton("Le Cercle (Signaux) - Free", url='https://t.me/lecerclefx')]]
          reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
          context.bot.send_message(chat_id=update.effective_user.id,text="Vous avez 1 abonnement actif :\n\nDate d'expiration : {}\n\nCliquez sur le bouton ci-dessous pour renouveler l'abonnement".format(da),reply_markup=reply_markup)
        else:
          context.bot.send_message(chat_id=update.effective_user.id,text="Vous n'avez pas d'abonnement actif")
def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  client = Client(api_key=API[0])
  if a== '1' or a=='2' or a=='3':
    if a=='1':
        keyboard = [[InlineKeyboardButton("Carte de crédit/débit", callback_data='111')],[InlineKeyboardButton("Crypto", callback_data='11')]]  
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Choisissez votre méthode de paiement:",reply_markup=reply_markup)
    elif a=='2':
        keyboard = [[InlineKeyboardButton("Carte de crédit/débit", callback_data='222')],[InlineKeyboardButton("Crypto", callback_data='22')]]  
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Choisissez votre méthode de paiement",reply_markup=reply_markup)
    else:
        keyboard = [[InlineKeyboardButton("Carte de crédit/débit", callback_data='333')],[InlineKeyboardButton("Crypto", callback_data='33')]]  
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Choisissez votre méthode de paiement:",reply_markup=reply_markup)
  elif a=="22" or a=="11" or a=="33":
    if a=="11":
        c=50
        d=1
    elif a=="22":
        c=120
        d=2
    else:
        c=400
        d=3
    charge = client.charge.create(name='Le Cercle premium',
                          description="Effectuez votre paiement en cryptomonnaie afin d'avoir accès au groupe premium",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": c,
                             "currency": "EUR"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,d)) 
    conn.commit()
    keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Achetez la cryptomonnaie de votre choix (BTC, ETH, USDC, DOGE, LTC, DAI, BCH) pour le montant mentionné. Si vous ne savez pas comment acheter des cryptomonnaies, voici les services recommandés pour le faire :\n- Coinbase.com\n- Binance.com\n- Localbitcoins.com\n- Blockchain.com\n- Crypto.com\nTout service ou portefeuille est adapté à notre système.\nEnvoyez les cryptomonnaies à l'adresse mentionnée.\nDès que la transaction sera validée et le paiement reçu, vous recevrez automatiquement votre accès au groupe VIP.\n\nCliquez sur le bouton ci-dessous pour effectuer le paiement",reply_markup=reply_markup)
  elif a=="111" or a=='222' or a=='333':
    if a=="111":
        c=50
        d=1
    elif a=="222":
        c=120
        d=2
    else:
        c=400
        d=3
    
    title = "Le cercle (Signaux) - Premium"
    description = "Ce bot permet d’accéder à tous mes signaux de trading, ainsi que les updates de mes trades. Tous les trades, résultats et analyses techniques sont les miens. Mon instagram est @lecerclefx."
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    provider_token = "350862534:LIVE:MzFhNWNiOTZiYjQ3"
    currency = "EUR"
    price = c
    prices = [LabeledPrice("Le cercle (Signaux)", price * 100)]
    context.bot.send_invoice(
       update.effective_user.id,  title, description, payload, provider_token, currency, prices
    )
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set pkg ='{}' where ID = '{}'".format(d,int(update.effective_user.id)))
    conn.commit()
    conn.close()

def callback_minut(context: telegram.ext.CallbackContext):
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
                conn = sqlite3.connect("kick.db")  
                conn.execute("UPDATE COMPANY set pkg ='0',date='0' where ID = '{}'".format(int(da)))
                conn.commit()
                conn.close()
                print(da)
                vb=datetime.datetime.now().utcnow() + datetime.timedelta(minutes =2)
                try:
                 context.bot.kick_chat_member(chat_id=-1001365652718,user_id=int(da),until_date=vb)
                except:
                  pass
                keyboard = [[InlineKeyboardButton("Abonnement 1 mois 50€", callback_data='1')],[InlineKeyboardButton("- Abonnement 3 mois 120€", callback_data='2')],[InlineKeyboardButton("- Abonnement 1 an 400€", callback_data='3')],[InlineKeyboardButton("Le Cercle (Signaux) - Free", url='https://t.me/lecerclefx')]]    
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                context.bot.send_message(chat_id=str(da),text="you are removed from group. Click on below button to renew the service",reply_markup=reply_markup)            
            elif x==y:
              keyboard = [[InlineKeyboardButton("Abonnement 1 mois 50€", callback_data='1')],[InlineKeyboardButton("- Abonnement 3 mois 120€", callback_data='2')],[InlineKeyboardButton("- Abonnement 1 an 400€", callback_data='3')],[InlineKeyboardButton("Le Cercle (Signaux) - Free", url='https://t.me/lecerclefx')]]   
              reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
              context.bot.send_message(chat_id=str(da),text="today is last date of your subsription. Update it otherwise you will be removed tomorrow\n\nClick on below button to renew the service")
          except:
            pass
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        query.answer(ok=True)

def successful_payment_callback(update, context):
    connection = sqlite3.connect("kick.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT pkg FROM COMPANY where id= '{}'".format(int(update.effective_user.id)) )
    for names in cursor:
      pkg=names[1]
    if pkg=="1":
      b = date.today() + timedelta(days=30)
    elif pkg=="2":
      b = date.today() + timedelta(days=90)
    else:
        b = date.today() + timedelta(days=365)

    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set date='{}', where ID = '{}'".format(b,int(update.effective_user.id)))
    conn.commit()
    conn.close()
    exp=datetime.datetime.now().utcnow() + datetime.timedelta(days=7)
    c=context.bot.createChatInviteLink(chat_id= -1001365652718, expire_date=exp,member_limit=1)
    link=c['invite_link']
    keyboard = [[InlineKeyboardButton("Le cercle (Signaux) - Premium", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Thank you for your payment\n.Please click the button below to join Channel" 
            ,reply_markup=reply_markup)
             

def main():
    updater = Updater("5122807155:AAF_lbNoN-iASPQkmYdkzw8vd7Jxt7mnj34", use_context=True)
    dp = updater.dispatcher
    dp.job_queue.run_repeating(callback_minut, 86400)
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
    dp.add_handler(MessageHandler(Filters.regex('^(Acheter un accès|Mon profil|Contactez-nous|À propos du Cercle)$'), gender))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()