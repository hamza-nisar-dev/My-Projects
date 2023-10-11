
import telegram.ext
from paypalrestsdk import Payment
import telegram.ext
from telegram import LabeledPrice, ShippingOption
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt
import paypalrestsdk
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
from datetime import datetime
from paypalrestsdk import BillingPlan, ResourceNotFound
from paypalrestsdk import BillingAgreement
from datetime import datetime, timedelta
import sqlite3
from paypalrestsdk import BillingAgreement
from datetime import date
from dateutil import parser
GEND= range(1)
from coinbase_commerce.client import Client
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "AXhC301fBtxP4YFx5K_BXXPg9SG0zo_ZzbqyIYrreQO7Zy578XWoPKAKQ4N6LBebxZwsPCg-zEQ53cXt",
  "client_secret": "EIi74r61Qt6wzuK0pxQNFIl3I-Ws1uWzWTaK_6CpTXpv08M9Abc7MEt9VZd0-tFSTA0Fm0jcAzF-otPn" })
API = ["c48f4562-d41a-4de1-ba2d-5c7ad54f603e"]
def start(update, context):
  conn = sqlite3.connect('kick.db')
  cursor = conn.cursor()
  cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:

    user = update.message.from_user
    usa=user.username
    usaa=user.first_name
    conn = sqlite3.connect('kick.db')
    conn.execute("INSERT INTO COMPANY (ID,date,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),"0","0")) 
    conn.commit()
    context.bot.send_message(chat_id=1991527010,text="{} start the bot for the first time\n\nID: {}\n\nUsername: {}".format(usaa,update.effective_user.id,usa))
  keyboard = [[InlineKeyboardButton("English 🇬🇧", callback_data='1'),InlineKeyboardButton("Español 🇪🇸", callback_data='2')],[InlineKeyboardButton("Italiano 🇮🇹", callback_data='3'),InlineKeyboardButton("Deutsche 🇩🇪", callback_data='4')],[InlineKeyboardButton("Français 🇫🇷", callback_data='5')]]  
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Please Select Your Language",reply_markup=reply_markup)
def cagree(pid):
    if pid=="P-3MA17355GS4821530LTWXCNQ":
        cc="🔑 1 WEEK VIP ACCESS🔑"
    elif pid=="P-3GV94404VX052992JLTXSORQ":
        cc="🔑 1 MONTH VIP ACCESS🔑"
    elif pid=="P-0AD21827NA8127730LTX7I6I":
        cc="🔑 3 MONTH VIP ACCESS🔑"
    elif pid=="P-16M45158DE9586719LTYOSKY":
        cc="🔑 6 MONTH VIP ACCESS🔑"
    a=(datetime.now()+ timedelta(hours=1)).replace(microsecond=0).isoformat()
    a=a+"Z"
    billing_agreement = BillingAgreement({
        "name": "NationForexSignals",
        "description": cc,
        "start_date": a,
        "plan": {
            "id": pid
        },
        "payer": {
            "payment_method": "paypal"
        }
    })
    if billing_agreement.create():
        for link in billing_agreement.links:
            if link.rel == "approval_url":
                approval_url = link.href
                return approval_url
    else:
        print(billing_agreement.error)
def ilife():
    

    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "https://0bb2-2a01-4f8-242-43c3-00-1d28-8501.eu.ngrok.io/lifetime",
            "cancel_url": "https://t.me/NationForexSignals_bot"},

        "transactions": [{

            "amount": {
                "total": "149.99",
                "currency": "EUR"},
            "description": "🔑 LIFETIME ACCESS VIP 🔑  €149.99"}]})

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
        c="{}***{}".format(payment.id,approval_url)
        return c
