from typing import List
import json
import re
from numpy import place
from telegram import LabeledPrice, ShippingOption,ParseMode
from telegram.ext import (
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
from datetime import  timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
AB,BUTTON,BB,AA,CON,CA,PKG,SAB= range(8)
MARKETS = ['3way_result', '3way_result_1st_half', 'both_teams_to_score',
           'over_under_1_5', 'over_under_2_5', 'over_under_3_5',
           'team_to_score_first']


def escape_markdown(text: str, version: int = 2, entity_type: str = None) -> str:
    """
    Helper function to escape telegram markup symbols.
    Args:
        text (:obj:`str`): The text.
        version (:obj:`int` | :obj:`str`): Use to specify the version of telegrams Markdown.
            Either ``1`` or ``2``. Defaults to ``1``.
        entity_type (:obj:`str`, optional): For the entity types ``PRE``, ``CODE`` and the link
            part of ``TEXT_LINKS``, only certain characters need to be escaped in ``MarkdownV2``.
            See the official API documentation for details. Only valid in combination with
            ``version=2``, will be ignored else.
    """
    if int(version) == 1:
        escape_chars = r'_*`['
    elif int(version) == 2:
        if entity_type in ['pre', 'code']:
            escape_chars = r'\`'
        elif entity_type == 'text_link':
            escape_chars = r'\)'
        else:
            escape_chars = r'_*[]()~`>#+-=|{}.!'
    else:
        raise ValueError('Markdown version must be either 1 or 2!')

    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

class OctosportAPI:

    def __init__(self, path_to_data=''):
        self._data_json = None
        self.path_to_data = path_to_data

    @property
    def json_data(self):
        '''return the json data'''

        if self._data_json is None:
            with open(os.path.join(self.path_to_data, 'octosport_bot_data.json'), 'r') as f:
                self._data_json = json.load(f)

        return self._data_json

    def get_continents(self) -> List[str]:
        '''get all continents'''
        return list(self.json_data.keys())

    def get_continent_contries(self, continent: str) -> List[str]:
        '''get all countries for a continent'''
        return list(self.json_data[continent].keys())

    def get_country_leagues(self, continent: str, country: str) -> List[str]:
        '''get all leagues for a country'''
        return list(self.json_data[continent][country].keys())

    def get_markets(self) -> List[str]:
        '''get all markets'''
        return MARKETS

    def get_league_market_prediction(self, continent: str, country: str, league: str, market: str) -> List:
        '''Get the league predictability index and accuracy for a continent, country, league, market tuple.'''
        return list(self.json_data[continent][country][league][market]['prediction'])

    def get_league_market_predictability(self, continent: str, country: str, league: str, market: str) -> dict:
        '''Get the league predictability index and accuracy for a continent, country, league, market tuple.'''
        return (self.json_data[continent][country][league][market]['predictability'])

    def send_markdown_message(self, continent: str, country: str, league: str, market: str):

        league_performance = self.get_league_market_predictability(continent,country,league,market)
        probabilities = self.get_league_market_prediction(continent,country,league,market)
        print_dict = lambda a_dict:'   '.join([f'{k}: '+str(v)+'%' for k,v in a_dict.items()])
        LPI_link = escape_markdown('https://medium.com/geekculture/how-to-measure-football-prediction-model-quality-cac480a1e2f7',version=2)
        line1 = '*'+escape_markdown('/'.join([continent,country, league])+'\n')+'*'
        line2 = f'_{escape_markdown(market)} probabilities_ '+'\n'
        line3 = f'<a href="https://medium.com/geekculture/how-to-measure-football-prediction-model-quality-cac480a1e2f7">LPI</a>: {escape_markdown(league_performance["accuracy"])} \- {league_performance["lpi"]}'+'\n'
        line4 = '\n'

        line5 = '\n\n'.join([escape_markdown(f'{x["home_name"]} - {x["away_name"]} | {x["match_date"]} \n {"  "+print_dict(x["probabilities"])}') for x in probabilities])

        message = ''.join([line1,line2,line3,line4,line5])

        return message


def start(update, context):
  print(update.effective_user.id)
  connection = sqlite3.connect("selection.db")  
  cursor = connection.cursor()  
  cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
        conn = sqlite3.connect('selection.db')
        conn.execute("INSERT INTO COMPANY (ID,continent,Country,pkg ) \
            VALUES ('{}', '{}','{}','{}')".format(update.effective_user.id,"0","0","0"))
        conn.commit()
        conn.close()
  user = update.message.from_user
  usa=user.first_name
  key=[["Info"],["My Countries"],["Continents"],["Buy Subscription"]]
  reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text=
        'Hello, welcome in Octosport football prediction bot\. '
        'Here you can quickly access to all our machine learning predictions for 1x2, btts, over/under, ftts amoung others\. You'
        ' can access all league within a country by substring\. See our /subscription plans\. This help us to maintain the bot alive\.'
        '\n\n'
        '*What we are:*'
        '\n'
        'We provide the best ⚽ prediction, measured by the [log\-loss](https://medium.com/p/cac480a1e2f7), that AI can learn from data\. You can find more informations on our [medium blog](https://medium.com/@octosport)\.'
         '\n\n'
         '*What we are not:*\n'
        'We are not a tipster or a bet recommendation system\. You can use the prediction as you want\.'
        '\n\n'
        '*Bot commands*'
        '\n'
        '/continents command to start diving in our data\. '
        '\n'
        '/mycountries to see your current subscriptions\.'
        '\n'
        '/free shows a free random set of countries available every day\.'
        '\n'
        '/infos you will find informations about the data we display\. '
        '\n'
        '/mytimezone command to set your timezone and display hours in your time\.'
         '\n'
        '/contact to leave a feedback\.'
        '\n\n'
        'You can also send /terms for our Terms and Condition\.'
        '', parse_mode=ParseMode.MARKDOWN_V2,disable_web_page_preview=True,reply_markup=reply_marku)
 

