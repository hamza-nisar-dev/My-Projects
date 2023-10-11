from email import message
import discord
from discord.ext import commands
import sqlite3
from ethereum_address import is_address
bot = commands.Bot(command_prefix='/')



@bot.command(pass_context=True)
@commands.has_role("Whitelisted")
async def presalelist(ctx):
    channel=ctx.message.channel.id
    if channel==939852141940604929:
        msg=ctx.message.content
        msg=msg.split("/presalelist")
        msg=msg[1].strip()
        wall=msg
        msg=msg.split(" ")
        asd=len(msg)
        if asd==1:
            if is_address(wall):
                author_id= ctx.message.author.id
                author_name = ctx.message.author.name
                connection = sqlite3.connect("white.db")  
                cursor = connection.cursor()  
                cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(author_id)) 
                jobs = cursor.fetchall()
                if len(jobs) ==0:
                    conn = sqlite3.connect('white.db')
                    conn.execute("INSERT INTO COMPANY (ID,name,wallet) \
                        VALUES ('{}', '{}','{}')".format(author_id,author_name,wall))
                    conn.commit()
                    conn.close() 
                else:
                    conn = sqlite3.connect('white.db')
                    conn.execute("UPDATE COMPANY set wallet= '{}' where ID = '{}'".format(wall,author_id))
                    conn.commit()
                await ctx.send('Added to whitelist')
            else:
                await ctx.send('Invalid Address!')
            
        else:
            await ctx.send('Invalid format!')

        await ctx.message.delete()
@commands.has_role("Owner")
@bot.command()
async def getlist(ctx):
    channel=ctx.message.channel.id
    if channel==936618233262399488:
        channel = bot.get_channel(channel)
        connection = sqlite3.connect("white.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT wallet FROM COMPANY") 
        jobs = cursor.fetchall()
        textfile = open("addresses.txt", "w")
        for element in jobs:
            print(element)
            textfile.write(element[0] + ",")
        textfile.close()
        await channel.send('Check this', file=discord.File("addresses.txt"))
    
        

bot.run('OTM4MzYyMTgzMjExOTY2NDc0.YfpL4g.-dHwUedAqJcYcXoOdYTyRNflKYY')