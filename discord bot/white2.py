
import discord
from discord import member, user
from discord.ext import commands
import random
import sqlite3
import string
import csv
import os
from discord.utils import get
import time
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('/'),intents=discord.Intents.all())
bot = Bot()
@bot.event
async def on_member_join(member):
            ax=member.id
            print(ax)
            role = get(member.guild.roles, name="unverified")
            await member.add_roles(role)
            ch=await bot.fetch_channel(943842905167114280)
            foo = ['🍎', '🏉', '🎁', '🏮', '🚀','🎱']
            c=random.choice(foo)
            conn = sqlite3.connect('lead.db')
            conn.execute("INSERT INTO COMPANY (id,username,email,captcha) \
                VALUES ('{}', '{}','{}','{}')".format(ax,member.name,"0",c))
            conn.commit()
            conn.close() 
            time.sleep(10)
            msg = await ch.send("@{} REACT WITH {} to prove you are a human".format(member.name,c))
            await msg.add_reaction('👍')
            await msg.add_reaction('🍎')
            await msg.add_reaction('🏉')
            await msg.add_reaction('🎁')
            await msg.add_reaction('🏮')
            await msg.add_reaction('🚀')
            await msg.add_reaction('🎱')
            

@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user:
        vb=reaction.emoji
        conn = sqlite3.connect('lead.db')
        cursor=conn.execute("SELECT id FROM COMPANY where id= '{}'".format(user.id)) 
        jobs= cursor.fetchall()
        c=len(jobs)
        if c!=0:
            conn = sqlite3.connect('lead.db')
            cursor=conn.execute("SELECT captcha FROM COMPANY where id= '{}'".format(user.id)) 
            jobs= cursor.fetchall()
            for name in jobs:
                cv=name[0]
            if cv!="0":
                if cv==vb:
                    ch=await bot.fetch_channel(943842905167114280) 
                    await ch.send("@{}, Send me your email to get access to channels?".format(user.name))
                    while(True):
                        mm=await bot.wait_for('message') 
                        msg=mm.content
                        ide=mm.author.id
                        await mm.delete()
                        if ide==user.id:
                            conn = sqlite3.connect('lead.db')
                            conn.execute("UPDATE COMPANY set email= '{}' where ID = '{}'".format(msg,ide))
                            conn.commit()
                            role = get(user.guild.roles, name="verified")
                            await user.add_roles(role)  
                            role = get(user.guild.roles, name="unverified")
                            await user.remove_roles(role)  
                            break

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