def menu(update, context):
    c=update.message.text
    if c=="Info":
        key=[["Info"],["My Countries"],["Continents"],["Buy Subscription"]]
        reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="This bot will give you pridictions",reply_markup=reply_marku)
    elif c=="Continents":
        con=octo_api.get_continents()
        key=[]
        for cn in con:
            v=[cn]
            key.append(v)
        key.append(["Main Menu"])
        reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the Continent:",reply_markup=reply_marku)
        return SAB
    elif c=="My Countries":
        connection = sqlite3.connect("countries.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT Country,continent FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            key=[["Info"],["My Countries"],["Continents"],["Buy Subscription"]]
            reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="You have not subscribe to any Country.")
        else:
            key=[]
            for cn in jobs:
                v=[cn[0]]
                key.append(v)
            key.append(["Main Menu"])
            global cen
            cen="t"
            reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select the Country:",reply_markup=reply_marku)
            return AB
    elif c=="Buy Subscription":
        con=octo_api.get_continents()
        key=[]
        for cn in con:
            v=[cn]
            key.append(v)
        key.append(["Main Menu"])
        reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the Continent:",reply_markup=reply_marku)
        return CON
    else:
        key=[["Info"],["My Countries"],["Continents"],["Buy Subscription"]]
        reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please Choose Your option",reply_markup=reply_marku)


def con(update, context):
    global cen
    c=update.message.text
    cen=c
    print(cen)
    if c=="Free":
        con=octo_api.get_continent_contries('Free')
        key=[]
        for cn in con:
            v=[cn]
            key.append(v)
        key.append(["Main Menu"])
        reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the Country:",reply_markup=reply_marku)
        return AB
    else:
        connection = sqlite3.connect("countries.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT Country FROM COMPANY where id= '{}' and continent='{}'".format(update.effective_user.id,c)) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            key=[["Info"],["My Countries"],["Continents"],["Buy Subscription"]]
            reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="You have not subscribe to any Country for this Continent.")
        else:
            key=[]
            for cn in jobs:
                v=[cn[0]]
                key.append(v)
            key.append(["Main Menu"])
            reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select the Country:",reply_markup=reply_marku)
            return AB
def button(update, context):
  chat_id = update.effective_user.id
  query = update.callback_query
  a=query.data
  if a== '1': 
    conn = sqlite3.connect("selection.db")  
    conn.execute("UPDATE COMPANY set  pkg ='1' where ID = '{}'".format(int(update.effective_user.id)))
    conn.commit()
    conn.close()
    chat_id =update.effective_user.id
    title = "Test payment"
    description = "Test payment using python-telegram-bot"
    payload = "Custom-Payload"
    provider_token = "284685063:TEST:ZjYyYzQxOWY3NWFl"
    currency = "EUR"
    price = 2
    prices = [LabeledPrice("Test", price * 100)]
    context.bot.send_invoice(
        chat_id, title, description, payload, provider_token, currency, prices
    )
  else:
        conn = sqlite3.connect("selection.db")  
        conn.execute("UPDATE COMPANY set  pkg ='2' where ID = '{}'".format(int(update.effective_user.id)))
        conn.commit()
        conn.close()
        chat_id =update.effective_user.id
        title = "Test payment"
        description = "Test payment using python-telegram-bot"
        payload = "Custom-Payload"
        provider_token = "284685063:TEST:ZjYyYzQxOWY3NWFl"
        currency = "EUR"
        price = 1.5
        prices = [LabeledPrice("Test", price * 100)]
        context.bot.send_invoice(
            chat_id, title, description, payload, provider_token, currency, prices
        )

