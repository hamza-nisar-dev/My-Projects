
import time
import discord
from discord import member, user
from discord.ext import commands
import random
import sqlite3
import string
import csv
import os
import random
from captcha.image import ImageCaptcha
import string
from discord.utils import get
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('/'),intents=discord.Intents.all())
bot = Bot()
@bot.event
async def on_member_join(member):
            ax=member.id
            role = get(member.guild.roles, name="unverified")
            await member.add_roles(role)
            ch=await bot.fetch_channel(952928690742910995)
            letters = string.ascii_uppercase
            c=[''.join(random.choice(letters) for i in range(5))]
            c=c[0]
            print(c)
            conn = sqlite3.connect('lead.db')
            conn.execute("INSERT INTO COMPANY (id,username,email,captcha) \
                VALUES ('{}', '{}','{}','{}')".format(ax,member.name,"0",c))
            conn.commit()
            conn.close() 
            img = ImageCaptcha()
            image = img.generate_image(c)
            image.save('python.jpg')
            cv=await ch.send("Please solve this captcha to verify you are a human first.", file=discord.File("python.jpg"))
            cva=cv.id
            print(cva)
            while(True):
                mm=await bot.wait_for('message') 
                msg=mm.content
                ide=mm.author.id

                if ide==ax:
                    conn = sqlite3.connect('lead.db')
                    cursor=conn.execute("SELECT captcha FROM COMPANY where id= '{}'".format(ax)) 
                    jobs= cursor.fetchall()
                    for name in jobs:
                        cv=name[0]
                    if cv!="0":
                        if cv==msg:
                            await mm.delete()
                            await bot.http.delete_message(952928690742910995,cva)
                            ch=await bot.fetch_channel(952928690742910995) 
                            cb=await ch.send("Final step - please type your email address to unlock all the channels.")
                            print(cb.id)
                            while(True):
                                mm=await bot.wait_for('message') 
                                await bot.http.delete_message(952928690742910995,cb.id)
                                msg=mm.content
                                ide=mm.author.id
                                user=mm.author
                                await mm.delete()
                                if ide==ax:
                                    conn = sqlite3.connect('lead.db')
                                    conn.execute("UPDATE COMPANY set email= '{}' where ID = '{}'".format(msg,ide))
                                    conn.commit()
                                    role = get(user.guild.roles, name="verified")
                                    await user.add_roles(role)  
                                    role = get(user.guild.roles, name="unverified")
                                    await user.remove_roles(role)  
                                    break
                            break
                        else:
                            await mm.delete()
                            print(cva)
                            ch=await bot.fetch_channel(952928690742910995)
                            await bot.http.delete_message(952928690742910995,cva)
                            letters = string.ascii_uppercase
                            c=[''.join(random.choice(letters) for i in range(5))]
                            c=c[0]
                            print(c)
                            conn = sqlite3.connect('lead.db')
                            conn.execute("UPDATE COMPANY set captcha= '{}' where ID = '{}'".format(c,ax))
                            conn.commit()
                            img = ImageCaptcha()
                            image = img.generate_image(c)
                            image.save('python.jpg')
                            cvd=await ch.send("Please solve this captcha to verify you are a human first.", file=discord.File("python.jpg"))
                            cva=cvd.id
             


            


@commands.has_role("Admin")
@bot.command()
async def getlist(ctx):
    conn=sqlite3.connect('lead.db')
    cur = conn.cursor()
    cur.execute('''SELECT id,username,email FROM COMPANY''')
    rows = cur.fetchall()    
    cursor = conn.cursor()
    cursor.execute("select id,username,email from COMPANY")
    with open("data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/data.csv"
    conn.close()
    await ctx.send('Check this', file=discord.File("data.csv"))
bot.run('OTU1MjE2MTY0MTc3NDczNTQ2.YjecYA.w19C82sJeeXgdVEh5ziAS67Wz7w')