def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  client = Client(api_key=API[0])
  if a== '1' or a=="2" or a=="3" or a=="4" or a=="5":
    conn = sqlite3.connect('lang.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        conn = sqlite3.connect('lang.db')
        conn.execute("INSERT INTO COMPANY (ID,lang) \
                VALUES ('{}','{}')".format(int(update.effective_user.id),a)) 
        conn.commit()
    else:
        conn = sqlite3.connect("lang.db")  
        conn.execute("UPDATE COMPANY set lang='{}' where ID = '{}'".format(a,int(update.effective_user.id)))
        conn.commit()
        conn.close()

    if a=="1":
        keyboard = [[InlineKeyboardButton("🔑 1 WEEK ACCESS VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONTHS ACCESS VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONTHS ACCESS VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
        text='<b>Welcome to NationForexSignals 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n<b>Forex & Indices Included</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Quality signals \n✅ Weekly report\n✅ Signals update (Example: <a href="https://prnt.sc/1xmfvuo">Update</a>)\n✅ Indices included (US30, NASDAQ and more)\n✅ Strategies (<a href="https://prnt.sc/1xmfjy0">Scalping</a>, <a href="https://prnt.sc/1xmfqd0">Intraday</a>, <a href="https://prnt.sc/1xmfrm4">MultiDay</a>, <a href="https://prnt.sc/1xmft9s">Cycle</a> )\n✅ Market news to avoid risk of loss (Example: <a href="https://prnt.sc/1xmfbqh">Risk</a>)\n✅ Money management (Guide Excel)\n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicators included \n\n<b>Example Signal:</b>\nXAUUSD SELL\nENTRY: 1789.40\nSL:  1799.00\nTP:  1765.00\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply type /status to the bot.\n\nPlease select your subscription plan:'
        key=[["VIP ROOM - PREMIUM SIGNALS  🔑","COPYTRADING  🗝"],["SUPPORT 🛎  🔑","SUBCRIPTION STATUS 📌"],["Change Language"]]
    elif a=="2":
        keyboard = [[InlineKeyboardButton("🔑 1 SEMANA DE ACCESO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MES DE ACCESO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESES DE ACCESO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESES DE ACCESO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESO VIP🔥€149.99", callback_data='p5')]]  
        key=[["SALAS VIP - SEGNALES PREMIUM 🔑","COPYTRADING 🗝"],["SOPORTE 🛎","STATUS ABONADO 📌"],["Change Language"]]
        text="<b>Bienvenido a NationForexSignals 👋</b>\n\n¡Compre su <u>plan</u> en solo <b>60 segundos!</b>\n\nDespués de realizar la compra, el bot le dará el enlace para acceder a la sala VIP.\n\n<b>Forex e índices incluidos</b>\n<b>(60% de descuento) 💡</b>\n\n✅ Señales de calidad \n✅ Informe semanal\n✅ Actualización de señales (Ejemplo: Actualización (<a href='https://prnt.sc/1xmfvuo'>Actualización</a>)\n✅ Índices incluidos (US30, NASDAQ y más)\n✅ Estrategias  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intradiario</a>, <a href='https://prnt.sc/1xmfrm4'>Varios días</a>, <a href='https://prnt.sc/1xmft9s'>Ciclo</a>)\n✅ Noticias del mercado para evitar el riesgo de pérdida (Ejemplo: <a href='https://prnt.sc/1xmfbqh'>Riesgo</a>)\n✅ Administración del dinero (Guía Excel)\n✅ Chat de soporte @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicadores incluidos \n\n<b>Ejemplo</b> de señal:\nXAUUSD SELL\nENTRY: 1789.40\nSL: 1799.00\nTP: 1765.00\n\n🔰👇 Seleccione su plan a continuación, conviértase en miembro Elite👇🔰\n\n✖️Cancele la suscripción en cualquier momento✖️\nPara cancelar o verificar el estado de la suscripción, simplemente escriba /status en el bot.\n\nSeleccione su plan de suscripción:"
    elif a=="3":
        keyboard = [[InlineKeyboardButton("🔑 1 SETTIMANA ACCESSO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MESE ACCESSO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESI ACCESSO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESI ACCESSO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESSO VIP🔥€149.99", callback_data='p5')]]  
        key=[["SALA VIP - SEGNALI PREMIUM  🔑","COPYTRADING  🗝"],["SUPPORTO 🛎","STATO ABBONAMENTO 📌"],["Change Language"]]
        text="<b>Benvenuto su NationForexSignals 👋</b>\n\nCompra il tuo <u>piano</u> in <b>60 secondi!</b>\n\nDopo aver effettuato l'acquisto il bot ti darà il link per accedere alla sala VIP!\n\n<b>Forex & Indici inclusi!</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualità dei segnali \n✅ Report settimanale \n✅ Aggiornamenti Segnali (Esempio: <a href='https://prnt.sc/1xmfvuo'>Update</a>) \n✅ Indici Inclusi (US30, NASDAQ. e altro) \n✅ Strategie  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a> )\n✅ Notizie di mercato, per evitare rischi sul conto (Esempio: <a href='https://prnt.sc/1xmfbqh'>Risk</a>) \n✅ Guida al Money Management (Guide Excel) \n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicatori inclusi \n\n<b>Esempio</b> Segnale: \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Seleziona il tuo piano qui sotto, Diventa un Membro Elite👇🔰 \n\n✖️Cancella l'abbonamento in qualsiasi momento✖️ \nPer cancellare o controllare lo stato dell'abbonamento, basta digitare /status al bot. \n\nSeleziona il tuo piano di abbonamento:"
    elif a=="4":
        keyboard = [[InlineKeyboardButton("🔑 1 WOCHE ZUGANG VIP 🔑 €19,99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONAT ZUGANG VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONATE ZUGANG VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONATE ZUGANG VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
        key=[["VIP-RAUM - PREMIUM-SIGNALE 🔑","COPYTRADING 🗝"],["UNTERSTÜTZUNG 🛎","ABONNEMENT STATUS 📌"],["Change Language"]]
        text="<b>Willkommen bei Nation Forex Signals 👋</b>\n\nKaufen Sie Ihren <u>plan</u> in nur <b>60 Sekunden!</b>\n\nNachdem Sie den Kauf getätigt haben, gibt Ihnen der Bot den <b>Link zum VIP-Raum!</b>\n\n<b>Forex & Indizes enthalten</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualitätssignale \n✅ Wöchentlicher Bericht \n✅ Signalaktualisierung (Beispiel: <a href='https://prnt.sc/1xmfvuo'>Update</a>)\n✅ Einschliesslich Indizes (US30, NASDAQ und mehr) \n✅ Strategien (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Zyklus</a>) \n✅ Marktnachrichten zur Vermeidung von Verlustrisiken (Beispiel: <a href='https://prnt.sc/1xmfbqh'>Risiko</a>) \n✅ Geldverwaltung (Excel-Leitfaden) \n✅ Support-Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Inbegriffene Indikatoren \n\n<b>Beispiel signal:</b> \nXAUUSD SELL \nENTRY: 1789.40 \nSL: 1799,00 \nTP: 1765,00 \n\n🔰👇Wählen Sie Ihren Plan unten, Werden Sie ein Elite-Mitglied 👇🔰 \n\n✖️Abonnement jederzeit kündigen✖️ \nUm den Abonnementstatus zu kündigen oder den Abonnementstatus zu überprüfen, tippen Sie einfach /status in den Bot ein. \n\nBitte wählen Sie Ihr Abonnement:"
    else:
        keyboard = [[InlineKeyboardButton("🔑 1 SEMAINE D'ACCÈS VIP 🔑 19,99€", callback_data='p1')],[InlineKeyboardButton("🔑 1 MOIS D'ACCÈS VIP 🔑 34,99€", callback_data='p2')],[InlineKeyboardButton("🔑 3 MOIS D'ACCÈS VIP 🔑 74,99€", callback_data='p3')],[InlineKeyboardButton("🔑 6 MOIS D'ACCÈS VIP 🔑 109,99€", callback_data='p4')],[InlineKeyboardButton("🔥 ACCÈS À LIFETIME  🔥149,99€", callback_data='p5')]]  
        key=[["SALLE VIP - SEGNALIS PREMIUM 🔑","COPYTRADING 🗝"],["SUPPORTS 🛎","STATUT ABONNEMENT 📌"],["Change Language"]]
        text="<b>Bienvenue sur Nation Forex Signals 👋</b>\n\nAchetez votre abonnement en <b>60 secondes seulement !</b>\n\nAprès avoir effectué l'achat, le robot vous donnera le lien pour accéder à la salle VIP ! \n\n<b>Forex et Indices inclus</b>\n<b>(-60% DE REDUCTION) 💡</b>\n\n✅ Signaux de qualité \n✅ Rapport hebdomadaire \n✅ Mise à jour des signaux (Exemple : <a href='https://prnt.sc/1xmfvuo'>Mise à jour</a>)\n✅ Indices inclus (US30, NASDAQ entre autres) \n✅ Stratégies (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a>)\n✅ Actualité du marché pour éviter les risques de perte (Exemple : <a href='https://prnt.sc/1xmfbqh'>Risque</a>) \n✅ Gestion financière (Guide Excel) \n✅ Chat d’Assistance @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicateurs inclus \n\n<b>Exemple</b> de Signal : \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Sélectionnez votre plan ci-dessous, Devenez un membre Elite 👇🔰 \n\n✖️ Annulez votre abonnement à tout moment ✖️ \nPour annuler ou vérifier le statut de votre abonnement, il suffit d’envoyer /status au bot. \n\nVeuillez sélectionner votre plan d'abonnement :"
    user = update.callback_query.from_user
    usa=user.first_name
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    user = update.callback_query.from_user
    usa=user.first_name
    context.bot.send_message(chat_id=update.effective_user.id,text="Hey {}!".format(usa),reply_markup=reply_marku)
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,parse_mode=telegram.ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
  elif a=="p1" or a=="p2" or a=="p3" or a=="p4" or a=="p5":
    if a=="p1":
        x=19.99
        y="1 week"
    elif a=="p2":
        x=34.99
        y="1 MONTH"
    elif a=="p3":
        x=74.99
        y="3 MONTHS"
    elif a=="p4":
        x=109.99
        y="6 MONTHS"
    else:
        x=149.99
        y="LIFETIME"
    keyboard = [[InlineKeyboardButton("Paypal", callback_data='p-{}'.format(x))],[InlineKeyboardButton("Credit/Debit Card", callback_data='c-{}'.format(x))],[InlineKeyboardButton("Crypto", callback_data='b-{}'.format(x))]]  
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    text= "Your benefits:\n✅ Nation Forex Signals VIP (✅)\n\nPrice: {} €\nBilling period: {}\nBilling mode: recurring".format(x,y)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup)
  
  elif a=="p-19.99" or a=="p-34.99" or a=="p-74.99" or a=="p-109.99" or a=="p-149.99":  
    if a=="p-19.99":
        pkg=1
        bs="P-3MA17355GS4821530LTWXCNQ"
    elif a=="p-34.99":
        pkg=2
        bs="P-3GV94404VX052992JLTXSORQ"
    elif a=="p-74.99":
        pkg=3
        bs="P-0AD21827NA8127730LTX7I6I"
    elif a=="p-109.99":
        pkg=4
        bs="P-16M45158DE9586719LTYOSKY"

    if a=="p-149.99":
        cv=ilife()
        cv=cv.split("***")
        id=cv[0]
        print(id)
        link=cv[1]
        print(link)
        conn = sqlite3.connect('paypal.db')
        conn.execute("INSERT INTO COMPANY (ID,ptoken,pkg) \
            VALUES ('{}','{}','{}')".format(update.effective_user.id,id,"5"))
        conn.commit()
    else:
      ad=cagree(bs)
      link=ad
      ass=ad.split("&token=")
      ass=ass[1].split("]")
      ass=ass[0].strip()
      conn = sqlite3.connect('paypal.db')
      conn.execute("INSERT INTO COMPANY (ID,ptoken ,pkg) \
            VALUES ('{}','{}','{}')".format(update.effective_user.id,ass,pkg))
      conn.commit()
      print(ass)
      print(ad)
    
    
    keyboard = [[InlineKeyboardButton("Make a Payment", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    c=context.bot.send_message(chat_id=update.effective_user.id,text="Please click the button below:" 
                    ,reply_markup=reply_markup)
    context.job_queue.run_once(callback_minut, 200, context=c)
  elif a=="c-19.99" or a=="c-34.99" or a=="c-74.99" or a=="c-109.99" or a=="c-149.99":  
    if a=="c-19.99":
        pkg=1
        pr=20
        cc="🔑 1 WEEK VIP ACCESS🔑"
    elif a=="c-34.99":
        pkg=2
        pr=35
        cc="🔑 1 MONTH VIP ACCESS🔑"
    elif a=="c-74.99":
        pkg=3
        pr =75
        cc="🔑 3 MONTH VIP ACCESS🔑"
    elif a=="c-109.99":
        cc="🔑 6 MONTH VIP ACCESS🔑"
        pkg=4
        pr =110
    else:
        cc="🔑 Lifetime VIP ACCESS🔑"
        pkg=5
        pr=150
    title = "Nation Forex Signals"
    description = cc
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    provider_token = "350862534:LIVE:YjE5YWIxZDY5Y2Zk"
    currency = "EUR"
    price = pr
    prices = [LabeledPrice("Nation Forex Signals", price * 100)]
    c=context.bot.send_invoice(
       update.effective_user.id,  title, description, payload, provider_token, currency, prices
    )
    context.job_queue.run_once(callback_minut, 200, context=c)
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set pkg ='{}' where ID = '{}'".format(pkg,int(update.effective_user.id)))
    conn.commit()
    conn.close()
  elif a=="b-19.99" or a=="b-34.99" or a=="b-74.99" or a=="b-109.99" or a=="b-149.99":  
    if a=="b-19.99":
        pkg=1
        pr=20
    elif a=="b-34.99":
        pkg=2
        pr=34.99
    elif a=="b-74.99":
        pkg=3
        pr =75
    elif a=="b-109.99":
        pkg=4
        pr =110
    else:
        pkg=5
        pr=150
    charge = client.charge.create(name='Nation Forex Signals',
                          description="Nation Forex Signals",
                          pricing_type='fixed_price',
                          local_price={ 
                             "amount": pr,
                             "currency": "EUR"
                      })
    linka=charge["hosted_url"]
    coda=charge["id"]
    conn = sqlite3.connect("wallet.db")  
    conn.execute("INSERT INTO COMPANY (ID,code,pkg) \
            VALUES ('{}', '{}','{}')".format(str(update.effective_user.id),coda,pkg)) 
    conn.commit()
    keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    c=context.bot.send_message(chat_id=update.effective_user.id,text="Please click on below button to make payment",reply_markup=reply_markup)
    context.job_queue.run_once(callback_minut, 200, context=c)
def gender(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0]
    c=update.message.text
    if c=="VIP ROOM - PREMIUM SIGNALS  🔑" or c=="SALAS VIP - SEGNALES PREMIUM 🔑"or c=="SALA VIP - SEGNALI PREMIUM  🔑"or c=="VIP-RAUM - PREMIUM-SIGNALE 🔑"or c=="SALLE VIP - SEGNALIS PREMIUM 🔑":
        if a=="1":
            keyboard = [[InlineKeyboardButton("🔑 1 WEEK ACCESS VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONTHS ACCESS VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONTHS ACCESS VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
            text='<b>Welcome to NationForexSignals 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n<b>Forex & Indices Included</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Quality signals \n✅ Weekly report\n✅ Signals update (Example: <a href="https://prnt.sc/1xmfvuo">Update</a>)\n✅ Indices included (US30, NASDAQ and more)\n✅ Strategies (<a href="https://prnt.sc/1xmfjy0">Scalping</a>, <a href="https://prnt.sc/1xmfqd0">Intraday</a>, <a href="https://prnt.sc/1xmfrm4">MultiDay</a>, <a href="https://prnt.sc/1xmft9s">Cycle</a> )\n✅ Market news to avoid risk of loss (Example: <a href="https://prnt.sc/1xmfbqh">Risk</a>)\n✅ Money management (Guide Excel)\n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicators included \n\n<b>Example Signal:</b>\nXAUUSD SELL\nENTRY: 1789.40\nSL:  1799.00\nTP:  1765.00\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply type /status to the bot.\n\nPlease select your subscription plan:'
       
        elif a=="2":
            keyboard = [[InlineKeyboardButton("🔑 1 SEMANA DE ACCESO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MES DE ACCESO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESES DE ACCESO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESES DE ACCESO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESO VIP🔥€149.99", callback_data='p5')]]  
            text="<b>Bienvenido a NationForexSignals 👋</b>\n\n¡Compre su <u>plan</u> en solo <b>60 segundos!</b>\n\nDespués de realizar la compra, el bot le dará el enlace para acceder a la sala VIP.\n\n<b>Forex e índices incluidos</b>\n<b>(60% de descuento) 💡</b>\n\n✅ Señales de calidad \n✅ Informe semanal\n✅ Actualización de señales (Ejemplo: Actualización (<a href='https://prnt.sc/1xmfvuo'>Actualización</a>)\n✅ Índices incluidos (US30, NASDAQ y más)\n✅ Estrategias  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intradiario</a>, <a href='https://prnt.sc/1xmfrm4'>Varios días</a>, <a href='https://prnt.sc/1xmft9s'>Ciclo</a>)\n✅ Noticias del mercado para evitar el riesgo de pérdida (Ejemplo: <a href='https://prnt.sc/1xmfbqh'>Riesgo</a>)\n✅ Administración del dinero (Guía Excel)\n✅ Chat de soporte @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicadores incluidos \n\n<b>Ejemplo</b> de señal:\nXAUUSD SELL\nENTRY: 1789.40\nSL: 1799.00\nTP: 1765.00\n\n🔰👇 Seleccione su plan a continuación, conviértase en miembro Elite👇🔰\n\n✖️Cancele la suscripción en cualquier momento✖️\nPara cancelar o verificar el estado de la suscripción, simplemente escriba /status en el bot.\n\nSeleccione su plan de suscripción:"
        elif a=="3":
            keyboard = [[InlineKeyboardButton("🔑 1 SETTIMANA ACCESSO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MESE ACCESSO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESI ACCESSO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESI ACCESSO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESSO VIP🔥€149.99", callback_data='p5')]]  
            text="<b>Benvenuto su NationForexSignals 👋</b>\n\nCompra il tuo <u>piano</u> in <b>60 secondi!</b>\n\nDopo aver effettuato l'acquisto il bot ti darà il link per accedere alla sala VIP!\n\n<b>Forex & Indici inclusi!</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualità dei segnali \n✅ Report settimanale \n✅ Aggiornamenti Segnali (Esempio: <a href='https://prnt.sc/1xmfvuo'>Update</a>) \n✅ Indici Inclusi (US30, NASDAQ. e altro) \n✅ Strategie  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a> )\n✅ Notizie di mercato, per evitare rischi sul conto (Esempio: <a href='https://prnt.sc/1xmfbqh'>Risk</a>) \n✅ Guida al Money Management (Guide Excel) \n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicatori inclusi \n\n<b>Esempio</b> Segnale: \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Seleziona il tuo piano qui sotto, Diventa un Membro Elite👇🔰 \n\n✖️Cancella l'abbonamento in qualsiasi momento✖️ \nPer cancellare o controllare lo stato dell'abbonamento, basta digitare /status al bot. \n\nSeleziona il tuo piano di abbonamento:"
        elif a=="4":
            keyboard = [[InlineKeyboardButton("🔑 1 WOCHE ZUGANG VIP 🔑 €19,99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONAT ZUGANG VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONATE ZUGANG VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONATE ZUGANG VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
            text="<b>Willkommen bei Nation Forex Signals 👋</b>\n\nKaufen Sie Ihren <u>plan</u> in nur <b>60 Sekunden!</b>\n\nNachdem Sie den Kauf getätigt haben, gibt Ihnen der Bot den <b>Link zum VIP-Raum!</b>\n\n<b>Forex & Indizes enthalten</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualitätssignale \n✅ Wöchentlicher Bericht \n✅ Signalaktualisierung (Beispiel: <a href='https://prnt.sc/1xmfvuo'>Update</a>)\n✅ Einschliesslich Indizes (US30, NASDAQ und mehr) \n✅ Strategien (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Zyklus</a>) \n✅ Marktnachrichten zur Vermeidung von Verlustrisiken (Beispiel: <a href='https://prnt.sc/1xmfbqh'>Risiko</a>) \n✅ Geldverwaltung (Excel-Leitfaden) \n✅ Support-Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Inbegriffene Indikatoren \n\n<b>Beispiel signal:</b> \nXAUUSD SELL \nENTRY: 1789.40 \nSL: 1799,00 \nTP: 1765,00 \n\n🔰👇Wählen Sie Ihren Plan unten, Werden Sie ein Elite-Mitglied 👇🔰 \n\n✖️Abonnement jederzeit kündigen✖️ \nUm den Abonnementstatus zu kündigen oder den Abonnementstatus zu überprüfen, tippen Sie einfach /status in den Bot ein. \n\nBitte wählen Sie Ihr Abonnement:"
        else:
            keyboard = [[InlineKeyboardButton("🔑 1 SEMAINE D'ACCÈS VIP 🔑 19,99€", callback_data='p1')],[InlineKeyboardButton("🔑 1 MOIS D'ACCÈS VIP 🔑 34,99€", callback_data='p2')],[InlineKeyboardButton("🔑 3 MOIS D'ACCÈS VIP 🔑 74,99€", callback_data='p3')],[InlineKeyboardButton("🔑 6 MOIS D'ACCÈS VIP 🔑 109,99€", callback_data='p4')],[InlineKeyboardButton("🔥 ACCÈS À LIFETIME  🔥149,99€", callback_data='p5')]]  
            text="<b>Bienvenue sur Nation Forex Signals 👋</b>\n\nAchetez votre abonnement en <b>60 secondes seulement !</b>\n\nAprès avoir effectué l'achat, le robot vous donnera le lien pour accéder à la salle VIP ! \n\n<b>Forex et Indices inclus</b>\n<b>(-60% DE REDUCTION) 💡</b>\n\n✅ Signaux de qualité \n✅ Rapport hebdomadaire \n✅ Mise à jour des signaux (Exemple : <a href='https://prnt.sc/1xmfvuo'>Mise à jour</a>)\n✅ Indices inclus (US30, NASDAQ entre autres) \n✅ Stratégies (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a>)\n✅ Actualité du marché pour éviter les risques de perte (Exemple : <a href='https://prnt.sc/1xmfbqh'>Risque</a>) \n✅ Gestion financière (Guide Excel) \n✅ Chat d’Assistance @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicateurs inclus \n\n<b>Exemple</b> de Signal : \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Sélectionnez votre plan ci-dessous, Devenez un membre Elite 👇🔰 \n\n✖️ Annulez votre abonnement à tout moment ✖️ \nPour annuler ou vérifier le statut de votre abonnement, il suffit d’envoyer /status au bot. \n\nVeuillez sélectionner votre plan d'abonnement :"
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
    elif c=="COPYTRADING  🗝" or c=="COPYTRADING 🗝":
        if a=="1":
            text='Welcome to the <b>COPYTRADING</b> sections of <b>Nation Forex Signals!</b>\n\nAfter many requests, we decided to reintroduce our <b>Copytrading</b> service which will be available for every member of our community and will guarantee <u>PASSIVE</u> income for each investor.\n\n<b>Which are the main advantages of our CopyTrading service?</b>\n- Monthly passive income\n- Automated trades\n- Managed by 24/7 team\n- 100% Free Service\n\nWhy would we do this for free?\nWe get <b>10%</b> of your profits and... only if we make you money! So it will be our interest to give you the best trades possible.\n\nIf you are intrested in our <b>CopyTrading</b> service click the botton down below to text our Support service so we can help you start making money.\n\n<a href="https://t.me/FxClare">I AM INTERESTED IN COPYTRADING</a>'
            keyboard = [[InlineKeyboardButton("I AM INTERESTED IN COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
        elif a=="2":
            text='Bienvenido a las secciones de <b>COPYTRADING</b> de <b>Nation Forex Signals! 🔥</b>\n\nDespués de muchas solicitudes, decidimos reintroducir nuestro servicio de Copytrading, que estará disponible para todos los miembros de nuestra comunidad y garantizará ingresos <u>PASIVOS</u> para cada inversor. \n\n<b>¿Cuáles son las principales ventajas de nuestro servicio de Copytrading?</b>\n- Ingresos pasivos mensuales \n- Operaciones automatizadas \n- Gestionado por el equipo 24/7 \n- Servicio 100% gratuito \n\n¿Por qué haríamos esto gratis? \nObtenemos el <b>10%</b> de sus ganancias y... ¡sólo si hacemos dinero! Por lo tanto, será nuestro interés brindarle las mejores operaciones posibles. \n\nSi está interesado en nuestro servicio de <b>Copytrading</b>, haga clic en el botón de abajo para enviar un mensaje de texto a nuestro servicio de soporte para que podamos ayudarlo a comenzar a ganar dinero. \n\n<a href="https://oddw.com/">ESTOY INTERESADO EN EL COPYTRADING</a>'
            keyboard = [[InlineKeyboardButton("ESTOY INTERESADO EN EL COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
        elif a=="3":
            text='Benvenuto nella sezione <b>COPYTRADING</b> di <b>Nation Forex Signals! 🔥</b>\n\nDopo moltissime richieste abbiamo riaperto il servizio di <b>CopyTrading</b>, che sarà disponibile per qualsiasi utente! \n\nIn questo modo potete usufruire della nostra strategia automatica dove permetterà di copiare i nostri segnali senza farlo manualmente! \ngarantendo un entrata costante totalmente <u>PASSIVA</u>. \n\n<b>I vantaggi del CopyTrading quali sono?</b>\n- Entrata <u>Passiva</u> Mensile \n- Non dovrai aprire operazioni manualmente \n- Gestito dal Team 24/7 \n- Ottenendo il <b>COPYTRADING</b> non dovrai pagare nessuna iscrizione \n\n<b>I vantaggi del CopyTrading quali sono?</b>\n\nOtteniamo il <b>10%</b> dei vostri profitti! \nGuadagniamo solamente se vi facciamo guadagnare! \n\nSe sei interessato al servizio di <b>CopyTrading</b> clicca il bottone per scrivere al nostro supporto cosi da gestire al meglio la tua richiesta di iscrizione! \n\n<a href="https://t.me/FxClare">SONO INTERESSATO AL COPYTRADING</a>'
            keyboard = [[InlineKeyboardButton("SONO INTERESSATO AL COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
        elif a=="4":
            text='Willkommen zu den <b>COPYTRADING</b>-Abschnitten der <b>Nation Forex Signals! 🔥</b>\n\nNach vielen Anfragen haben wir uns entschieden, unseren <b>Copytrading</b>-Service wieder einzuführen, der jedem Mitglied unserer Community zur Verfügung steht und jedem Investor ein <u>PASSIVES</u> Einkommen garantiert. \n\n<b>Was sind die Hauptvorteile unseres Copytrading Service?</b>\n- Monatliches passives Einkommen \n- Automatisierter Handel \n- Verwaltet von einem 24/7-Team \n- 100% kostenloser Service \n\nWarum sollten wir das umsonst tun? \nWir bekommen <b>10%</b> Ihres Gewinns und... nur, wenn wir Ihnen Geld einbringen! Es wird also unser Interesse sein, Ihnen die bestmöglichen Trades zu bieten. \n\nWenn Sie Interesse an unserem <b>Copytrading</b>-Service haben, klicken Sie auf die Schaltfläche unten, um unseren Support-Service zu simsen, damit wir Ihnen helfen können, Geld zu verdienen. \n\n<a href="https://t.me/FxClare">ICH BIN AN COPYTRADING INTERESSIERT</a>'
            keyboard = [[InlineKeyboardButton("ICH BIN AN COPYTRADING INTERESSIERT", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
        elif a=="5":
            text='Bienvenue dans la section <b>COPYTRADING</b> de <b>Nation Forex Signals! 🔥</b>\n\nAprès de nombreuses demandes, nous avons décidé de réintroduire notre service Copytrading, qui sera disponible pour chaque membre de notre communauté, et garantira un revenu passif à chaque investisseur. \n\n<b>Quels sont les principaux avantages de notre service Copytrading ?</b>\n- Revenu passif mensuel \n- Trading automatisé \n- Géré par l équipe 24/7 \n- Service 100% gratuit \n\nPourquoi faisons-nous cela gratuitement ? \nNous recevons <b>10%</b> de vos bénéfices et... seulement si nous vous faisons gagner de l argent ! Il est donc dans notre intérêt de vous faire réaliser les meilleurs trades possibles. \n\nSi vous êtes intéressé par notre service <b>Copytrading</b>, cliquez sur le bouton ci-dessous pour envoyer un message à notre service d assistance, nous pourrons ainsi vous aider à gagner de l argent. \n\n<a href="https://t.me/FxClare">JE SUIS INTÉRESSÉ PAR LE COPYTRADING</a>'
            keyboard = [[InlineKeyboardButton("JE SUIS INTÉRESSÉ PAR LE COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
    elif c=="SUPPORT 🛎  🔑" or c=="SOPORTE 🛎"or c=="SUPPORTO 🛎"or c=="UNTERSTÜTZUNG 🛎"or c=="SUPPORTS 🛎":
        if a=="2":
            keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
            text='Este bot no ofrece soporte: \n\nSi necesita ayuda de un miembro del personal, haga clic en el botón de abajo:\n» <a href="https://t.me/FxClare">SPANISH SUPPORT</a>«\n\nComandos que pueden ser útiles: \n\n/plans - consulta nuestro plan para acceder a la sala VIP - Señales Premium \n/copytrading - servicio de copytrading, copia nuestras señales con nuestro sistema automatizado \n/support - si desea ser ayudado por un miembro del personal \n/status - para ver sus planes actuales / darse de baja'
        elif a=="1":
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
            text='This bot does not offer support:\n\nIf you need help from a staff members click the botton down below:\n» <a href="https://t.me/FxClare">ENGLISH SUPPORT</a>«\n\nCommands that may be useful:\n\n/plans - check our plan to access the Vip Room - Premium Signals\n/copytrading - copytrading service, copy our signals with our automated system\n/support - if you want to be helped by a staff member \n/status - to see your current plans / unsubscribe'
        elif a=="3":
            keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
            text='Questo bot non offre assistenza. \n\nPer ottenere aiuto da un nostro staff clicca qui in basso\n» <a href="https://t.me/FxClare">SUPPORTO ITALIANO</a>«\n\nComandi che possono essere utili: \n\n/plans  - ottieni i piani di acquisto della sala vip - segnali premium \n/copytrading - servizio di copytrading, copia i segnali in modo passivo \n/support - contatto diretto con un membro dello staff \n/status - puoi vedere i tuoi abbonamenti attivi o cancellarli'
        elif a=="4":
            keyboard = [[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
            text='Dieser Bot bietet keine Unterstützung: \n\nWenn Sie Hilfe von einem Mitarbeiter benötigen, klicken Sie auf die Schaltfläche unten:\n» <a href="https://t.me/FxClare">DEUTSCHE UNTERSTÜTZUNG</a>«\n\nCommands, die nützlich sein können: \n\n/plans – überprüfen Sie unseren Plan für den Zugang zum Vip Room – Premium Signals \n/copytrading – Copytrading Service, kopieren Sie unsere Signale mit unserem automatisierten System \n/support – wenn Sie von einem Mitarbeiter unterstützt werden möchten \n/status – um Ihre aktuellen Pläne zu sehen / abbestellen'
        elif a=="5":
            keyboard = [[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
            text='Ce bot ne propose pas d assistance : \n\nSi vous avez besoin de l aide d un membre du personnel, cliquez sur le bouton ci-dessous :\n» <a href="https://t.me/FxClare">FRENCH SUPPORT</a>«\n\nCommandes qui peuvent être utiles : \n\n/plans - consultez notre plan pour accéder à la Salle Vip - Signaux Premium \n/copytrading - service Copytrading, suivez nos signaux avec notre système automatisé. \n/support - si vous souhaitez être assisté par un membre du staff \n/status - pour consulter vos abonnements actuels / vous désinscrire'
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
    elif c=="Change Language":
        keyboard = [[InlineKeyboardButton("English 🇬🇧", callback_data='1'),InlineKeyboardButton("Español 🇪🇸", callback_data='2')],[InlineKeyboardButton("Italiano 🇮🇹", callback_data='3'),InlineKeyboardButton("Deutsche 🇩🇪", callback_data='4')],[InlineKeyboardButton("Français 🇫🇷", callback_data='5')]]  
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please Select Your Language",reply_markup=reply_markup)
    elif c=="SUBCRIPTION STATUS 📌" or c=="STATUS ABONADO 📌"or c=="STATO ABBONAMENTO 📌"or c=="ABONNEMENT STATUS 📌"or c=="STATUT ABONNEMENT 📌":
        connection = sqlite3.connect("kick.db")  
        cursor = connection.execute("SELECT date FROM COMPANY where id='{}'".format(update.effective_user.id))
        for names in cursor:
            da=names[0]
        if da=="0":
            conn = sqlite3.connect('agreement.db')
            cursor = conn.cursor()
            cursor.execute("SELECT agree_id,pkg FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
            jobs = cursor.fetchall()
            print(jobs)
            if len(jobs) !=0:
                for nm in jobs:
                    if nm[1]=="4":
                        da="LIFETIME ACCESS"
                    else:
                        billing_agreement = BillingAgreement.find(nm[0])
                        exp=billing_agreement['agreement_details']['next_billing_date']
                        da=parser.parse(exp)
        if da !="0":
            if a=="1":
                keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
                text='Your subscription will expire the:\n\n<b>{}</b>\n\nTo unsubscribe, type /cancel\n\nIf you choose this option, you will be removed from the Vip Room after your plan is expired!'.format(da)
            elif a=="2":
                keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
                text='Estimado usuario/a:\n\nSu suscripción expirará el:\n\n<b>{}</b>\n\nPara cancelar la suscripción, escriba /cancel\n\nSi elige esta opción, se le eliminará de la sala Vip una vez que su plan haya caducado.'.format(da)
            elif a=="3":
                keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
                text='Caro utente,\n\n Il tuo abbonamento scadrà il giorno:\n\n<b>{}</b>\n\nPer annullare il tuo abbonamento utilizza /cancel\n\nSe deciderai di annullare l abbonamento verrai rimosso dalla Sala Vip dopo la scadenza del tuo piano! nachdem Ihr Tarif abgelaufen ist!'.format(da)
            elif a=="4":
                keyboard = [[InlineKeyboardButton("⬅️ Zurück", callback_data='5')]]   
                text='Sehr geehrter Nutzer,\n\nIhr Abonnement läuft ab am:\n\n<b>{}</b>\n\nUm sich abzumelden, geben Sie /cancel ein\n\nWenn Sie diese Option wählen, werden Sie aus dem VIP-Raum entfernt, nachdem Ihr Tarif abgelaufen ist!'.format(da)
            elif a=="5":
                keyboard = [[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
                text='Cher utilisateur,\n\nVotre abonnement expirera le :\n\n<b>{}</b>\n\nPour vous désabonner, tapez /cancel\n\nSi vous faites ce choix, vous serez exclu de la salle Vip après l expiration de votre abonnement !'.format(da)
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
        else:
            if a=="1":
                keyboard = [[InlineKeyboardButton("ACTIVATE YOUR PLAN", callback_data='1')],[InlineKeyboardButton("ENGLISH SUPPORT", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
                text='Dear user, you do not have any active subscriptions at this time.\n\nTo activate your VIP ROOM subscription, select the "ACTIVATE YOUR PLAN" button 🔑\n\n\nIf you need SUPPORT in english language select the button "ENGLISH SUPPORT" 🇬🇧\n\n» <a href="https://t.me/FxClare">ENGLISH SUPPORT</a>«'
            elif a=="2":
                keyboard = [[InlineKeyboardButton("ACTIVA TU PLAN 🔑", callback_data='2')],[InlineKeyboardButton("SOPORTE EN ESPAÑOL", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
                text='Estimado usuario, no tiene ninguna suscripción activa en este momento. \n\nPara activar tu suscripción a la SALA VIP selecciona el botón "ACTIVA TU PLAN" 🔑\n\nSi necesitas SOPORTE en el idioma español selecciona el botón  "SOPORTE EN ESPAÑOL" 🇪🇸\n\n» <a href="https://t.me/FxClare">SOPORTE EN ESPAÑOL</a>«'
            elif a=="3":
                keyboard = [[InlineKeyboardButton("ATTIVA IL TUO PIANO 🔑", callback_data='3')],[InlineKeyboardButton("SUPPORTO ITALIANO 🇮🇹", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
                text='Caro utente, non hai abbonamenti attivi in questo momento.\n\nPer attivare l abbonamento alla SALA VIP seleziona il bottone "ATTIVA IL TUO PIANO" 🔑\n\nSe hai bisogno di SUPPORTO nella lingua italiana seleziona il bottone "SUPPORTO ITALIANO" 🇮🇹\n\n» <a href="https://t.me/FxClare">SUPPORTO ITALIANO 🇮🇹</a>«'
            elif a=="4":
                keyboard = [[InlineKeyboardButton("AKTIVIEREN SIE IHREN PLAN 🔑", callback_data='4')],[InlineKeyboardButton("DEUTSCHE UNTERSTÜTZUNG 🇩🇪", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
                text='Sehr geehrter Benutzer, Sie haben zur Zeit keine aktiven Abonnements.\n\n Um Ihr VIP-RAUM-Abonnement zu aktivieren, wählen Sie die Schaltfläche "AKTIVIEREN SIE IHREN PLAN" 🔑\n\nWenn Sie SUPPORT in Deutsche Sprache benötigen, wählen Sie die Schaltfläche "DEUTSCHE UNTERSTÜTZUNG" 🇩🇪\n\n» <a href="https://t.me/FxClare">DEUTSCHE UNTERSTÜTZUNG 🇩🇪</a>«'
            elif a=="5":
                keyboard = [[InlineKeyboardButton("ACTIVEZ VOTRE PLAN 🔑", callback_data='5')],[InlineKeyboardButton("ASSISTANCE EN FRANÇAIS 🇫🇷", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
                text='Cher utilisateur, vous n avez pas d abonnements actifs pour le moment.\n\n Pour activer votre abonnement au SALON VIP, veuillez sélectionner le bouton "ACTIVER VOTRE PLAN" 🔑. \n\nSi vous avez besoin de SUPPORT en langue français, veuillez sélectionner le bouton "ASSISTANCE EN FRANÇAIS 🇫🇷"\n\n» <a href="https://t.me/FxClare">ASSISTANCE EN FRANÇAIS 🇫🇷</a>«'
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
def copytrading(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0]
    if a=="1":
        text='Welcome to the <b>COPYTRADING</b> sections of <b>Nation Forex Signals!</b>\n\nAfter many requests, we decided to reintroduce our <b>Copytrading</b> service which will be available for every member of our community and will guarantee <u>PASSIVE</u> income for each investor.\n\n<b>Which are the main advantages of our CopyTrading service?</b>\n- Monthly passive income\n- Automated trades\n- Managed by 24/7 team\n- 100% Free Service\n\nWhy would we do this for free?\nWe get <b>10%</b> of your profits and... only if we make you money! So it will be our interest to give you the best trades possible.\n\nIf you are intrested in our <b>CopyTrading</b> service click the botton down below to text our Support service so we can help you start making money.\n\n<a href="https://t.me/FxClare">I AM INTERESTED IN COPYTRADING</a>'
        keyboard = [[InlineKeyboardButton("I AM INTERESTED IN COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
    elif a=="2":
        text='Bienvenido a las secciones de <b>COPYTRADING</b> de <b>Nation Forex Signals! 🔥</b>\n\nDespués de muchas solicitudes, decidimos reintroducir nuestro servicio de Copytrading, que estará disponible para todos los miembros de nuestra comunidad y garantizará ingresos <u>PASIVOS</u> para cada inversor. \n\n<b>¿Cuáles son las principales ventajas de nuestro servicio de Copytrading?</b>\n- Ingresos pasivos mensuales \n- Operaciones automatizadas \n- Gestionado por el equipo 24/7 \n- Servicio 100% gratuito \n\n¿Por qué haríamos esto gratis? \nObtenemos el <b>10%</b> de sus ganancias y... ¡sólo si hacemos dinero! Por lo tanto, será nuestro interés brindarle las mejores operaciones posibles. \n\nSi está interesado en nuestro servicio de <b>Copytrading</b>, haga clic en el botón de abajo para enviar un mensaje de texto a nuestro servicio de soporte para que podamos ayudarlo a comenzar a ganar dinero. \n\n<a href="https://oddw.com/">ESTOY INTERESADO EN EL COPYTRADING</a>'
        keyboard = [[InlineKeyboardButton("ESTOY INTERESADO EN EL COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
    elif a=="3":
        text='Benvenuto nella sezione <b>COPYTRADING</b> di <b>Nation Forex Signals! 🔥</b>\n\nDopo moltissime richieste abbiamo riaperto il servizio di <b>CopyTrading</b>, che sarà disponibile per qualsiasi utente! \n\nIn questo modo potete usufruire della nostra strategia automatica dove permetterà di copiare i nostri segnali senza farlo manualmente! \ngarantendo un entrata costante totalmente <u>PASSIVA</u>. \n\n<b>I vantaggi del CopyTrading quali sono?</b>\n- Entrata <u>Passiva</u> Mensile \n- Non dovrai aprire operazioni manualmente \n- Gestito dal Team 24/7 \n- Ottenendo il <b>COPYTRADING</b> non dovrai pagare nessuna iscrizione \n\n<b>I vantaggi del CopyTrading quali sono?</b>\n\nOtteniamo il <b>10%</b> dei vostri profitti! \nGuadagniamo solamente se vi facciamo guadagnare! \n\nSe sei interessato al servizio di <b>CopyTrading</b> clicca il bottone per scrivere al nostro supporto cosi da gestire al meglio la tua richiesta di iscrizione! \n\n<a href="https://t.me/FxClare">SONO INTERESSATO AL COPYTRADING</a>'
        keyboard = [[InlineKeyboardButton("SONO INTERESSATO AL COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
    elif a=="4":
        text='Willkommen zu den <b>COPYTRADING</b>-Abschnitten der <b>Nation Forex Signals! 🔥</b>\n\nNach vielen Anfragen haben wir uns entschieden, unseren <b>Copytrading</b>-Service wieder einzuführen, der jedem Mitglied unserer Community zur Verfügung steht und jedem Investor ein <u>PASSIVES</u> Einkommen garantiert. \n\n<b>Was sind die Hauptvorteile unseres Copytrading Service?</b>\n- Monatliches passives Einkommen \n- Automatisierter Handel \n- Verwaltet von einem 24/7-Team \n- 100% kostenloser Service \n\nWarum sollten wir das umsonst tun? \nWir bekommen <b>10%</b> Ihres Gewinns und... nur, wenn wir Ihnen Geld einbringen! Es wird also unser Interesse sein, Ihnen die bestmöglichen Trades zu bieten. \n\nWenn Sie Interesse an unserem <b>Copytrading</b>-Service haben, klicken Sie auf die Schaltfläche unten, um unseren Support-Service zu simsen, damit wir Ihnen helfen können, Geld zu verdienen. \n\n<a href="https://t.me/FxClare">ICH BIN AN COPYTRADING INTERESSIERT</a>'
        keyboard = [[InlineKeyboardButton("ICH BIN AN COPYTRADING INTERESSIERT", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
    elif a=="5":
        text='Bienvenue dans la section <b>COPYTRADING</b> de <b>Nation Forex Signals! 🔥</b>\n\nAprès de nombreuses demandes, nous avons décidé de réintroduire notre service Copytrading, qui sera disponible pour chaque membre de notre communauté, et garantira un revenu passif à chaque investisseur. \n\n<b>Quels sont les principaux avantages de notre service Copytrading ?</b>\n- Revenu passif mensuel \n- Trading automatisé \n- Géré par l équipe 24/7 \n- Service 100% gratuit \n\nPourquoi faisons-nous cela gratuitement ? \nNous recevons <b>10%</b> de vos bénéfices et... seulement si nous vous faisons gagner de l argent ! Il est donc dans notre intérêt de vous faire réaliser les meilleurs trades possibles. \n\nSi vous êtes intéressé par notre service <b>Copytrading</b>, cliquez sur le bouton ci-dessous pour envoyer un message à notre service d assistance, nous pourrons ainsi vous aider à gagner de l argent. \n\n<a href="https://t.me/FxClare">JE SUIS INTÉRESSÉ PAR LE COPYTRADING</a>'
        keyboard = [[InlineKeyboardButton("JE SUIS INTÉRESSÉ PAR LE COPYTRADING", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
def plans(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0]
    if a=="1":
        keyboard = [[InlineKeyboardButton("🔑 1 WEEK ACCESS VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONTH ACCESS VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONTHS ACCESS VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONTHS ACCESS VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
        text='<b>Welcome to NationForexSignals 👋</b>\n\n<b>Buy</b> your <u>plan</u> in just <b>60 seconds!</b>\n\nAfter you make the purchase the bot will give you the <b>link to access the VIP room!</b>\n\n<b>Forex & Indices Included</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Quality signals \n✅ Weekly report\n✅ Signals update (Example: <a href="https://prnt.sc/1xmfvuo">Update</a>)\n✅ Indices included (US30, NASDAQ and more)\n✅ Strategies (<a href="https://prnt.sc/1xmfjy0">Scalping</a>, <a href="https://prnt.sc/1xmfqd0">Intraday</a>, <a href="https://prnt.sc/1xmfrm4">MultiDay</a>, <a href="https://prnt.sc/1xmft9s">Cycle</a> )\n✅ Market news to avoid risk of loss (Example: <a href="https://prnt.sc/1xmfbqh">Risk</a>)\n✅ Money management (Guide Excel)\n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicators included \n\n<b>Example Signal:</b>\nXAUUSD SELL\nENTRY: 1789.40\nSL:  1799.00\nTP:  1765.00\n\n🔰👇 Select your Plan below, Become an Elite Member👇🔰\n\n✖️Cancel subscription anytime✖️\nTo cancel or to check subscription status, simply type /status to the bot.\n\nPlease select your subscription plan:'
    
    elif a=="2":
        keyboard = [[InlineKeyboardButton("🔑 1 SEMANA DE ACCESO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MES DE ACCESO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESES DE ACCESO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESES DE ACCESO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESO VIP🔥€149.99", callback_data='p5')]]  
        text="<b>Bienvenido a NationForexSignals 👋</b>\n\n¡Compre su <u>plan</u> en solo <b>\60 segundos!</b>\\n\nDespués de realizar la compra, el bot le dará el enlace para acceder a la sala VIP.\n\n<b>Forex e índices incluidos</b>\n<b>(60% de descuento) 💡</b>\n\n✅ Señales de calidad \n✅ Informe semanal\n✅ Actualización de señales (Ejemplo: Actualización (<a href='https://prnt.sc/1xmfvuo'>Actualización</a>)\n✅ Índices incluidos (US30, NASDAQ y más)\n✅ Estrategias  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intradiario</a>, <a href='https://prnt.sc/1xmfrm4'>Varios días</a>, <a href='https://prnt.sc/1xmft9s'>Ciclo</a>)\n✅ Noticias del mercado para evitar el riesgo de pérdida (Ejemplo: <a href='https://prnt.sc/1xmfbqh'>Riesgo</a>)\n✅ Administración del dinero (Guía Excel)\n✅ Chat de soporte @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪\n✅ Indicadores incluidos \n\n<b>Ejemplo</b> de señal:\nXAUUSD SELL\nENTRY: 1789.40\nSL: 1799.00\nTP: 1765.00\n\n🔰👇 Seleccione su plan a continuación, conviértase en miembro Elite👇🔰\n\n✖️Cancele la suscripción en cualquier momento✖️\nPara cancelar o verificar el estado de la suscripción, simplemente escriba /status en el bot.\n\nSeleccione su plan de suscripción:"
    elif a=="3":
        keyboard = [[InlineKeyboardButton("🔑 1 SETTIMANA ACCESSO VIP 🔑  €19.99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MESE ACCESSO VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MESI ACCESSO VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MESI ACCESSO VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥 LIFETIME ACCESSO VIP🔥€149.99", callback_data='p5')]]  
        text="<b>Benvenuto su NationForexSignals 👋</b>\n\nCompra il tuo <u>piano</u> in <b>60 secondi!</b>\n\nDopo aver effettuato l'acquisto il bot ti darà il link per accedere alla sala VIP!\n\n<b>Forex & Indici inclusi!</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualità dei segnali \n✅ Report settimanale \n✅ Aggiornamenti Segnali (Esempio: <a href='https://prnt.sc/1xmfvuo'>Update</a>) \n✅ Indici Inclusi (US30, NASDAQ. e altro) \n✅ Strategie  (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a> )\n✅ Notizie di mercato, per evitare rischi sul conto (Esempio: <a href='https://prnt.sc/1xmfbqh'>Risk</a>) \n✅ Guida al Money Management (Guide Excel) \n✅ Support Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicatori inclusi \n\n<b>Esempio</b> Segnale: \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Seleziona il tuo piano qui sotto, Diventa un Membro Elite👇🔰 \n\n✖️Cancella l'abbonamento in qualsiasi momento✖️ \nPer cancellare o controllare lo stato dell'abbonamento, basta digitare /status al bot. \n\nSeleziona il tuo piano di abbonamento:"
    elif a=="4":
        keyboard = [[InlineKeyboardButton("🔑 1 WOCHE ZUGANG VIP 🔑 €19,99", callback_data='p1')],[InlineKeyboardButton("🔑 1 MONAT ZUGANG VIP🔑 €34.99", callback_data='p2')],[InlineKeyboardButton("🔑 3 MONATE ZUGANG VIP🔑 €74.99", callback_data='p3')],[InlineKeyboardButton("🔑 6 MONATE ZUGANG VIP🔑 €109.99", callback_data='p4')],[InlineKeyboardButton("🔥LIFETIME ACCESS VIP🔥€149.99", callback_data='p5')]]  
        text="<b>Willkommen bei Nation Forex Signals 👋</b>\n\nKaufen Sie Ihren <u>plan</u> in nur <b>60 Sekunden!</b>\n\nNachdem Sie den Kauf getätigt haben, gibt Ihnen der Bot den <b>Link zum VIP-Raum!</b>\n\n<b>Forex & Indizes enthalten</b>\n<b>(-60% OFF) 💡</b>\n\n✅ Qualitätssignale \n✅ Wöchentlicher Bericht \n✅ Signalaktualisierung (Beispiel: <a href='https://prnt.sc/1xmfvuo'>Update</a>)\n✅ Einschliesslich Indizes (US30, NASDAQ und mehr) \n✅ Strategien (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Zyklus</a>) \n✅ Marktnachrichten zur Vermeidung von Verlustrisiken (Beispiel: <a href='https://prnt.sc/1xmfbqh'>Risiko</a>) \n✅ Geldverwaltung (Excel-Leitfaden) \n✅ Support-Chat @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Inbegriffene Indikatoren \n\n<b>Beispiel signal:</b> \nXAUUSD SELL \nENTRY: 1789.40 \nSL: 1799,00 \nTP: 1765,00 \n\n🔰👇Wählen Sie Ihren Plan unten, Werden Sie ein Elite-Mitglied 👇🔰 \n\n✖️Abonnement jederzeit kündigen✖️ \nUm den Abonnementstatus zu kündigen oder den Abonnementstatus zu überprüfen, tippen Sie einfach /status in den Bot ein. \n\nBitte wählen Sie Ihr Abonnement:"
    else:
        keyboard = [[InlineKeyboardButton("🔑 1 SEMAINE D'ACCÈS VIP 🔑 19,99€", callback_data='p1')],[InlineKeyboardButton("🔑 1 MOIS D'ACCÈS VIP 🔑 34,99€", callback_data='p2')],[InlineKeyboardButton("🔑 3 MOIS D'ACCÈS VIP 🔑 74,99€", callback_data='p3')],[InlineKeyboardButton("🔑 6 MOIS D'ACCÈS VIP 🔑 109,99€", callback_data='p4')],[InlineKeyboardButton("🔥 ACCÈS À LIFETIME  🔥149,99€", callback_data='p5')]]  
        text="<b>Bienvenue sur Nation Forex Signals 👋</b>\n\nAchetez votre abonnement en <b>60 secondes seulement !</b>\n\nAprès avoir effectué l'achat, le robot vous donnera le lien pour accéder à la salle VIP ! \n\n<b>Forex et Indices inclus</b>\n<b>(-60% DE REDUCTION) 💡</b>\n\n✅ Signaux de qualité \n✅ Rapport hebdomadaire \n✅ Mise à jour des signaux (Exemple : <a href='https://prnt.sc/1xmfvuo'>Mise à jour</a>)\n✅ Indices inclus (US30, NASDAQ entre autres) \n✅ Stratégies (<a href='https://prnt.sc/1xmfjy0'>Scalping</a>, <a href='https://prnt.sc/1xmfqd0'>Intraday</a>, <a href='https://prnt.sc/1xmfrm4'>MultiDay</a>, <a href='https://prnt.sc/1xmft9s'>Cycle</a>)\n✅ Actualité du marché pour éviter les risques de perte (Exemple : <a href='https://prnt.sc/1xmfbqh'>Risque</a>) \n✅ Gestion financière (Guide Excel) \n✅ Chat d’Assistance @FxClare 24/7 🇬🇧🇮🇹🇫🇷🇪🇸🇩🇪 \n✅ Indicateurs inclus \n\n<b>Exemple</b> de Signal : \nXAUUSD SELL \nENTRY: 1789.40 \nSL:  1799.00 \nTP:  1765.00 \n\n🔰👇 Sélectionnez votre plan ci-dessous, Devenez un membre Elite 👇🔰 \n\n✖️ Annulez votre abonnement à tout moment ✖️ \nPour annuler ou vérifier le statut de votre abonnement, il suffit d’envoyer /status au bot. \n\nVeuillez sélectionner votre plan d'abonnement :"
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,reply_markup=reply_markup,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
def er(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0]
    if a=="2":
        text='El comando que escribió es <b>incorrecto</b>, si necesita ayuda, ¡este comando podría ayudarlo a resolver su problema! \n\n/plans - consulta nuestro plan para acceder a la sala VIP - Señales Premium \n/copytrading - servicio de copytrading, copia nuestras señales con nuestro sistema automatizado \n/support - si desea ser ayudado por un miembro del personal \n/status - para ver sus planes actuales / darse de baja'
    elif a=="1":
        text='The command you typed <b>is wrong</b>, if you need help, this commands could help you solve your problem! \n\n/plans - check our plan to access the Vip Room - Premium Signals \n/copytrading - copytrading service, copy our signals with our automated system \n/support - if you want to be helped by a staff member \n/status - to see your current plans / unsubscribe' 
    elif a=="3":    
        text='Il comando che hai digitato <b>è errato</b>, se hai bisogno di un aiuto questi comandi possono aiutarti a trovare il tuo problema! \n\n/plans  - ottieni i piani di acquisto della sala vip - segnali premium \n/copytrading - servizio di copytrading, copia i segnali in modo passivo \n/support - contatto diretto con un membro dello staff \n/status - puoi vedere i tuoi abbonamenti attivi o cancellarli'
    elif a=="4":
        text='Der von Ihnen eingegebene Befehl <b>ist falsch</b>. \n\n/plans – überprüfen Sie unseren Plan für den Zugang zum Vip Room – Premium Signals \n/copytrading – Copytrading Service, kopieren Sie unsere Signale mit unserem automatisierten System \n/support – wenn Sie von einem Mitarbeiter unterstützt werden möchten \n/status – um Ihre aktuellen Pläne zu sehen / abbestellen'
    elif a=="5":
        text='La commande que vous avez tapée <b>est incorrecte</b>, si vous avez besoin d assistance, ces commandes pourraient vous aider à résoudre votre problème ! \n\n/plans - consultez notre plan pour accéder à la Salle Vip - Signaux Premium \n/copytrading - service Copytrading, suivez nos signaux avec notre système automatisé. \n/support - si vous souhaitez être assisté par un membre du staff \n/status - pour consulter vos abonnements actuels / vous désinscrire'
    context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
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
      pkg=names[0]
    if pkg=="1":
        b = date.today() + timedelta(days=7)
        bb=date.today()
        cc="🔑 1 WEEK VIP ACCESS🔑"
        ff="19,99 € 1 week"
    elif pkg=="2":
        b = date.today() + timedelta(days=30)
        bb=date.today()
        cc="🔑 1 MONTH VIP ACCESS🔑"
        ff="34,99 € 1 month"

    elif pkg=="3":
        b = date.today() + timedelta(days=90)
        bb=date.today()
        cc="🔑 3 MONTH VIP ACCESS🔑"
        ff="74,99 € 3 month"
    elif pkg=="4":
        b = date.today() + timedelta(days=180)
        bb=date.today()
        cc="🔑 6 MONTH VIP ACCESS🔑"
        ff="109,99 € 6 month"

    elif pkg=="5":
        b = "Lifetime"
        bb=date.today()
        cc="🔑 Lifetime VIP ACCESS🔑"
        ff="149,99 € Lifetime"
    text2="Congratulations! You have a new Stripe subscription\n\nUser: {}\nProject: NationForexSignals\nPlan: {}\nBilling: {}\n Received: {}\nStatus: active\nNext payment on: {}\n".format(update.effective_user.id,cc,ff,bb,b)
    print(b)
    conn = sqlite3.connect("kick.db")  
    conn.execute("UPDATE COMPANY set date='{}' where ID = '{}'".format(b,int(update.effective_user.id)))
    conn.commit()
    conn.close()
    exp=dt.datetime.now().utcnow() + dt.timedelta(days=7)
    c=context.bot.createChatInviteLink(chat_id= -1001403638093, expire_date=exp,member_limit=1)
    link=c['invite_link']
    keyboard = [[InlineKeyboardButton("Nation Forex Signals VIP", url=link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_user.id,text="Thank you for your payment\n.Please click the button below to join Channel" 
            ,reply_markup=reply_markup)
    context.bot.send_message(chat_id=1991527010,text=text2)
def support(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0] 
    if a=="2":
            keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
            text='Este bot no ofrece soporte: \n\nSi necesita ayuda de un miembro del personal, haga clic en el botón de abajo:\n» <a href="https://t.me/FxClare">SPANISH SUPPORT</a>«\n\nComandos que pueden ser útiles: \n\n/plans - consulta nuestro plan para acceder a la sala VIP - Señales Premium \n/copytrading - servicio de copytrading, copia nuestras señales con nuestro sistema automatizado \n/support - si desea ser ayudado por un miembro del personal \n/status - para ver sus planes actuales / darse de baja'
    elif a=="1":
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
        text='This bot does not offer support:\n\nIf you need help from a staff members click the botton down below:\n» <a href="https://t.me/FxClare">ENGLISH SUPPORT</a>«\n\nCommands that may be useful:\n\n/plans - check our plan to access the Vip Room - Premium Signals\n/copytrading - copytrading service, copy our signals with our automated system\n/support - if you want to be helped by a staff member \n/status - to see your current plans / unsubscribe'
    elif a=="3":
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
        text='Questo bot non offre assistenza. \n\nPer ottenere aiuto da un nostro staff clicca qui in basso\n» <a href="https://t.me/FxClare">SUPPORTO ITALIANO</a>«\n\nComandi che possono essere utili: \n\n/plans  - ottieni i piani di acquisto della sala vip - segnali premium \n/copytrading - servizio di copytrading, copia i segnali in modo passivo \n/support - contatto diretto con un membro dello staff \n/status - puoi vedere i tuoi abbonamenti attivi o cancellarli'
    elif a=="4":
        keyboard = [[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
        text='Dieser Bot bietet keine Unterstützung: \n\nWenn Sie Hilfe von einem Mitarbeiter benötigen, klicken Sie auf die Schaltfläche unten:\n» <a href="https://t.me/FxClare">DEUTSCHE UNTERSTÜTZUNG</a>«\n\nCommands, die nützlich sein können: \n\n/plans – überprüfen Sie unseren Plan für den Zugang zum Vip Room – Premium Signals \n/copytrading – Copytrading Service, kopieren Sie unsere Signale mit unserem automatisierten System \n/support – wenn Sie von einem Mitarbeiter unterstützt werden möchten \n/status – um Ihre aktuellen Pläne zu sehen / abbestellen'
    elif a=="5":
        keyboard = [[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
        text='Ce bot ne propose pas d assistance : \n\nSi vous avez besoin de l aide d un membre du personnel, cliquez sur le bouton ci-dessous :\n» <a href="https://t.me/FxClare">FRENCH SUPPORT</a>«\n\nCommandes qui peuvent être utiles : \n\n/plans - consultez notre plan pour accéder à la Salle Vip - Signaux Premium \n/copytrading - service Copytrading, suivez nos signaux avec notre système automatisé. \n/support - si vous souhaitez être assisté par un membre du staff \n/status - pour consulter vos abonnements actuels / vous désinscrire'
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
def status(update, context):
    connection = sqlite3.connect("lang.db")  
    cursor = connection.execute("SELECT lang FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        a=names[0] 
    connection = sqlite3.connect("kick.db")  
    cursor = connection.execute("SELECT date FROM COMPANY where id='{}'".format(update.effective_user.id))
    for names in cursor:
        da=names[0]
    if da !="0":
        if a=="1":
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
            text='Your subscription will expire the:\n\n{}\n\nTo unsubscribe, type /cancel\n\nIf you choose this option, you will be removed from the Vip Room after your plan is expired!'.format(da)
        elif a=="2":
            keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
            text='Estimado usuario/a:\n\nSu suscripción expirará el:\n\n{}\n\nPara cancelar la suscripción, escriba /cancel\n\nSi elige esta opción, se le eliminará de la sala Vip una vez que su plan haya caducado.'.format(da)
        elif a=="3":
            keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
            text='Caro utente,\n\n Il tuo abbonamento scadrà il giorno:\n\n{}\n\nPer annullare il tuo abbonamento utilizza /cancel\n\nSe deciderai di annullare l abbonamento verrai rimosso dalla Sala Vip dopo la scadenza del tuo piano! nachdem Ihr Tarif abgelaufen ist!'.format(da)
        elif a=="4":
            keyboard = [[InlineKeyboardButton("⬅️ Zurück", callback_data='5')]]   
            text='Sehr geehrter Nutzer,\n\nIhr Abonnement läuft ab am:\n\n{}\n\nUm sich abzumelden, geben Sie /cancel ein\n\nWenn Sie diese Option wählen, werden Sie aus dem VIP-Raum entfernt, nachdem Ihr Tarif abgelaufen ist!'.format(da)
        elif a=="5":
            keyboard = [[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
            text='Cher utilisateur,\n\nVotre abonnement expirera le :\n\n{}\n\nPour vous désabonner, tapez /cancel\n\nSi vous faites ce choix, vous serez exclu de la salle Vip après l expiration de votre abonnement !'.format(da)
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
    else:
        if a=="1":
            keyboard = [[InlineKeyboardButton("ACTIVATE YOUR PLAN", callback_data='1')],[InlineKeyboardButton("ENGLISH SUPPORT", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Back", callback_data='1')]]
            text='Dear user, you do not have any active subscriptions at this time.\n\nTo activate your VIP ROOM subscription, select the "ACTIVATE YOUR PLAN" button 🔑\n\n\nIf you need SUPPORT in english language select the button "ENGLISH SUPPORT" 🇬🇧\n\n» <a href="https://t.me/FxClare">ENGLISH SUPPORT</a>«'
        elif a=="2":
            keyboard = [[InlineKeyboardButton("ACTIVA TU PLAN 🔑", callback_data='2')],[InlineKeyboardButton("SOPORTE EN ESPAÑOL", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Volver", callback_data='2')]]
            text='Estimado usuario, no tiene ninguna suscripción activa en este momento. \n\nPara activar tu suscripción a la SALA VIP selecciona el botón "ACTIVA TU PLAN" 🔑\n\nSi necesitas SOPORTE en el idioma español selecciona el botón  "SOPORTE EN ESPAÑOL" 🇪🇸\n\n» <a href="https://t.me/FxClare">SOPORTE EN ESPAÑOL</a>«'
        elif a=="3":
            keyboard = [[InlineKeyboardButton("ATTIVA IL TUO PIANO 🔑", callback_data='3')],[InlineKeyboardButton("SUPPORTO ITALIANO 🇮🇹", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Indietro", callback_data='3')]]
            text='Caro utente, non hai abbonamenti attivi in questo momento.\n\nPer attivare l abbonamento alla SALA VIP seleziona il bottone "ATTIVA IL TUO PIANO" 🔑\n\nSe hai bisogno di SUPPORTO nella lingua italiana seleziona il bottone "SUPPORTO ITALIANO" 🇮🇹\n\n» <a href="https://t.me/FxClare">SUPPORTO ITALIANO 🇮🇹</a>«'
        elif a=="4":
            keyboard = [[InlineKeyboardButton("AKTIVIEREN SIE IHREN PLAN 🔑", callback_data='4')],[InlineKeyboardButton("DEUTSCHE UNTERSTÜTZUNG 🇩🇪", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Zurück", callback_data='4')]]
            text='Sehr geehrter Benutzer, Sie haben zur Zeit keine aktiven Abonnements.\n\n Um Ihr VIP-RAUM-Abonnement zu aktivieren, wählen Sie die Schaltfläche "AKTIVIEREN SIE IHREN PLAN" 🔑\n\nWenn Sie SUPPORT in Deutsche Sprache benötigen, wählen Sie die Schaltfläche "DEUTSCHE UNTERSTÜTZUNG" 🇩🇪\n\n» <a href="https://t.me/FxClare">DEUTSCHE UNTERSTÜTZUNG 🇩🇪</a>«'
        elif a=="5":
            keyboard = [[InlineKeyboardButton("ACTIVEZ VOTRE PLAN 🔑", callback_data='5')],[InlineKeyboardButton("ASSISTANCE EN FRANÇAIS 🇫🇷", url='https://t.me/FxClare')],[InlineKeyboardButton("⬅️ Retour", callback_data='5')]]
            text='Cher utilisateur, vous n avez pas d abonnements actifs pour le moment.\n\n Pour activer votre abonnement au SALON VIP, veuillez sélectionner le bouton "ACTIVER VOTRE PLAN" 🔑. \n\nSi vous avez besoin de SUPPORT en langue français, veuillez sélectionner le bouton "ASSISTANCE EN FRANÇAIS 🇫🇷"\n\n» <a href="https://t.me/FxClare">ASSISTANCE EN FRANÇAIS 🇫🇷</a>«'
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
def callback_minut(context):
    job = context.job
    updat=job.context
    aa=updat['message_id']
    ab=updat['chat']['id']
    context.bot.delete_message(chat_id=ab,
                  message_id=aa)
def callback_minute(context: telegram.ext.CallbackContext):
    connection = sqlite3.connect("kick.db")  
    cursor = connection.execute("SELECT ID,date FROM COMPANY ")
    connection.close()
    for names in cursor:
        da=names[0]
        dy=names[1]
        try:
            x=datetime.today().strftime('%Y-%m-%d')
            a=str(dy) #date
            y=a.split(" ")
            y=y[0]
            if x>y:
                conn = sqlite3.connect("kick.db")  
                conn.execute("DELETE COMPANY  where ID = '{}'".format(int(da)))
                conn.commit()
                conn.close()
                print(da)
                vb=datetime.datetime.now().utcnow() + datetime.timedelta(minutes =2)
                try:
                    context.bot.kick_chat_member(chat_id=-1001403638093,user_id=int(da),until_date=vb)
                except:
                    pass
                context.bot.send_message(chat_id=str(da),text="you are removed from group. Click on below button to renew the service")            
            elif x==y:
              context.bot.send_message(chat_id=str(da),text="today is last date of your subsription. Update it otherwise you will be removed tomorrow\n\nClick on below button to renew the service")
        except:
          pass  
def broadcast(update, context):
    bn=str(update.effective_user.id)
    if bn=="1991527010":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send your message to broadcast")
        return GEND
def gend(update, context):
    print(update)
    if update.message.photo:
        conn = sqlite3.connect('kick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM COMPANY") 
        jobs = cursor.fetchall()
        for names in jobs:
            ida=names[0]
            try:
                context.bot.send_photo(chat_id=ida,photo=update.message.photo[-1].file_id,caption=update.message.caption)
            except:
                pass
    else:
        conn = sqlite3.connect('kick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM COMPANY") 
        jobs = cursor.fetchall()
        for names in jobs:
            ida=names[0]
            try:
                context.bot.send_message(chat_id=ida,text=update.message.text)
            except:
                pass
    context.bot.send_message(chat_id=update.effective_user.id,text="Message send sucessfully.")
    return ConversationHandler.END
def main():
  updater = Updater("1994434514:AAFJVFzT4K3ifga1gHMA7gZ2ZUvM5eQqwiI", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CallbackQueryHandler(button))
  dp.job_queue.run_repeating(callback_minute, 86400)
  dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
  dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
  dp.add_handler(CommandHandler('plans', plans))
  dp.add_handler(CommandHandler('copytrading', copytrading))
  dp.add_handler(CommandHandler('support', support))
  dp.add_handler(CommandHandler('status', status))
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(MessageHandler(Filters.regex('^(VIP ROOM - PREMIUM SIGNALS  🔑|COPYTRADING  🗝|COPYTRADING 🗝|SUPPORT 🛎  🔑|SOPORTE 🛎|SUPPORTO 🛎|UNTERSTÜTZUNG 🛎|SUPPORTS 🛎|SUBCRIPTION STATUS 📌|STATUS ABONADO 📌|STATO ABBONAMENTO 📌|ABONNEMENT STATUS 📌|STATUT ABONNEMENT 📌|Change Language|SALAS VIP - SEGNALES PREMIUM 🔑|SALA VIP - SEGNALI PREMIUM  🔑|VIP-RAUM - PREMIUM-SIGNALE 🔑|SALLE VIP - SEGNALIS PREMIUM 🔑)$'), gender))
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler('broadcast', broadcast)],
        states={

            GEND: [MessageHandler(Filters.text|Filters.photo, gend)],
  
        },
        fallbacks=[CommandHandler('broadcast', broadcast)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler)
  dp.add_handler(MessageHandler(Filters.all,er))
  updater.start_polling()
  updater.idle()
    
    
if __name__ == '__main__':
    main()