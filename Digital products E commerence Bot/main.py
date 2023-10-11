import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import sqlite3
import random
from coinbase_commerce.client import Client

API_KEY = "c9ae131d-76b5-46dd-8023-a1a01226d818"
client = Client(api_key=API_KEY)

def start(update, context):
  bnm=update.message.from_user

  ms=bnm.first_name

  print(update.effective_user.id)
  user = update.message.from_user
  usa=str(update.effective_user.id)
  if usa ==  "1394902938" or usa=="807516m030":
    keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
    
  else:
    keyf=[["𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗠𝗲𝗻𝘂📜","𝗙𝗔𝗤 ❓","𝗛𝗼𝘄 𝗶𝘀 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁? 🌐"],["𝗣𝗵𝗶𝗮 𝗠𝗮𝗿𝗸𝗲𝘁 𝗟𝗶𝗻𝗸 🔗"]]
    reply_markup = ReplyKeyboardMarkup(keyf,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="𝗪𝗲𝗹𝗰𝗼𝗺𝗲🌟\nto CVV Verified Bot 𝗺𝗲𝗻𝘂\n\n𝗡𝗮𝘃𝗶𝗴𝗮𝘁𝗲 𝗵𝗲𝗿𝗲 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂 📂",reply_markup=reply_markup)   
