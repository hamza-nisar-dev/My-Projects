import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram import KeyboardButton, replykeyboardremove
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import sqlite3
from telegram import LabeledPrice
import re
import os
import  random 
import datetime 
from datetime import date
from datetime import timedelta
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
import sqlite3 as sql
from urlextract import URLExtract

extractor = URLExtract()
BAS,AAA,BBB,CCC,DDD,EE,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A99,A999,QWER,P1,P2,P3,P4,P22,P33,P44,P5,P6,P7,P8,P9,P10,P11= range(36)
wc=["welcome to bot shop"]
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    # check the payload, is this from your bot?
    if query.invoice_payload != 'Custom-Payload':
        # answer False pre_checkout_query
        query.answer(ok=False, error_message="Something went wrong...")
    else:
        query.answer(ok=True)

def start(update, context):
  user=update.effective_user.id
  print(user)
  connection = sqlite3.connect("user.db")  
  cursor = connection.cursor()  
  cursor.execute("SELECT ID FROM COMPANY where ID= '{}'".format(int(user))) 
  jobs = cursor.fetchall()
  if len(jobs) ==0:
      use = update.message.from_user
      usaa=use.username
      connection = sqlite3.connect("user.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,username,date_birth,body_type,height,race,weight,verification_numbers,report_numbers,contact_info,account_type) \
        VALUES ('{}', '{}','{}','{}','{}', '{}','{}','{}','{}','{}','{}')".format(int(user),usaa,"0","0","0","0","0","0","0","0","0"))
      connection.commit()
      connection.close()
      connection = sqlite3.connect("filters.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,Country,Age,Height,weight,race,bt,lf,pos,Tribe) \
        VALUES ('{}', '{}','{}','{}','{}', '{}','{}','{}','{}','{}')".format(int(user),"0","0","0","0","0","0","0","0","0"))
      connection.commit()
      connection.close()
  user = update.message.from_user
  usa=user.first_name
  foo = ['🍎', '🏉', '🎁', '🏮', '🚀','🎱']
  c=random.choice(foo)
  print(c)
  keyboard = [[InlineKeyboardButton("{}".format(c), callback_data='1')]]  
  reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
  context.bot.send_message(chat_id=update.message.chat_id,text="{} Please click on {} to prove you are a human".format(usa,c),reply_markup=reply_markup)
  
def USER(update, context):
    msg=update.message.text
    if  msg =="Free Profile":
        user=int(update.effective_user.id)
        conn = sqlite3.connect('user.db')
        conn.execute("UPDATE COMPANY set account_type = '{}' where ID = '{}'".format(msg,user))
        conn.commit()
        context.bot.send_message(chat_id=update.effective_user.id,text="Send your date of birth format: YYYY-MM-DD ",reply_markup=ReplyKeyboardRemove())
        return BAS
    elif msg =="Premium Profile":
        title = "Pay through Stripe"
        description = "Access premium features in bot"
        # select a payload just for you to recognize its the donation from your bot
        payload = "Custom-Payload"
        # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
        provider_token = "284685063:TEST:ZmIwYzdlZGZkNjgz"
        start_parameter = "live-payment"
        currency = "GBP"
        #price in dollars
        price = 3
        # price * 100 so as to include 2 decimal points
        prices = [LabeledPrice("Subscribe", price * 100)]
        # optionally pass need_name=True, need_phone_number=True,
        # need_email=True, need_shipping_address=True, is_flexible=True
        context.bot.send_invoice(
        
        update.effective_user.id, title, description, payload, provider_token, currency, prices, 
        )
        return QWER

