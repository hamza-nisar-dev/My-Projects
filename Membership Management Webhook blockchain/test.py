import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import KeyboardButton
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from datetime import date
from dateutil.relativedelta import relativedelta
import sqlite3
import random
import string
from pyCoinPayments import CryptoPayments
IPN_URL = 'http://t.me/BPTSubscription_bot'
API_KEY = 'c1b66395ad7a9a99ca35e43edbe8df5376a6a33df74a27a5eb01f2ba8c899419'
API_SECRET = '9534C4f9Da52875D1b325Dd0685f9F299010F7204F650448d7664BcA71bd1458'
client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
post = {
    'txid' : "CPGD4XMEFHIZUKJNZAUIFMZBDF",}
transactionInfo = client.getTransactionInfo(post) 
print(transactionInfo)
c=transactionInfo['status']
print(c) 
