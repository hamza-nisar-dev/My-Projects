import telegram.ext
import telegram.ext
from decimal import Decimal
from datetime import datetime, time
from pytz import timezone
from web3 import Web3
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
import sqlite3


web3 =  Web3(Web3.HTTPProvider("http://localhost:8545"))

BAS, CAS, DAS, EAS, FAS= range(5)


def start(update, context):
    connection = sqlite3.connect("mystock.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT ID FROM wallet where ID= {}".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        connection = sqlite3.connect("mystock.db")  
        cursor = connection.cursor() 
        cursor.execute("INSERT INTO wallet (ID,wallet,quantity) \
            VALUES ({}, '{}','{}')".format(update.effective_user.id,"0","0"))
        connection.commit()
        connection.close()


    print(update.effective_user.id)
    keyboard = [
        [
            InlineKeyboardButton("View Stock Prices", callback_data="view"),
            InlineKeyboardButton("My Stocks", callback_data="my_stocks"),
        ],
        [
            InlineKeyboardButton("Buy Stocks", callback_data="buy"),
            InlineKeyboardButton("Sell Stocks", callback_data="sell"),
        ],

        [
            InlineKeyboardButton("Update Wallet", callback_data="wallet")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Welcome to Stonks! What would you like to do?",
        reply_markup=reply_markup,
    )

def trading_active():
    tz = timezone("US/Eastern") 
    now = datetime.now(tz)
    current_time = now.time()  
    open_time = time(9, 30, 0)
    close_time = time(16, 0, 0)  
    if open_time <= current_time <= close_time:
        return True
    else:
        return False


def button(update, context):
    h = update.effective_user.id
    query = update.callback_query
    a = query.data
    c = update.callback_query.message.message_id
    if a == "view":
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Kindly submit the stock ticker for the stock you wish to view.",
            reply_markup=reply_markup,
        )
        return BAS
    elif "my_stocks" in a:
        connection = sqlite3.connect("mystock.db")
        cursor = connection.cursor()
        hh = "Your stocks are listed below \n\n"
        cursor.execute(
            "SELECT Stock,status,price_bought,amount FROM COMPANY where id= {}".format(
                int(update.effective_user.id)
            )
        )
        for names in cursor:
            stock = names[0]
            status = names[1]
            price = float(names[2])
            amount = float(names[3])
            if status == "buy":
                if trading_active() == False:
                    keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
                    reply_markup = InlineKeyboardMarkup(
                        keyboard, resize_keyboard=True, one_time_keyboard=True
                    )
                    context.bot.send_message(
                        chat_id=update.effective_user.id,
                        text="Trading is closed, opening times are between 9:30am-4pm EST",
                        reply_markup=reply_markup,
                    )
                    return BAS
                                
                old_am = amount * price
                api_key = "VO6H8TH5F10IL39U"
                endpoint = "https://www.alphavantage.co/query"
                symbol = stock
                params = {
                    "function": "TIME_SERIES_INTRADAY",
                    "symbol": symbol,
                    "interval": "1min",
                    "apikey": api_key,
                }
                response = requests.get(endpoint, params=params)
                data = response.json()

                latest_data = next(iter(data["Time Series (1min)"].values()))
                latest_price = float(latest_data["1. open"])
                latest_price = round(latest_price, 5)
                np = latest_price * amount
                np = round(np, 5)
                amount = round(amount, 5)
                percentage_change = ((old_am - np) / old_am) * 100
                percentage_change = round(percentage_change, 5)
                hh = (
                    hh
                    + "Symbol: {}\nQuantity: {}\nAmount: ${}\nBought at: ${}\nProfit: {}%\n\n".format(
                        stock, amount, np, latest_price, percentage_change
                    )
                )

        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text=hh,
            reply_markup=reply_markup,
        )

    elif a == "main_menu":
        keyboard = [
        [
            InlineKeyboardButton("View Stock Prices", callback_data="view"),
            InlineKeyboardButton("My Stocks", callback_data="my_stocks"),
        ],
        [
            InlineKeyboardButton("Buy Stocks", callback_data="buy"),
            InlineKeyboardButton("Sell Stocks", callback_data="sell"),
        ],

        [
            InlineKeyboardButton("Update Wallet", callback_data="wallet")
        ]
        ]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text="Please Chose one of the following options",
            reply_markup=reply_markup,
        )

    elif "buy" in a:
        if trading_active() == False:
            keyboard = [[InlineKeyboardButton("Go back", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(
                keyboard, resize_keyboard=True, one_time_keyboard=True
            )
            context.bot.send_message(
                chat_id=update.effective_user.id,
                text="Trading is closed, opening times are between 9:30am-4pm EST",
                reply_markup=reply_markup,
            )
            return BAS
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Kindly submit the amount in usd that you want to purchase",
            reply_markup=reply_markup,
        )
        return FAS
    elif "confirm" in a:
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Kindly provide your transaction hash and wallet address in the following format (Hash, Wallet Address) for us to verify the txn and be able to send your payment back",
            reply_markup=reply_markup,
        )

        return DAS

    elif "main_menu_cancel" in a:
        conn = sqlite3.connect("mystock.db")
        conn.execute(
            "UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format(
                "Cancel", update.effective_user.id, "pending"
            )
        )
        conn.commit()
        conn.close()
        keyboard = [
        [
            InlineKeyboardButton("View Stock Prices", callback_data="view"),
            InlineKeyboardButton("My Stocks", callback_data="my_stocks"),
        ],
        [
            InlineKeyboardButton("Buy Stocks", callback_data="buy"),
            InlineKeyboardButton("Sell Stocks", callback_data="sell"),
        ],

        [
            InlineKeyboardButton("Update Wallet", callback_data="wallet")
        ]
        ]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text="Please Chose one of the following options",
            reply_markup=reply_markup,
        )

    elif "admin" in a:
        cc = a.split("admin-")
        cc = cc[1]
        conn = sqlite3.connect("mystock.db")
        conn.execute(
            "UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format(
                "buy", cc, "pending"
            )
        )
        conn.commit()
        conn.close()
        context.bot.send_message(
            chat_id=cc, text="We are pleased to confirm your order! You can verify it under 'View My Stock."
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id, message_id=c, text="request updated"
        )
    elif "rejectorder" in a:
        conn = sqlite3.connect("mystock.db")
        conn.execute(
            "UPDATE COMPANY set status = '{}' where ID = {} and status='{}'".format(
                "rejected", update.effective_user.id, "pending"
            )
        )
        conn.commit()
        conn.close()
        context.bot.send_message(
            chat_id=cc,
            text="your order is reject if any fund will be recievd on same address within 3 days",
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text="request updated",
            reply_markup=reply_markup,
        )
    elif a == "sell":
        if trading_active() == False:
            keyboard = [[InlineKeyboardButton("Go back", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(
                keyboard, resize_keyboard=True, one_time_keyboard=True
            )
            context.bot.send_message(
                chat_id=update.effective_user.id,
                text="Trading is closed",
                reply_markup=reply_markup,
            )
            return BAS
        connection = sqlite3.connect("mystock.db")
        cursor = connection.cursor()
        h = []
        cursor.execute(
            "SELECT Stock,status,price_bought,amount FROM COMPANY where id= {} and status='buy'".format(
                int(update.effective_user.id)
            )
        )
        for names in cursor:
            stock = names[0]
            status = names[1]
            price = float(names[2])
            amount = float(names[3])
            h.append(
                [
                    InlineKeyboardButton(
                        stock, callback_data="stock-{}-{}".format(stock, amount)
                    )
                ]
            )
        h.append([InlineKeyboardButton("Cancel", callback_data="main_menu")])
        reply_markup = InlineKeyboardMarkup(
            h, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text="Please select which stock you wish to sell.",
            reply_markup=reply_markup,
        )

    elif "stock" in a:
        cc = a.split("-")
        sy = cc
        cc = cc[1]
        am = float(sy[2])
        api_key = "VO6H8TH5F10IL39U"
        endpoint = "https://www.alphavantage.co/query"
        symbol = sy[0].strip()
        am = float(sy[2])
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": cc,
            "interval": "1min",
            "apikey": api_key,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        latest_data = next(iter(data["Time Series (1min)"].values()))
        latest_price = latest_data["1. open"]
        latest_price = float(latest_price)
        amount_stock = am * latest_price
        amount_stock = round(amount_stock, 4)
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.edit_message_text(
            chat_id=update.effective_user.id,
            message_id=c,
            text="Proceeds from the stock sale will be credited back to your wallet. \nThe Stock price you sold at was: {}  \nYou will be sent: {}$ ".format(
                latest_price, amount_stock
            ),
            reply_markup=reply_markup,
        )
        conn = sqlite3.connect("mystock.db")
        conn.execute(
            "UPDATE COMPANY set status = '{}' where ID = {} and stock='{}'".format(
                "sell", update.effective_user.id, cc
            )
        )
        conn.commit()
        conn.close()
        print(update.effective_user)
        c=update.callback_query.message.from_user
        ms=c.username
        ms=str(ms)
        if "None" in ms:
         ms=c.first_name
        else:
            usss="@{}".format(ms)

        context.bot.send_message(
            chat_id=807516030,
            text="User : @{}\nSymbol: {}\nSell at: {}\nQuantity: {}\nAmount: ${}".format(
                usss, cc, latest_price, am, amount_stock
            ),
        )
    elif a=="wallet":
        connection = sqlite3.connect("mystock.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT wallet FROM wallet  where id= {}".format(
                int(update.effective_user.id)
            )
        )
        for names in cursor:
            wallet = names[0]
        if names=="0":
            wallet="None"
        else:
            keyboard = [[InlineKeyboardButton("Go back", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(
                keyboard, resize_keyboard=True, one_time_keyboard=True
            )
            context.bot.send_message(
                chat_id=update.effective_user.id,
                text="Your Previous address is {} if you want to change please send a new address".format(wallet),
                reply_markup=reply_markup,
            )
            return EAS

    

def fas(update, context):
    try:

        msg = update.message.text
        msg=float(msg)
        conn = sqlite3.connect("mystock.db")
        conn.execute(
            "UPDATE wallet set quantity  = '{}' where ID = {} and stock='{}'".format(msg,
        update.effective_user.id
            )
        )
        conn.commit()
        conn.close()
        msg = update.message.text
        keyboard = [[InlineKeyboardButton("Main Menu", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Wallet address updated",
            reply_markup=reply_markup,
        )
        return CAS
    except:
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="invalid amount! send valid amount.",
            reply_markup=reply_markup,
        )
        return CAS


def cas(update, context):
    msg = update.message.text

    try:
        
        api_key = "VO6H8TH5F10IL39U"
        endpoint = "https://www.alphavantage.co/query"
        symbol = msg
        connection = sqlite3.connect("mystock.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT quantity from wallet where id= {}".format(
                int(update.effective_user.id)
            )
        )
        for names in cursor:
            am= names[0]

            am = float(am)
 
        endpoint = "https://www.alphavantage.co/query"
        params_eth = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": "ETH",
            "to_currency": "USD",
            "apikey": api_key,
        }
        response = requests.get(endpoint, params=params_eth)
        data = response.json()
        print(data)
        eth = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

        aso = eth * am
        amount_eth = am

        print("price:" ,aso)

        amount_usd = aso
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": api_key,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()

        latest_data = next(iter(data["Time Series (1min)"].values()))
        latest_price = latest_data["1. open"]
        latest_price = float(latest_price)
        amount_stock = aso / latest_price
        amount_stock = round(amount_stock, 4)
        print(amount_stock)
        endpoint = "https://www.alphavantage.co/query"
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": "ETH",
            "to_currency": "USD",
            "apikey": api_key,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        print(data)
        eth = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        print("am",am)
        print("ETH", eth)


        if eth <0.025:
            keyboard = [[InlineKeyboardButton("Go back", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(
                keyboard, resize_keyboard=True, one_time_keyboard=True
            )
            context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Minimum not met",
            reply_markup=reply_markup,
            )
            return BAS

        print("to eth", web3.to_wei(Decimal(aso), 'ether'))
        wei = web3.to_wei(Decimal(amount_eth), 'ether')  
        ase = round(amount_usd, 4)
        print(ase)
        connection = sqlite3.connect("mystock.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO COMPANY (ID,stock,status,price_bought,amount) \
            VALUES ({}, '{}','{}','{}','{}')".format(
                update.effective_user.id, symbol, "pending", latest_price, amount_stock
            )
        )
        connection.commit()
        connection.close()
        gg = "Symbol: {}\n\nStock amount: {}\n\nPrice of stock: {}\n\nIn order to buy the stock please send {} Eth to {} after sending amount you have to click on confirm order otherwise order will be cancel automatically".format(
            symbol, amount_stock, latest_price, amount_eth, "0x982749hdh08909"
        )
        keyboard = [
            [InlineKeyboardButton("Open in Metamask", url=f"https://metamask.app.link/send/0x3454E652Bd19ebA7447eDE7bD089EA48eCBfF33A@1?value={wei}")],

            [InlineKeyboardButton("Confirm Order", callback_data="confirm")],
            
            [InlineKeyboardButton("Cancel Order", callback_data="main_menu_cancel")],
        ]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id, text=gg, reply_markup=reply_markup
        )

    except Exception as e:
        print(e)
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Oops.. Invalid stock ticker format! Please provide the correct format (ex. AAPL, 0.4).",
            reply_markup=reply_markup,
        )
        return BAS


def das(update, context):
    msg = update.message.text
    connection = sqlite3.connect("mystock.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT Stock,status,price_bought,amount FROM COMPANY where id= {}".format(
            int(update.effective_user.id)
        )
    )
    for names in cursor:
        stock = names[0]
        status = names[1]
        price = float(names[2])
        amount = float(names[3])
    c=update.message.from_user
    ms=c.username
    ms=str(ms)
    if "None" in ms:
      ms=c.first_name
    else:
        usss="@{}".format(ms)
    hh = "User: {}\nSymbol: {}\nQuantity: {}\nInvst: ${}\n\nTranscational Hash: {}".format(usss,
        stock, amount, price, msg
    )
    keyboard = [
        [
            InlineKeyboardButton(
                "Confirm", callback_data="admin-{}".format(update.effective_user.id)
            ),
            InlineKeyboardButton(
                "Reject",
                callback_data="rejectorder-{}".format(update.effective_user.id),
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )
    context.bot.send_message(chat_id=807516030, text=hh, reply_markup=reply_markup)
    keyboard = [[InlineKeyboardButton("Main Menu", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Your patience is appreciated while we process the confirmation.",
        reply_markup=reply_markup,
    )

def eas(update, context):
    msg = update.message.text
    conn = sqlite3.connect("mystock.db")
    conn.execute(
        "UPDATE wallet set wallet = '{}' where ID = {}".format(msg,
       update.effective_user.id
        )
    )
    conn.commit()
    conn.close()
    msg = update.message.text
    keyboard = [[InlineKeyboardButton("Main Menu", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Wallet address updated",
        reply_markup=reply_markup,
    )
    return ConversationHandler.END

def bas(update, context):
    msg = update.message.text
    print(msg)
    try:
        api_key = "VO6H8TH5F10IL39U"
        endpoint = "https://www.alphavantage.co/query"
        symbol = msg
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": api_key,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()

        latest_data = next(iter(data["Time Series (1min)"].values()))
        latest_price = latest_data["1. open"]

        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="Current Price of {}: ${}".format(symbol, latest_price),
            reply_markup=reply_markup,
        )
        return ConversationHandler.END

    except:
        keyboard = [[InlineKeyboardButton("Cancel", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        )
        context.bot.send_message(
            chat_id=update.effective_user.id,
            text="invalid Stock! please send the correct stock",
            reply_markup=reply_markup,
        )
        return BAS


def main():
    updater = Updater(
        "1919009832:AAHiauPUWVHGQ2ZAVPolfUepTPV0MaKDVwE", use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button)],
        states={
            BAS: [MessageHandler(Filters.text, bas)],
            CAS: [MessageHandler(Filters.text, cas)],
            DAS: [MessageHandler(Filters.text, das)],
            EAS: [MessageHandler(Filters.text, eas)],
            FAS: [MessageHandler(Filters.text, fas)],
        },
        fallbacks=[CommandHandler("start", start)],
        allow_reentry=True,
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()