def qwer(update, context):
    b = date.today() + timedelta(days=30)
    print (b) 
    c=update.effective_chat.id
    conn = sqlite3.connect('kick.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM COMPANY where id= {}".format(update.effective_user.id)) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        conn.execute("INSERT INTO COMPANY (ID,date) \
                VALUES ('{}','{}')".format(update.effective_user.id,b))
    
        conn.commit()
        conn.close()
    else:
        conn.execute("UPDATE COMPANY set date = '{}' where ID = {}".format(b,update.effective_user.id))
        conn.commit()
    user=int(update.effective_user.id)
    conn = sqlite3.connect('user.db')
    conn.execute("UPDATE COMPANY set account_type = '{}' where ID = '{}'".format("Premium Profile",user))
    conn.commit()
    context.bot.send_message(chat_id=update.effective_user.id,text="Send your date of birth format: YYYY-MM-DD ",reply_markup=ReplyKeyboardRemove())
    return BAS

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def bas(update, context):
    msg=update.message.text
    try:
        msg=msg.split("-")
        yy=int(msg[0])
        mm=int(msg[1])
        dd=int(msg[2])
        ag=age(date(yy,mm,dd))
        if ag>=18:
            user=int(update.effective_user.id)
            conn = sqlite3.connect('user.db')
            conn.execute("UPDATE COMPANY set date_birth = '{}' where ID = '{}'".format(msg,user))
            conn.commit()
            key=[["Asian","Black"],["Latino","Middle Eastern"],["Mixed","Native American"],["South Asian","White"],["Other"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Your Race:",reply_markup=reply_markup)
            return AAA
        else:
            context.bot.send_message(chat_id=update.effective_user.id,text="Only 18+ Profiles are Allowed")
            return BAS


    except:
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid format: YYYY-MM-DD ")
        return BAS
def aaa(update, context):
    msg=update.message.text
    user=int(update.effective_user.id)
    conn = sqlite3.connect('user.db')
    conn.execute("UPDATE COMPANY set race= '{}' where ID = '{}'".format(msg,user))
    conn.commit()
    key=[["Average","Large"],["Muscular","Slim"],["Stocky","Toned"],["Other"]]
    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select Your body type:",reply_markup=reply_markup)
    return BBB
def bbb(update, context):
    msg=update.message.text
    user=int(update.effective_user.id)
    conn = sqlite3.connect('user.db')
    conn.execute("UPDATE COMPANY set body_type = '{}' where ID = '{}'".format(msg,user))
    conn.commit()
    context.bot.send_message(chat_id=update.effective_user.id,text="Send your height in cm",reply_markup=ReplyKeyboardRemove())
    return CCC
def ccc(update, context):
    try:
        msg=update.message.text
        msg=float(msg)
        he=msg
        count = 0
        while msg != 0:
            msg //= 10
            count += 1
        if count==3:
            user=int(update.effective_user.id)
            conn = sqlite3.connect('user.db')
            conn.execute("UPDATE COMPANY set height = '{}' where ID = '{}'".format(he,user))
            conn.commit()
            context.bot.send_message(chat_id=update.effective_user.id,text="Send your Weight in Kg")
            return DDD
        else:
            context.bot.send_message(chat_id=update.effective_user.id,text="Invalid send only 3 digits ",reply_markup=ReplyKeyboardRemove())
            return CCC
    except:
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid send only 3 digits ",reply_markup=ReplyKeyboardRemove())
        return CCC

def ddd(update, context):
    try:
        msg=update.message.text
        msg=float(msg)
        count = 0
        while msg != 0:
            msg //= 10
            count += 1
        if count==3 or count ==2:
            user=int(update.effective_user.id)
            conn = sqlite3.connect('user.db')
            conn.execute("UPDATE COMPANY set weight = '{}' where ID = '{}'".format(msg,user))
            conn.commit()
            key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
            return EE
        else:
            context.bot.send_message(chat_id=update.effective_user.id,text="Invalid send only 3 or 2 digits ",reply_markup=ReplyKeyboardRemove())
            return DDD

    except:
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid send only 3 or 2 digits ",reply_markup=ReplyKeyboardRemove())
        return DDD

def ee(update, context):
    msg=update.message.text
    if msg=="Info, Terms and Conditions":
        keyboard = [[InlineKeyboardButton("Website",  url='https://www.dlpluglondon.com/telegramchannelinfo')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_user.id,text="Click on below button to see your terms and Conditions.",reply_markup=reply_markup)
        return EE
    elif msg=="Update Weight or Body Type":
        loc_keyboard = KeyboardButton(text="Update Weight")
        loc_keyboard2 = KeyboardButton(text="Update Body Type")
        loc_keyboard3 = KeyboardButton(text="Main Menu")
        keyboard = [[loc_keyboard],[loc_keyboard2],[loc_keyboard3 ]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Choose your option:",reply_markup=reply_markup)
        return A1
    elif msg=="View Channel":
        c=context.bot.getChat(chat_id=-1001746555418)
        cz=c['title']
        c=context.bot.createChatInviteLink(chat_id=-1001746555418,member_limit=1)
        link3=c['invite_link']
        keyboard = [[InlineKeyboardButton(cz,  url=link3)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_user.id,text="Click below button to view channel",reply_markup=reply_markup)
        return EE


    elif msg=="Report":
        key=[["Suspected Catfish","Abusive"],["Illegal Activity","Prohibited Behaviour"],["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="What you are reporting",reply_markup=reply_markup)
        return A4
    elif msg=="Contact Member":
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send members associated ID to receive their telegram username.",reply_markup=reply_markup)
        return A6
    elif msg=="Verify":
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="“By verifying a member, you agree that you have either met the individual in real life or have seen substantial evidence to verify the users profile information is correct. If several users you verify are removed from channel because of suspected catfishing your profile will automatically be removed and you will be unable to make another profile.\n\nAdd user id or username that you want to verify.",reply_markup=reply_markup)
        return A7
    elif msg=="Post":
        user = update.message.from_user
        usa=user.first_name
        foo = ['🍎', '🏉', '🎁', '🏮', '🚀','🎱']
        c=random.choice(foo)
        print(c)
        keyboard = [[InlineKeyboardButton("{}".format(c), callback_data='2')]]  
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.message.chat_id,text="{} Please click on {} to prove you are a human".format(usa,c),reply_markup=reply_markup)
    elif msg=="Premium Feature":
        conn = sqlite3.connect('kick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(update.effective_user.id)) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            context.bot.send_message(chat_id=update.effective_user.id,text="You dont have any active subscription.",)
        else:
            key=[["Hide Profile","Filtered Search"],["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P1
    
def p1(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        if msg=="Hide Profile":
            key=[["Age","Body Type","Ethnicity"],["Reset Filters"],["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option to hide profile from:',reply_markup=reply_markup)
            return P2
        elif msg=="Filtered Search":
            key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your filter',reply_markup=reply_markup)
            return P22

def p22(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    elif msg =="Reset Filters":
      connection = sqlite3.connect("filters.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,Country,Age,Height,weight,race,bt,lf,pos,Tribe) \
        VALUES ('{}', '{}','{}','{}','{}', '{}','{}','{}','{}','{}')".format(int(update.effective_user.id),"0","0","0","0","0","0","0","0","0"))
      connection.commit()
      connection.close()
      key=[["Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='FIlters reset successfully',reply_markup=reply_markup)
      return P22

    else:
        if msg=="Age":
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Send an age range, example: 28-30.',reply_markup=reply_markup)
            return P44
        elif msg=="Body Type":
            key=[["Average","Large"],["Muscular","Slim"],["Stocky","Toned"],["Other","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P33
        elif msg=="Ethnicity":
            key=[["Asian","Black"],["Latino","Middle Eastern"],["Mixed","Native American"],["South Asian","White"],["Other","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P5
        elif msg=="Country":
            countries=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe','Main Menu']
            cou=[]
            for names in countries:
                a=[]
                a.append(names)
                cou.append(a)
            reply_markup = ReplyKeyboardMarkup(cou,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P6
        elif msg=="Position":
            key=[['top', 'top vers'],['vers', 'bottom vers'],['bottom',"Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P7
        elif msg=="Looking For":
            key=[["Fun"], ["Dating"], ["Networking"],["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P8
        elif msg=="Tribe":
            key=[["Bear","Clean-Cut","Daddy"],["Discreet","DL","Geek"],["Jock","Leather","Poz"],["Rugged","Trans","Twink"],["Sober","Other","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option:',reply_markup=reply_markup)
            return P9
        elif msg=="Height":
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Send Height range from,to(110-124)',reply_markup=reply_markup)
            return P10
        elif msg=="Weight":
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Send Height Weight from,to(50-80)',reply_markup=reply_markup)
            return P11
        elif msg=="Filtered Result":
            conn = sqlite3.connect('filters.db')
            cursor = conn.execute("SELECT Country,Age,Height,weight,race,bt,lf,pos,Tribe from COMPANY where ID= '{}'".format(update.effective_user.id))
            for names in cursor:
                cu=names[0]
                ag=names[1]
                he=names[2]
                we=names[3]
                rc=names[4]
                bt=names[5]
                lf=names[6]
                pos=names[7]
                tr=names[8]
            a="SELECT Country,town,area,Age,height,weight,bt,wlf,race,lf,pos,Tribe,member,reports from COMPANY where "
            if cu!="0":
                a=a+"Country = '{}' AND ".format(cu)
            if ag!="0":
                sd=ag.split("-")
                q=int(sd[0])
                s=int(sd[1])
                a=a+"Age >= {} AND Age <= {} AND ".format(q,s)
            if he!="0":
                sd=ag.split("-")
                q=float(sd[0])
                s=float(sd[1])
                a=a+"Height >= {} AND Height <= {} AND ".format(q,s)
            if we!="0":
                sd=ag.split("-")
                q=float(sd[0])
                s=float(sd[1])
                a=a+"weight >= {} AND weight <= {} AND ".format(q,s)
            if rc!="0":
                a=a+"race= '{}' AND ".format(rc)
            if bt!="0":
                a=a+"bt= '{}' AND ".format(bt)
            if lf!="0":
                a=a+"lf= '{}' AND ".format(lf)
            if pos!="0":
                a=a+"pos= '{}' AND ".format(pos)
            if tr!="0":
                a=a+"Tribe= '{}'".format(tr)
            if a.endswith('AND '):
                a= a.removesuffix(' AND ')
            print(a)
            conn = sqlite3.connect('post.db')
            cursor = conn.execute(a)
            for names in cursor:
                print(names)
                cu=names[0]
                tw=names[1]
                ar=names[2]
                ag=names[3]
                he=names[4]
                we=names[5]
                bt=names[6]
                wlf=names[7]
                rc=names[8]
                lf=names[9]
                pos=names[10]
                tri=names[11]
                mem=names[12] 
                rep=names[13] 
                context.bot.send_message(chat_id=update.effective_user.id,text="Country: #{}  Town: #{} Area: #{} Age: #{} Height: #{} Body Type: #{} Looking For: #{} Tribe: #{} When: {} Member: {} Reports: {}".format(cu,tw,ar,ag,he,bt,lf,tri,wlf,mem,rep))
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='You can see the Filters result above:',reply_markup=reply_markup)
            return P22
        
def call_minute(context):
    job = context.job
    iu=job.context
    connection = sqlite3.connect("post.db")
    cursor = connection.execute("DELETE from COMPANY where ID='{}'".format(iu))
    connection.commit()
    connection.close()

def p2(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        if msg=="Age":
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Send Age range from,to(28-29)',reply_markup=reply_markup)
            return P4
        elif msg=="Body Type":
            key=[["Average","Large"],["Muscular","Slim"],["Stocky","Toned"],["Other","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option to hide profile from:',reply_markup=reply_markup)
            return P3
        elif msg=="Reset Filters":
            key=[["Main Menu"]]
            connection = sqlite3.connect("proh.db")  
            cursor = connection.cursor() 
            cursor.execute("DELETE FROM COMPANY Where ID= '{}'".format(int(update.effective_user.id)))
            connection.commit()
            connection.close() 
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Filters Reset Successfully',reply_markup=reply_markup)
            return P2
        elif msg=="Ethnicity":
            key=[["Asian","Black"],["Latino","Middle Eastern"],["Mixed","Native American"],["South Asian","White"],["Other","Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Choose your option to hide profile from:',reply_markup=reply_markup)
            return P3

def p3(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      connection = sqlite3.connect("proh.db")  
      cursor = connection.cursor() 
      cursor.execute("INSERT INTO COMPANY (ID,feat ) \
        VALUES ('{}', '{}')".format(int(update.effective_user.id),msg))
      connection.commit()
      connection.close() 
      key=[["Age","Body Type","Ethnicity"],["Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Added Successfully.',reply_markup=reply_markup)
      return P2

def p33(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set bt = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p5(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set race = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p6(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set Country = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p7(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set pos = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p4(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE

    else: 
      try:
        mg=msg
        msg=msg.split("-")
        a=int(msg[0])
        b=int(msg[1])
        connection = sqlite3.connect("age.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT ID FROM COMPANY where ID= '{}'".format(int(update.effective_user.id))) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            connection = sqlite3.connect("age.db")  
            cursor = connection.cursor() 
            cursor.execute("INSERT INTO COMPANY (ID,range) \
                VALUES ('{}', '{}')".format(int(update.effective_user.id),mg))
            connection.commit()
            connection.close() 
        else:
            conn = sqlite3.connect('age.db')
            conn.execute("UPDATE COMPANY set range = '{}' Where ID= '{}'".format(mg,int(update.effective_user.id)))
            conn.commit()
        key=[["Age","Body Type","Ethnicity"],["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Added Successfully.',reply_markup=reply_markup)
        return P2
      except:
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Invaid! range format: from-to(28-29)',reply_markup=reply_markup)
        return P4
def p44(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE

    else: 
      try:
        mg=msg
        msg=msg.split("-")
        a=int(msg[0])
        b=int(msg[1])
        conn = sqlite3.connect('filters.db')
        conn.execute("UPDATE COMPANY set Age = '{}' Where ID= '{}'".format(mg,int(update.effective_user.id)))
        conn.commit()
        key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
        return P22
      except:
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Invaid! range format: from-to(28-29)',reply_markup=reply_markup)
        return P44
def p8(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set lf = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p9(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:         
      conn = sqlite3.connect('filters.db')
      conn.execute("UPDATE COMPANY set Tribe = '{}' Where ID= '{}'".format(msg,int(update.effective_user.id)))
      conn.commit()
      key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
      reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
      context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
      return P22
def p10(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE

    else: 
      try:
        mg=msg
        msg=msg.split("-")
        a=float(msg[0])
        b=float(msg[1])
        conn = sqlite3.connect('filters.db')
        conn.execute("UPDATE COMPANY set Height = '{}' Where ID= '{}'".format(mg,int(update.effective_user.id)))
        conn.commit()
        key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
        return P22
      except:
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Invaid! range format: from-to(118-169)',reply_markup=reply_markup)
        return P10
def a9(update, context):
    msg=update.message.text
    countries=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe','Main Menu']
    if msg in countries:
        if msg =="Main Menu" or msg == "Reject":
            key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
            return EE
        else:
                global cu
                cu=msg
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="Send Your Town",reply_markup=reply_markup)
                return A99
    else:
        return A9

def p11(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE

    else: 
      try:
        mg=msg
        msg=msg.split("-")
        a=float(msg[0])
        b=float(msg[1])
        conn = sqlite3.connect('filters.db')
        conn.execute("UPDATE COMPANY set weight = '{}' Where ID= '{}'".format(mg,int(update.effective_user.id)))
        conn.commit()
        key=[["Age","Body Type","Ethnicity"],["Country","Position","Looking For"],["Tribe","Height","Weight"],["Filtered Result","Reset Filters","Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Filter Added Successfully.',reply_markup=reply_markup)
        return P22
      except:
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Invaid! range format: from-to(50-89)',reply_markup=reply_markup)
        return P11
def a99(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
            line = msg
            count = len(re.findall(r'\w+', line))
            web= extractor.find_urls(line)
            match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
            print(match)
            print(web)
            print(count)
            if match or web:
                context.bot.send_message(chat_id=update.effective_user.id,text="Invalid! It Should Not Contain Email or Website")
                return A99

            elif count>3:
                context.bot.send_message(chat_id=update.effective_user.id,text="Invalid! It Should Not Nontain More Than 3 Words")
                return A99
            else:
                global tw
                tw=msg
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="Send Your Area",reply_markup=reply_markup)
                return A999
   
def a999(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        line = msg
        count = len(re.findall(r'\w+', line))
        web= extractor.find_urls(line)
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        print(web)
        print(match)
        if match or web:
            context.bot.send_message(chat_id=update.effective_user.id,text="Invalid! It Should Not Contain Email or Website")
            return A999
        elif count>3:
            context.bot.send_message(chat_id=update.effective_user.id,text="Invalid! It Should Not Contain More Than 3 Words")
            return A999
        else:
            global ar
            ar=msg
            key=[['Top', 'Top Vers'],['Vers', 'Bottom Vers'],['Bottom',"Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Your Position",reply_markup=reply_markup)
            return A10

def a10(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        global pos
        pos=msg
        key=[["Fun"], ["Dating"], ["Networking"],["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="What You Are Looking For:",reply_markup=reply_markup)
        return A11
def a11(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        global loc
        loc=msg
        key=[["Bear","Clean-Cut","Daddy"],["Discreet","DL","Geek"],["Jock","Leather","Poz"],["Rugged","Trans","Twink"],["Sober","Other","Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send The Tribe:",reply_markup=reply_markup)
        return A12
def a12(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        global tri
        tri=msg
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="When Are You Looking For? Please Enter The Date in The Format YYYY-MM-DD",reply_markup=reply_markup)
        return A13

def a13(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        try:
            datetime.datetime.strptime(msg, '%Y-%m-%d')
            conn = sqlite3.connect('user.db')
            cursor = conn.execute("SELECT date_birth,race,height,weight,body_type,verification_numbers,report_numbers,race from COMPANY where ID= '{}'".format(update.effective_user.id))
            for names in cursor:
                dob=names[0]
                r=names[1]
                h=names[2]
                w=names[3]
                bt=names[4]
                vn=names[5]
                rem=names[6]
                rc=names[7]
            birth_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
            age = date.today().year - birth_date.year
            key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            connection = sqlite3.connect("filters.db")  
            cv=context.bot.send_message(chat_id=-1001746555418,text="Country: #{}\n\nTown: #{}\n\nArea: #{}\n\nAge: {}\n\nHeight: {}cm\n\nWeight: {}kg\n\nPosition: #{}\n\nBody Type: #{}\n\nRace: #{}\n\nLooking For: #{}\n\nTribe: #{}\n\nWhen: {}\n\nVerifications: {}\n\nMember ID: {}".format(cu,tw,ar,age,h,w,pos,bt,r,loc,tri,msg,vn,update.effective_user.id))
            ida=cv["message_id"]
            connection = sqlite3.connect("post.db")
            cursor = connection.cursor() 
            cursor.execute("INSERT INTO COMPANY (ID,Country,town,area,Age,height,weight,bt,wlf,race,lf,pos,Tribe,member,reports) \
                VALUES ('{}', '{}','{}','{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(ida),cu,tw,ar,age,h,w,bt,msg,rc,loc,pos,tri,update.effective_user.id,rem))
            connection.commit()
            connection.close()
            c=context.job_queue.run_repeating(call_minute, 172800, context=ida,name=str(update.message.message_id))
            context.bot.send_message(chat_id=update.effective_user.id,text="Post sent successfully",reply_markup=reply_markup)
            return EE
        except:
            key=[["Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Invalid! format YYYY-MM-DD",reply_markup=reply_markup)
            return A13

def button(update, context):
  query = update.callback_query
  a=query.data
  if a== '1':
    query.answer()
    loc_keyboard = KeyboardButton(text="Free Profile")
    loc_keyboard2 = KeyboardButton(text="Premium Profile")
    keyboard = [[loc_keyboard],[loc_keyboard2]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Select which type of profile you want to create",reply_markup=reply_markup)
  elif a=='2':
        print("check")
        countries=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe','Main Menu']
        cou=[]
        for names in countries:
            a=[]
            a.append(names)
            cou.append(a)
        reply_markup = ReplyKeyboardMarkup(cou,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select Your Country:",reply_markup=reply_markup)
        return A9
def a1(update, context):
    msg=update.message.text
    if  msg =="Update Body Type":
        key=[["Average","Large"],["Muscular","Slim"],["Stocky","Toned"],["Other"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Select Your body type:",reply_markup=reply_markup)
        return A2
    elif msg =="Update Weight":
        context.bot.send_message(chat_id=update.effective_user.id,text="Send your Weight in Kg",reply_markup=ReplyKeyboardRemove())
        return A3
    else:
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
def a3(update, context):
    msg=update.message.text
    user=int(update.effective_user.id)
    conn = sqlite3.connect('user.db')
    conn.execute("UPDATE COMPANY set weight = '{}' where ID = '{}'".format(msg,user))
    conn.commit()
    key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="weight updated successfully",reply_markup=reply_markup)
    return EE
def a2(update, context):
    msg=update.message.text
    user=int(update.effective_user.id)
    conn = sqlite3.connect('user.db')
    conn.execute("UPDATE COMPANY set body_type = '{}' where ID = '{}'".format(msg,user))
    conn.commit()
    key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Body type updated successfully",reply_markup=reply_markup)
    return EE
def a4(update, context):
    msg=update.message.text
    global rep
    rep=msg
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        key=[["Main Menu"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send the telegram username or channel ID of the profile you would like to report",reply_markup=reply_markup)
        return A5
def a6(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
            us=int(msg)
            conn = sqlite3.connect('kick.db')
            cursor = conn.cursor()
            a=0
            cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(us)) 
            jobs = cursor.fetchall()
            if len(jobs) ==0:
                a=0

            else:
                conn = sqlite3.connect('age.db')
                cursor = conn.execute("SELECT range from COMPANY where ID= '{}'".format(us))
                for names in cursor:
                    r=names[0]
                    r=r.split("-")
                    aa=int(r[0])
                    b=int(r[1])
                conn = sqlite3.connect('user.db')
                cursor = conn.execute("SELECT date_birth,body_type,race from COMPANY where ID= '{}'".format(update.effective_user.id))
                for names in cursor:
                    dob=names[0]
                    bt=names[1]
                    ra=names[2]
                birth_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
                age = date.today().year - birth_date.year
                age=int(age)
                if age> aa and age <b:
                    a=1
                conn = sqlite3.connect('proh.db')
                cursor = conn.cursor()
                cursor.execute("SELECT ID FROM COMPANY where ID = '{}' AND feat='{}'".format(us,bt)) 
                jobs = cursor.fetchall()
                if len(jobs) !=0:
                    a=1
                conn = sqlite3.connect('proh.db')
                cursor = conn.cursor()
                cursor.execute("SELECT ID FROM COMPANY where ID = '{}' AND feat='{}'".format(us,ra)) 
                jobs = cursor.fetchall()
                if len(jobs) !=0:
                    a=1
            if a==0:

                connection = sqlite3.connect("user.db")  
                cursor = connection.cursor()  
                cursor.execute("SELECT ID FROM COMPANY where ID= '{}'".format(us)) 
                jobs = cursor.fetchall()
                if len(jobs) !=0:
                    conn = sqlite3.connect('user.db')
                    cursor = conn.execute("SELECT username from COMPANY where ID= '{}'".format(us))
                    for names in cursor:
                        r=names[0]
                    key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="here is the username @{}".format(r),reply_markup=reply_markup)
                    return EE
                else:
                    key=[["Main Menu"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="user not found",reply_markup=reply_markup)
                    return A5
            else:
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="You cannot contact this user",reply_markup=reply_markup)
                return A5
def a7(update, context):
    msg=update.message.text
    global usf
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup,disable_web_page_preview=True)
        return EE
    else:
        try:
            us=int(msg)
            usf=us
            connection = sqlite3.connect("user.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT ID FROM COMPANY where ID= '{}'".format(us)) 
            jobs = cursor.fetchall()
            print(jobs)
            if len(jobs) !=0:
                conn = sqlite3.connect('verify.db')
                cursor = conn.execute("SELECT verify_by from COMPANY where ID= '{}'".format(us))
                for names in cursor:
                    vby=int(names[0])
                try:
                  print(vby)
                except:
                    vby=0
                if vby==int(update.effective_user.id):
                    key=[["Main Menu"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You already verify that user.",reply_markup=reply_markup)
                    return A7
                else:
                    conn = sqlite3.connect('user.db')
                    cursor = conn.execute("SELECT username,date_birth,body_type,height,weight,race from COMPANY where ID= '{}'".format(us))
                    for names in cursor:
                        us=names[0]
                        db=names[1]
                        bt=names[2]
                        h=names[3]
                        w=names[4]
                        r=names[5]
                    birth_date = datetime.datetime.strptime(db, '%Y-%m-%d')
                    age = date.today().year - birth_date.year
                    key=[["Confirm","Reject"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="Age: {}\nHeight: {}\nWeight: {}\nBody Type: {}\nRace: {}".format(age,h,w,bt,r),reply_markup=reply_markup)
                    return A8
            else:
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="user not found",reply_markup=reply_markup)
                return A7
        except:
            connection = sqlite3.connect("user.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT id FROM COMPANY where username= '{}'".format(msg)) 
            jobs = cursor.fetchall()
            print(jobs)
            if len(jobs) !=0:
                conn = sqlite3.connect('user.db')
                cursor = conn.execute("SELECT id from COMPANY where                                           username= '{}'".format(msg))
                for names in cursor:
                    us=names[0]
                conn = sqlite3.connect('verify.db') 
                cursor = conn.execute("SELECT verify_by from COMPANY where ID= '{}'".format(us))
                for names in cursor:
                    vby=int(names[0])
                try:
                  print(vby)
                except:
                    vby=0
                if vby==int(update.effective_user.id):
                    key=[["Main Menu"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You already verify that user.",reply_markup=reply_markup)
                    return A7
                else:
                    conn = sqlite3.connect('user.db')
                    cursor = conn.execute("SELECT ID,date_birth,body_type,height,weight,race from COMPANY where username= '{}'".format(msg))
                    for names in cursor:
                        us=names[0]
                        usf=us
                        db=names[1]
                        bt=names[2]
                        h=names[3]
                        w=names[4]
                        r=names[5]
                    birth_date = datetime.datetime.strptime(db, '%Y-%m-%d')
                    age = date.today().year - birth_date.year
                    key=[["Confirm","Reject"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="Age: {}\nHeight: {}\nWeight: {}\nBody Type: {}\nRace: {}".format(age,h,w,bt,r),reply_markup=reply_markup)
                    return A8
            else:
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="user not found",reply_markup=reply_markup)
                return A7
def a5(update, context):
    msg=update.message.text
    if msg =="Main Menu":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    else:
        try:
            us=int(msg)
            connection = sqlite3.connect("user.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT ID FROM COMPANY where ID= '{}'".format(us)) 
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('report.db')
                cursor = conn.execute("SELECT report_by from COMPANY where ID= '{}'".format(us))
                for names in cursor:
                    vby=int(names[0])
                try:
                  print(vby)
                except:
                    vby=0
                if vby==int(update.effective_user.id):
                    key=[["Main Menu"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You already report that user.",reply_markup=reply_markup)
                    return A5
                else:
                    conn = sqlite3.connect('user.db')
                    cursor = conn.execute("SELECT report_numbers from COMPANY where ID= '{}'".format(us))
                    for names in cursor:
                        r=int(names[0])
                        rt=r+1
                    print(rt)
                    if r>11:
                        context.bot.kick_chat_member(chat_id=-1001746555418,user_id=us)
                    connection = sqlite3.connect("report.db")  
                    cursor = connection.cursor()  
                    cursor.execute("SELECT ID FROM COMPANY where ID = '{}' and report='{}'".format(us,rep)) 
                    jobs = cursor.fetchall()
                    tot=len(jobs)
                    print(tot)
                    if tot>5:
                        context.bot.kick_chat_member(chat_id=-1001746555418,user_id=us)
                    conn = sqlite3.connect('user.db')
                    conn.execute("UPDATE COMPANY set report_numbers = '{}' where ID = '{}'".format(rt,us))
                    conn.commit()
                    conn = sqlite3.connect('report.db')
                    conn.execute("INSERT INTO COMPANY (ID,report,report_by) \
                        VALUES ('{}', '{}','{}')".format(us,rep,int(update.effective_user.id)))
                    conn.commit()
                    conn.close()
                    key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="Account reported successfully!",reply_markup=reply_markup)
                    return EE
            else:
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="user not found",reply_markup=reply_markup)
                return A5

        except:
            connection = sqlite3.connect("user.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT ID FROM COMPANY where username= '{}'".format(msg)) 
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('user.db')
                cursor = conn.execute("SELECT id from COMPANY where username= '{}'".format(msg))
                for names in cursor:
                    us=names[0]
                conn = sqlite3.connect('report.db')
                cursor = conn.execute("SELECT report_by from COMPANY where ID= '{}'".format(us))
                for names in cursor:
                    vby=int(names[0])
                try:
                  print(vby)
                except:
                    vby=0
                if vby==int(update.effective_user.id):
                    key=[["Main Menu"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You already report that user.",reply_markup=reply_markup)
                    return A7
                else:
                    conn = sqlite3.connect('user.db')
                    cursor = conn.execute("SELECT report_numbers from COMPANY where username= '{}'".format(msg))
                    for names in cursor:
                        r=int(names[0])
                        rt=r+1
                    if r>11:
                        context.bot.kick_chat_member(chat_id=-1001746555418,user_id=us)
                    connection = sqlite3.connect("report.db")  
                    cursor = connection.cursor()  
                    cursor.execute("SELECT ID FROM COMPANY where ID = '{}' and report='{}'".format(us,rep)) 
                    jobs = cursor.fetchall()
                    tot=len(jobs)
                    print(tot)
                    if tot>5:
                        context.bot.kick_chat_member(chat_id=-1001746555418,user_id=us)
                    conn = sqlite3.connect('user.db')
                    conn.execute("UPDATE COMPANY set report_numbers = '{}' where username = '{}'".format(rt,msg))
                    conn.commit()
                    conn = sqlite3.connect('report.db')
                    conn.execute("INSERT INTO COMPANY (ID,report,report_by) \
                        VALUES ('{}', '{}','{}')".format(us,rep,int(update.effective_user.id)))
                    conn.commit()
                    conn.close()
                    key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update weight or body type"]]
                    reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="Account reported successfully!",reply_markup=reply_markup)
                    return EE
            else:
                key=[["Main Menu"]]
                reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="user not found",reply_markup=reply_markup)
                return A5
def a8(update, context):
    msg=update.message.text
    if msg =="Main Menu" or msg == "Reject":
        key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update Weight or Body Type","View Channel"]]
        reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id, text='Welcome to  Main Menu',reply_markup=reply_markup)
        return EE
    elif msg=="Confirm":
            conn = sqlite3.connect('user.db')
            cursor = conn.execute("SELECT verification_numbers from COMPANY where ID= '{}'".format(usf))
            for names in cursor:
                r=int(names[0])
                rt=r+1
            conn = sqlite3.connect('user.db')
            conn.execute("UPDATE COMPANY set verification_numbers = '{}' where ID = '{}'".format(rt,usf))
            conn.commit()
            connection = sqlite3.connect("verify.db")  
            cursor = connection.cursor() 
            cursor.execute("INSERT INTO COMPANY (ID,verify_by) \
                VALUES ('{}', '{}')".format(usf,int(update.effective_user.id)))
            connection.commit()
            connection.close()
            key=[["Info, Terms and Conditions","Contact Member"],["Premium Feature","Post"],["Verify","Report"],["Update weight or body type"]]
            reply_markup = ReplyKeyboardMarkup(key,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Account is verified".format(r),reply_markup=reply_markup)
            return EE
def main():
    updater = Updater('5050210947:AAEI-n79U8lQv97WqwEx3MSUmlRU5gVQ0ds',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Free Profile|Premium Profile|)$'), USER),MessageHandler(Filters.regex('^(Main Menu|)$'), a8),CallbackQueryHandler(button)],

        states={
            
            BAS: [MessageHandler(Filters.text, bas)],
            AAA: [MessageHandler(Filters.regex('^(Asian|Black|Latino|Middle Eastern|Mixed|Native American|South Asian|White|Other)$'), aaa)],
            BBB: [MessageHandler(Filters.regex('^(Average|Large|Muscular|Slim|Stocky|Toned|Other)$'), bbb)], 
            CCC: [MessageHandler(Filters.text, ccc)], 
            DDD: [MessageHandler(Filters.text, ddd)], 
            EE: [MessageHandler(Filters.text, ee)],
            A1: [MessageHandler(Filters.text, a1)],
            A2: [MessageHandler(Filters.text, a2)],
            A3: [MessageHandler(Filters.text, a3)],
            A4: [MessageHandler(Filters.regex('^(Suspected Catfish|Abusive|Illegal Activity|Prohibited Behaviour|Main Menu)$'), a4)],
            A5: [MessageHandler(Filters.text, a5)],
            A6: [MessageHandler(Filters.text, a6)],
            A7: [MessageHandler(Filters.text, a7)], 
            A8: [MessageHandler(Filters.text, a8)],
            A9: [MessageHandler(Filters.text, a9)],
            A99: [MessageHandler(Filters.text, a99)],
            A999: [MessageHandler(Filters.text, a999)],
            A10: [MessageHandler(Filters.regex('^(Top|Top Vers|Vers|Bottom Vers|Bottom|Main Menu)$'), a10)],
            A11: [MessageHandler(Filters.regex('^(Fun|Dating|Networking|Main Menu)$'), a11)],
            A12: [MessageHandler(Filters.regex('^(Bear|Clean-Cut|Daddy|Discreet|DL|Geek|Jock|Leather|Poz|Rugged|Trans|Twink|Sober|Other|Main Menu)$'), a12)], 
            A13: [MessageHandler(Filters.text, a13)],
            P1: [MessageHandler(Filters.text, p1)],
            P2: [MessageHandler(Filters.text, p2)],
            P3: [MessageHandler(Filters.text, p3)],
            P4: [MessageHandler(Filters.text, p4)],
            P22: [MessageHandler(Filters.text, p22)],
            P33: [MessageHandler(Filters.text, p33)],
            P44: [MessageHandler(Filters.text, p44)],
            P5: [MessageHandler(Filters.text, p5)],
            P6: [MessageHandler(Filters.text, p6)],
            P7: [MessageHandler(Filters.text, p7)],
            P8: [MessageHandler(Filters.text, p8)],
            P9: [MessageHandler(Filters.text, p9)],
            P10: [MessageHandler(Filters.text, p10)],
            P11: [MessageHandler(Filters.text, p11)],
            QWER: [MessageHandler(Filters.successful_payment, qwer)],   
                                               
        },
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
    dp.add_handler(conv_handler) 
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