def cone(update, context): 
    c=update.message.text
    conn = sqlite3.connect("selection.db")  
    conn.execute("UPDATE COMPANY set  continent ='{}' where ID = '{}'".format(c,int(update.effective_user.id)))
    conn.commit()
    conn.close()
    global pc
    pc=c
    con=octo_api.get_continent_contries(c)
    key=[]
    for cn in con:
        v=[cn]
        key.append(v)
    key.append(["Main Menu"])
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the Country:",reply_markup=reply_marku)
    return CA
def ca(update, context): 
    c=update.message.text
    conn = sqlite3.connect("selection.db")  
    conn.execute("UPDATE COMPANY set  Country ='{}' where ID = '{}'".format(c,int(update.effective_user.id)))
    conn.commit()
    conn.close()
    global pl
    pl=c
    d=octo_api.get_country_leagues(pc,pl)
    key=[]
    for cn in d:
        v=[cn]
        key.append(v)
    key.append(["Main Menu"])
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the Leagues:",reply_markup=reply_marku)
    return PKG
def pkg(update, context): 
      keyboard = [[InlineKeyboardButton("2.00€ Per Week", callback_data='1')],[InlineKeyboardButton("3.00€ Per Month", callback_data='2')]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="Please choose your payment plan:",reply_markup=reply_markup)
def ab(update, context):
    global ctr
    global cen
    c=update.message.text
    ctr=c
    if cen!="Free":
        connection = sqlite3.connect("countries.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT continent FROM COMPANY where Country='{}'".format(c)) 
        jobs = cursor.fetchall()
        for names in jobs:
            cv=names[0]
            cen=cv
    else:
        cv="Free"
        cen="Free"
    d=octo_api.get_country_leagues(cv, c)
    key=[]
    for cn in d:
        v=[cn]
        key.append(v)
    key.append(["Main Menu"])
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the Leagues:",reply_markup=reply_marku)
    return AA
def aa(update, context):
    global leg
    c=update.message.text
    leg=c
    d=octo_api.get_markets()
    key=[]
    for cn in d:
        v=[cn]
        key.append(v)
    key.append(["Main Menu"])
    reply_marku = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select the market:",reply_markup=reply_marku)
    return BB
def bb(update, context):
    c=update.message.text
    x=octo_api.send_markdown_message(cen,  ctr, leg, c) 
    x=str(x)
    print(x)
    context.bot.send_message(chat_id=update.effective_user.id,text=x,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
    return BB
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        query.answer(ok=True)
def successful_payment_callback(update,context):
    connection = sqlite3.connect("selection.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT Country,continent,pkg FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    for names in jobs:
        cu=names[0]
        cont=names[1]
        pkg=names[2]
    if pkg=="1":
      b = date.today() + timedelta(days=7)
    else:
      b = date.today() + timedelta(days=30)
    conn = sqlite3.connect('countries.db')
    conn.execute("INSERT INTO COMPANY (ID,continent,Country,exp ) \
        VALUES ('{}', '{}','{}','{}')".format(update.effective_user.id,cont,cu,b))
    conn.commit()
    conn.close()  
    context.bot.send_message(chat_id=update.effective_user.id,text="Thank you for your payment!")
def main():
    updater = Updater("5075375826:AAHbD6HO-C5Ud4H2LWCmCGN9FK8OLlLv5AM", use_context=True)
    dp = updater.dispatcher
#    dp.job_queue.run_repeating(callback_minut, 86400)
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
    dp.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Info|Continents|Main Menu|Buy Subscription)$'), menu),MessageHandler(Filters.regex('^(My Countries)$'), menu)],

        states={
            SAB: [MessageHandler(Filters.regex('^(Africa|Americas|Asia|Europe|Oceania|Free)$'), con)],
            AB: [MessageHandler(Filters.text,ab)],
            CON: [MessageHandler(Filters.regex('^(Africa|Americas|Asia|Europe|Oceania|Free)$'),cone)],
            CA: [MessageHandler(Filters.text,ca)],
            PKG: [MessageHandler(Filters.text,pkg)],
            AA: [MessageHandler(Filters.text,aa)],
            BB: [MessageHandler(Filters.text,bb)],
        },
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    octo_api = OctosportAPI()
    main()

   


