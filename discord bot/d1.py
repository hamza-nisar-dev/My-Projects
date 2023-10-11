
import discord
from discord.ext import commands
import re
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import re
asf=[]
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('hamza.json', scope)
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    client = gspread.authorize(creds)
    Sheet=client.open('discord_bot').worksheet("Sheet1")
    for guild in bot.guilds:
        log_start = datetime.now()
        total_text_channels = len(guild.text_channels)
        total_voice_channels = len(guild.voice_channels)
        total_channels = total_text_channels  + total_voice_channels 
        number_msg = 0
        number_img = 0
        number_gif = 0
        number_30 = 0
        number_50 = 0
        number_100 = 0
        number_Q = 0
        med_link=0
        pic_ext = ['.jpg','.png','.jpeg']
        c=guild.text_channels
        for names in c:
           async for h in names.history(limit=None):
                pic_ext = ['.jpg','.png','.jpeg']
                for ext in pic_ext:
                        typ=(h.attachments)
                        for names in typ:
                            if ext in names.filename.lower():
                              number_img += 1
                for names in h.attachments:
                    if ".gif" in names.filename.lower():
                      number_gif+=1
                msg=h.content
                a=Find(msg)
                for names in a:
                    if "medium" in names:
                        med_link+=1
                if "?" in msg:
                    number_Q+=1
                msg=msg.split(" ")
                a=len(msg)
                if a>30:
                    number_30+=1
                if a>50:
                    number_50+=1
                if a>100:
                    number_100+=1
                number_msg += 1
        log_end = datetime.now() 
        print(log_start)
        print(log_end)
        print(guild.id)
        print(guild.name)
        print(number_msg)
        print(number_img)
        print(number_gif)
        print(number_30)
        print(number_50)
        print(number_100)
        print(number_Q)
        print(med_link)
        print(total_channels)
        insertRow = [str(log_start),str(log_end),guild.id,guild.name,total_channels,number_msg,number_img,number_gif,number_30,number_50,number_100,number_Q,med_link]
        Sheet.insert_row(insertRow,2)

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
bot.run('OTIyNDU1NDc0NzYxMjQwNTc3.YcBtmw.vVXN28xG06CrxhpcevnSHPWvau8')