def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    msg_id=update.callback_query.message.message_id
    if a== 'Main_menu':
       context.bot.delete_message(chat_id=update.effective_user.id,message_id=msg_id)
       keyf=[["𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗠𝗲𝗻𝘂📜","𝗙𝗔𝗤 ❓","𝗛𝗼𝘄 𝗶𝘀 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁? 🌐"],["𝗣𝗵𝗶𝗮 𝗠𝗮𝗿𝗸𝗲𝘁 𝗟𝗶𝗻𝗸 🔗"]]
       reply_markup = ReplyKeyboardMarkup(keyf,resize_keyboard=True)
       context.bot.send_message(chat_id=update.effective_user.id,text="𝗪𝗲𝗹𝗰𝗼𝗺𝗲🌟\nto CVV Verified Bot 𝗺𝗲𝗻𝘂\n\n𝗡𝗮𝘃𝗶𝗴𝗮𝘁𝗲 𝗵𝗲𝗿𝗲 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂 📂",reply_markup=reply_markup)
    elif "vendor" in a:
      vend=a.split("vendor-")
      vend=vend[1]
      connection = sqlite3.connect("database.db")  
      cursor = connection.cursor()  
      keyf=[]
      cursor.execute("SELECT name from products where catagory = '{}'".format(vend))
      for names in cursor:
        name=names[0]
        key=[InlineKeyboardButton(name, callback_data="pro-{}".format(names[0]))]
        keyf.append(key)
      keyf.append([InlineKeyboardButton("🔙 Back", callback_data="back")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=msg_id,text="*Please select your product below:*",reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)

    elif a=="back":
      connection = sqlite3.connect("database.db")  
      cursor = connection.cursor()  
      keyf=[]
      cursor.execute("SELECT name from catagories")
      for names in cursor:
        name=names[0]
        key=[InlineKeyboardButton(name, callback_data="vendor-{}".format(names[0]))]
        keyf.append(key)
      keyf.append([InlineKeyboardButton("🔙 Cancel", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=msg_id,text="*Please select your catagory below:*",reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
    
    elif "pro" in a:
      vend=a.split("pro-")
      vend=vend[1]
      connection = sqlite3.connect("database.db")  
      cursor = connection.cursor()  
      keyf=[]
      cursor.execute("SELECT price,description from products where name = '{}'".format(vend))
      for names in cursor:
        pr=float(names[0])
        des=names[1]
      keyf.append([InlineKeyboardButton("Purchase ✅", callback_data="pur-{}".format(vend))],[InlineKeyboardButton("🔙 cancel", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=msg_id,text="*Product name: {}\nProduct Price: {}*\n\n{}".format(vend,pr,des),reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
    elif "pur-" in a:
      vend=a.split("pur-")
      vend=vend[1]
      cursor.execute("SELECT price from products where name = '{}'".format(vend))
      for names in cursor:
        pr=float(names[0])
       
      charge = client.charge.create(name='Telegram botShop',
                            description='Pay to add credit to your wallet',
                            pricing_type='no_price',
                            local_price={ 
                        })
      linka=charge["hosted_url"]
      coda=charge["id"]          
      keyboard =[[InlineKeyboardButton("Make a Payment",url=linka)],[InlineKeyboardButton("🔙 cancel", callback_data="Main_menu")]]
      reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
      context.bot.edit_message_text(chat_id=update.effective_user.id,message_id=msg_id,text="Click on below button to make payment procuct send to your after payment confirmation.",reply_markup=reply_markup) 
    if a== '1':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send name of product",reply_markup=reply_markup) 
        return QW
def qw(update,context):
    msg=update.message.text
    global nm
    nm =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send Description of product" ,reply_markup=reply_markup)
    return DESCR 
def descr(update,context):
  msg=update.message.text
  global dsr
  dsr=msg
  keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Send Special product ID" ,reply_markup=reply_markup)
  return RRT
def rrt(update,context):
  msg=update.message.text
  global pid
  pid=msg
  keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
  context.bot.send_message(chat_id=update.effective_user.id,text="Send price of product" ,reply_markup=reply_markup)
  return PRII

def prii(update,context):
  msg=update.message.text
  try:
    msg=float(msg)
    global tp
    tp=msg
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send text file contain delivery each line of txt file send in delivery.",reply_markup=reply_markup)
    return FILA
  except:
    keyboard =[[InlineKeyboardButton("Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Wrong Format\nSend price of product in digits",reply_markup=reply_markup)
    return PRII

def fila(update,context):
    vc=update.message.document.file_id
    global fill
    fill="0"
    file1 = context.bot.getFile(update.message.document.file_id)
    file1.download('{}.txt'.format(pid))
    yu= random.randint (0,999999)
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO COMPANY (ID,oi,de,pr,fi,name,pid) \
                      VALUES ('{}', '{}','{}', '{}','{}', '{}', '{}')".format(str(update.effective_user.id),yu,dsr,tp,"1",nm,pid))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Account added" ,reply_markup=reply_markup)
    return BUTTON

def menu(update, context):
   a=update.message.text
   if a=="𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗠𝗲𝗻𝘂📜":
      connection = sqlite3.connect("database.db")  
      cursor = connection.cursor()  
      keyf=[]
      cursor.execute("SELECT name from catagories")
      for names in cursor:
        name=names[0]
        key=[InlineKeyboardButton(name, callback_data="vendor-{}".format(names[0]))]
        keyf.append(key)
      keyf.append([InlineKeyboardButton("🔙 Back", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="*Please select your catagory below:*",reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
   elif a=="𝗙𝗔𝗤 ❓":
      a="How does it work\n\n?It differs with every product.\nEach product comes with a guide. Except for the 𝗙𝘂𝗹𝗹𝘇/𝗗𝘂𝗺𝗽𝘀/𝗩𝗶𝗿𝘁𝘂𝗮𝗹 𝗖𝗮𝗿𝗱 🏧, if you want to go to crypto, for example, the guide 𝗖𝗖 𝘁𝗼 𝗕𝗧𝗖, and for PayPal is the guide 𝗖𝗖 𝗣𝗔𝗬𝗣𝗔𝗟 𝗣𝗔𝗬𝗣𝗔𝗟. Furthermore, it is not difficult, you can also simply buy products on Amazon, for example.\n\nshipping?\n\nGetting shipped with DHL Express, in live in the middle of the EU\n𝗘𝗨: 𝟮-𝟯 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗱𝗮𝘆𝘀\n𝗨𝗦𝗔/𝗖𝗔𝗡: 𝟯-𝟱 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗱𝗮𝘆𝘀\n𝗔𝗨𝗦: 𝟯-𝟱 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗱𝗮𝘆𝘀\n𝗔𝗦𝗜𝗔: 𝟯-𝟱 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗱𝗮𝘆𝘀\n𝗔𝗙𝗥𝗜𝗖𝗔: 𝟯-𝟰 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗱𝗮𝘆𝘀\nWhy I use dhl, beceause dhl has a low border security and a more accurate track and trace system. Each order get shipped the next working day.\n\nWorldwide useage\n\nEverything is worldwide, Most of the products we offer are online. But the physical products are also worldwide.\n\nIf you have more questions, ask them to, @CVVPhia on telegram."
      keyf=[]
      keyf.append([InlineKeyboardButton("🔙 Back", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text=a,reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
   elif a=="𝗛𝗼𝘄 𝗶𝘀 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁? 🌐":
      keyf=[]
      print("here")
      keyf.append([InlineKeyboardButton("🔙 Back", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="𝗛𝗼𝘄 𝗶𝘀 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁? 🌐\n\n𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁𝘀 𝗶 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗮𝗰𝗰𝗲𝗽𝘁 𝗮𝗿𝗲\n- 𝗕𝗧𝗖, 𝗘𝗧𝗛, 𝗟𝗧𝗖, 𝗨𝗦𝗗𝗧.\n\n𝗗𝗼𝗻𝘁 𝗵𝗮𝘃𝗲 𝗰𝗿𝘆𝗽𝘁𝗼? 𝗡𝗼 𝗽𝗿𝗼𝗯𝗹𝗲𝗺, 𝗴𝗲𝘁 𝗮 𝗰𝗿𝘆𝗽𝘁𝗼 𝘃𝗼𝘂𝗰𝗵𝗲𝗿!\n\n• cryptovoucher.io 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝙨𝙞𝙩𝙚\n\n• Dundle.com\n  • G2A.com \n• Kinguin.net \n• Gamecardsdirect.com \n• Vgo-shop.com\n• Kaartdirect.nl\n\n𝗖𝗿𝘆𝗽𝘁𝗼 is the only 𝘀𝗮𝗳𝗲𝘀𝘁 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝗼𝗽𝘁𝗶𝗼𝗻 to ensure the 𝗮𝗻𝗼𝗻𝘆𝗺𝗶𝘁𝘆 𝗮𝗻𝗱 𝘀𝗲𝗰𝘂𝗿𝗶𝘁𝘆 for buyers and sellers.\n...",reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
   elif a=="𝗣𝗵𝗶𝗮 𝗠𝗮𝗿𝗸𝗲𝘁 𝗟𝗶𝗻𝗸 🔗":
      keyf=[]
      keyf.append([InlineKeyboardButton("🔙 Back", callback_data="Main_menu")])
      reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id,text="𝘠𝘰𝘶 𝘯𝘦𝘦𝘥 𝙏𝙊𝙍 𝘽𝙧𝙤𝙬𝙨𝙚𝙧 𝘵𝘰 𝘶𝘴𝘦 𝘵𝘩𝘦\n𝘪𝘯𝘬, 𝘪𝘵’𝘴 𝙎𝙚𝙘𝙪𝙧𝙚 𝘢𝘯𝘥 𝘱𝘳𝘪𝘷𝘢𝘵𝘦 𝘰𝘯 𝘥𝘢𝘳𝘬𝘸𝘦𝘣 𝙉𝙚𝙩𝙬𝙤𝙧𝙠.\n\n⚠️𝙎𝙩𝙤𝙧𝙚 𝙤𝙣𝙡𝙮 𝙖𝙘𝙘𝙚𝙨𝙨𝙞𝙗𝙡𝙚 𝙤𝙣 𝙏𝙤𝙧 𝙗𝙧𝙤𝙬𝙨𝙚𝙧, 𝙡𝙞𝙣𝙠 𝙩𝙤 𝙨𝙩𝙤𝙧𝙚 .𝙤𝙣𝙞𝙤𝙣:⚠️\n\n𝗪𝗲𝗯𝘀𝗶𝘁𝗲 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲!\n\n𝗣𝗿𝗼𝗱𝘂𝗰𝘁𝘀:\n\n💳 𝗣𝗵𝘆𝘀𝗶𝗰𝗮𝗹 𝗖𝗹𝗼𝗻𝗲𝗱 𝗖𝗮𝗿𝗱𝘀 \n💻 𝗣𝗮𝘆𝗽𝗮𝗹 𝗮𝗰𝗰𝗼𝘂𝗻𝘁\n🪪 𝗜𝗱𝗲𝗻𝘁𝗶𝘁𝘆 𝗖𝗮𝗿𝗱 \n📚 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗚𝘂𝗶𝗱𝗲𝘀 \n📈 𝗖𝗿𝘆𝗽𝘁𝗼 𝗮𝗰𝗰𝗼𝘂𝗻𝘁\n🛠 𝗖𝗹𝗼𝗻𝗶𝗻𝗴 𝘀𝗼𝗳𝘁𝘄𝗮𝗿𝗲 \n🏧 𝗙𝘂𝗹𝗹𝘇/𝗗𝘂𝗺𝗽𝘀/𝗩𝗶𝗿𝘁𝘂𝗮𝗹 𝗖𝗮𝗿𝗱 \n🐁 𝗥𝗮𝘁𝘀 & 𝗩𝗶𝗿𝘂𝘀 & 𝗥𝗮𝗻𝘀𝗼𝗺𝘄𝗮𝗿𝗲",reply_markup=reply_markup,parse_mode=telegram.ParseMode.MARKDOWN)
      
def main():  
  updater = Updater("6053161068:AAF78zNpWqJclV5EGroCQ0eeiDW_iIzqCc8", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(MessageHandler(Filters.regex('^(𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗠𝗲𝗻𝘂📜|𝗙𝗔𝗤 ❓|𝗛𝗼𝘄 𝗶𝘀 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁? 🌐|𝗣𝗵𝗶𝗮 𝗠𝗮𝗿𝗸𝗲𝘁 𝗟𝗶𝗻𝗸 🔗)$'), menu))
  dp.add_handler(CallbackQueryHandler(button))
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()
       