import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import requests
import sqlite3
5020757891
BAS,CAS,DAS=range(3)
def start(update,context):
    connection = sqlite3.connect("mystock.db")  
    cursor = connection.cursor() 
    cursor.execute("INSERT INTO wallet (ID,wallet) \
        VALUES ({}, '{}','{}','{}','{}')".format(update.effective_user.id,"0"))
    connection.commit()
    connection.close()
    print(update.effective_user.id)   
    keyboard =[[InlineKeyboardButton("View Stock Prices", callback_data="view"),InlineKeyboardButton("My Stocks", callback_data="my_stocks")],[InlineKeyboardButton("Buy Stocks", callback_data="buy"),InlineKeyboardButton("Sell Stocks", callback_data="sell")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Please Chose one of the following options",reply_markup=reply_markup)

def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    c=update.callback_query.message.message_id
    if a== 'view':
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please send the symbol of stock that you want to check:",reply_markup=reply_markup)
        return BAS
    elif "my_stocks" in a:
        connection = sqlite3.connect("mystock.db")  
        cursor = connection.cursor()  
        hh="MINIMUM BUY $10 MAX BUY $1000 USD\n\n"
        cursor.execute("SELECT Stock,status,price_bought,amount FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
        for names in cursor:
            stock=names[0]
            status=names[1]
            price=float(names[2])
            amount=float(names[3])
            if status=="buy":
                old_am=amount*price
                api_key = 'VO6H8TH5F10IL39U'
                endpoint = 'https://www.alphavantage.co/query'
                symbol = stock
                params = {
                        'function': 'TIME_SERIES_INTRADAY',
                        'symbol': symbol,
                        'interval': '1min',  
                        'apikey': api_key
                    }
                response = requests.get(endpoint, params=params)
                data = response.json()

                latest_data = next(iter(data['Time Series (1min)'].values()))
                latest_price = float(latest_data['1. open'])
                latest_price=round(latest_price,5)
                np=latest_price*amount
                np=round(np,5)
                amount=round(amount,5)
                percentage_change = ((old_am - np) / old_am) * 100
                percentage_change=round(percentage_change,5)
                hh=hh+"Symbol: {}\nQuantity: {}\nAmount: ${}\nBought at: ${}\nProfit: {}%\n\n".format(stock,amount,np,latest_price,percentage_change)
           
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text=hh,reply_markup=reply_markup)
    
    elif a=="main_menu":
      keyboard =[[InlineKeyboardButton("View Stock Prices", callback_data="view"),InlineKeyboardButton("My Stocks", callback_data="my_stocks")],[InlineKeyboardButton("Buy Stocks", callback_data="buy"),InlineKeyboardButton("Sell Stocks", callback_data="sell")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="Please Chose one of the following options",reply_markup=reply_markup)
       
    elif "buy" in a:
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please send the symbol of stock,amount to invest (AAPL,1500) that you want to Buy:",reply_markup=reply_markup)
        return CAS
    elif "confirm" in a:
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Please send your Transcational Hash.",reply_markup=reply_markup)
        return DAS
    elif "main_menu_cancel" in a:
        conn = sqlite3.connect("mystock.db")  
        conn.execute("UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format("Cancel",update.effective_user.id,"pending"))
        conn.commit()
        conn.close()
        keyboard =[[InlineKeyboardButton("View Stock Prices", callback_data="view"),InlineKeyboardButton("My Stocks", callback_data="my_stocks")],[InlineKeyboardButton("Buy Stocks", callback_data="buy"),InlineKeyboardButton("Sell Stocks", callback_data="sell")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="Please Chose one of the following options",reply_markup=reply_markup)
    elif "admin" in a:
        cc=a.split("admin-")
        cc=cc[1]
        conn = sqlite3.connect("mystock.db")  
        conn.execute("UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format("buy",cc,"pending"))
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id=cc,text="your order is confirm now check in view my stock")
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="request updated")
    elif "rejectorder" in a:
        conn = sqlite3.connect("mystock.db")  
        conn.execute("UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format("rejected",update.effective_user.id,"pending"))
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id=cc,text="your order is reject if any fund will be recievd on same address within 3 days")
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="request updated",reply_markup=reply_markup)
    elif a=="sell":
        connection = sqlite3.connect("mystock.db")  
        cursor = connection.cursor()  
        h=[]
        cursor.execute("SELECT Stock,status,price_bought,amount FROM COMPANY where id= {} and status='buy'".format(int(update.effective_user.id)) )
        for names in cursor:
            stock=names[0]
            status=names[1]
            price=float(names[2])
            amount=float(names[3])
            h.append([InlineKeyboardButton(stock, callback_data="stock-{}-{}".format(stock,amount))])  
        h.append([InlineKeyboardButton("Cancel", callback_data="main_menu")])      
        reply_markup = InlineKeyboardMarkup(h,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="Please select the stock that you want to sell:",reply_markup=reply_markup)

    elif "stock" in a:
        cc=a.split("-")
        sy=cc
        cc=cc[1]
        am=float(sy[2])
        api_key = 'VO6H8TH5F10IL39U'
        endpoint = 'https://www.alphavantage.co/query'
        symbol = sy[0].strip()
        am=float(sy[2])
        params = {
                'function': 'TIME_SERIES_INTRADAY',
                'symbol': cc,
                'interval': '1min',  
                'apikey': api_key
            }
        response = requests.get(endpoint, params=params)
        data = response.json()
        latest_data = next(iter(data['Time Series (1min)'].values()))
        latest_price = latest_data['1. open'] 
        latest_price=float(latest_price)
        amount_stock=am*latest_price
        amount_stock=round(amount_stock,4)
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=c,text="stock sell at {} {}$ will send back to your address.".format(latest_price,amount_stock),reply_markup=reply_markup)
        conn = sqlite3.connect("mystock.db")  
        conn.execute("UPDATE COMPANY set status = '{}' where ID = {} and stock='{}'".format("sell",update.effective_user.id,cc))
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id=5020757891,text="User ID: {}\nSymbol: {}\nSell at: {}\nQuantity: {}\nAmount: ${}".format(update.effective_user.id,cc,latest_price,am,amount_stock))



        

    



def cas(update,context):
   msg=update.message.text

   try:
        sy=msg.split(",")
        api_key = 'VO6H8TH5F10IL39U'
        endpoint = 'https://www.alphavantage.co/query'
        symbol = sy[0].strip()
        am=float(sy[1])
        params = {
                'function': 'TIME_SERIES_INTRADAY',
                'symbol': symbol,
                'interval': '1min',  
                'apikey': api_key
            }
        response = requests.get(endpoint, params=params)
        data = response.json()

        latest_data = next(iter(data['Time Series (1min)'].values()))
        latest_price = latest_data['1. open'] 
        latest_price=float(latest_price)
        amount_stock=am/latest_price
        amount_stock=round(amount_stock,4)
        print(amount_stock)
        endpoint = 'https://www.alphavantage.co/query'
        params = {
            'function': 'CURRENCY_EXCHANGE_RATE',
            'from_currency': 'ETH',
            'to_currency': 'USD',
            'apikey': api_key
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        eth= float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        aso=am/eth
        ase=round(aso,4)
        print(ase)
        connection = sqlite3.connect("mystock.db")  
        cursor = connection.cursor() 
        cursor.execute("INSERT INTO COMPANY (ID,stock,status,price_bought,amount) \
            VALUES ({}, '{}','{}','{}','{}')".format(update.effective_user.id,symbol,"pending",latest_price,amount_stock))
        connection.commit()
        connection.close()
        gg="Symbol: {}\nQuantity: {}\n\nPrice: {}\n\n In order to buy the stock please send {} Eth to {} after sending amount you have to click on confirm order otherwise order will be cancel automatically".format(symbol,amount_stock,latest_price,ase,"0x982749hdh08909")
        keyboard =[[InlineKeyboardButton("Confirm Order", callback_data="confirm")],[InlineKeyboardButton("Cancel Order", callback_data="main_menu_cancel")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text=gg,reply_markup=reply_markup)

   
   except:
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="invalid Stock! please send the correct formst and stock(AAPL,1500)",reply_markup=reply_markup)
        return BAS    


def das(update,context):
    msg=update.message.text
    connection = sqlite3.connect("mystock.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT Stock,status,price_bought,amount FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
    for names in cursor:
        stock=names[0]
        status=names[1]
        price=float(names[2])
        amount=float(names[3])

    hh="Symbol: {}\nQuantity: {}\nInvst: ${}\n\nTranscational Hash: {}".format(stock,amount,price,msg)
    keyboard =[[InlineKeyboardButton("Confirm", callback_data="admin-{}".format(update.effective_user.id)),InlineKeyboardButton("Reject", callback_data="rejectorder-{}".format(update.effective_user.id))]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=5020757891,text=hh,reply_markup=reply_markup)
    keyboard =[[InlineKeyboardButton("Main Menu", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Please wait for the confirmation...",reply_markup=reply_markup)


def bas(update,context):
   msg=update.message.text
   print(msg)
   try:
        api_key = 'VO6H8TH5F10IL39U'
        endpoint = 'https://www.alphavantage.co/query'
        symbol = msg
        params = {
                'function': 'TIME_SERIES_INTRADAY',
                'symbol': symbol,
                'interval': '1min',  
                'apikey': api_key
            }
        response = requests.get(endpoint, params=params)
        data = response.json()

        latest_data = next(iter(data['Time Series (1min)'].values()))
        latest_price = latest_data['1. open'] 

        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Current Price of {}: ${}".format(symbol,latest_price),reply_markup=reply_markup)
        return ConversationHandler.END
   
   except:
        keyboard =[[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="invalid Stock! please send the correct stock",reply_markup=reply_markup)
        return BAS
      

def main():
  updater = Updater("6632043637:AAEokmALpk9TFZqRc8YvvWF8aE4qYNaUTeg", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))
  conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button)],

        states={
            
            BAS: [MessageHandler(Filters.text, bas)],
            CAS: [MessageHandler(Filters.text, cas)],
            DAS: [MessageHandler(Filters.text, das)],
         
            
                                               
        },
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler) 
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()