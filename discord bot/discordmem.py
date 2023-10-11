from discord import guild, member, user
from discord.ext import commands
import sqlite3
import mysql.connector
import datetime
from mysql.connector import Error
from dateutil.relativedelta import relativedelta
from datetime import datetime as dn
from discord.ext import tasks
import discord
from discord.utils import get
bot = commands.Bot(command_prefix='/')

@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("Please provide the email used to join at koinplug.com")
    mm= await bot.wait_for('message')
    user=mm.author.id
    msg=mm.content
    msg.strip()
    msg=msg.lower()
    try:
        connection = sqlite3.connect("vision.db")  
        cursor = connection.execute("SELECT email from COMPANY where ID= '{}'".format(user))
        em="0"
        for names in cursor:
            em=names[0]
        cursor.execute("SELECT email FROM COMPANY where email= '{}'".format(msg)) 
        jobs= cursor.fetchall()
        c=len(jobs)
        print(c)
        if msg==em:
            c=0
        if c ==0:
            connection = mysql.connector.connect(host='koinplug.com',
                database='i7587954_wp1',
                user='telebot',
                password='raja1260')
            mycursor = connection.cursor()
            sqla="SELECT customer_id FROM wp_wc_customer_lookup WHERE email ='{}'".format(msg)
            mycursor.execute(sqla)
            myresult = mycursor.fetchall()
            a=myresult[0][0]
            print(a)
            sqla="SELECT date_created FROM wp_wc_order_product_lookup WHERE customer_id= {}".format(a)
            mycursor.execute(sqla)
            myresult = mycursor.fetchall()
            for names in myresult:
                dty=names[0]   
            print(dty)        
            dt=dty+ relativedelta(months=1)
            vb=datetime.datetime.now().utcnow()
            if dt>vb:
                print("in")
                member = ctx.message.author.id
                guild=await bot.fetch_guild(875527884830306314)
                mem=await guild.fetch_member(int(member))
                role = discord.utils.get(guild.roles, name='Koin Plug Pro')
                print(role)
                await mem.add_roles(role)
                await mm.reply("Success, you now have access to private koin plug alert rooms.")
                connection = sqlite3.connect("vision.db")  
                cursor = connection.cursor()  
                cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(user)) 
                jobs = cursor.fetchall()
                if len(jobs) ==0:
                    conn = sqlite3.connect('vision.db')
                    conn.execute("INSERT INTO COMPANY (ID,email,customer_id) \
                        VALUES ('{}', '{}','{}')".format(user,msg,str(a)))
                    conn.commit()
                    conn.close() 

                else:
                    conn = sqlite3.connect('vision.db')
                    conn.execute("UPDATE COMPANY set email= '{}', customer_id= '{}' where ID = '{}'".format(msg,str(a),user))
                    conn.commit()
            else:
                await mm.reply("Your Subscription is expired!")
        else:
            await mm.reply("User already registered with this email")  
    except:    
        await mm.reply("Sorry, no subscription found under email provided, please type /start to try again.")

@bot.command(pass_context=True)
async def iniciar(ctx):
    await ctx.send('Proporcione el correo electrónico que utilizó para suscribirse en koinplug.com')
    mm= await bot.wait_for('message')
    user=mm.author.id
    msg=mm.content
    msg.strip()
    msg=msg.lower()
    try:
        connection = sqlite3.connect("vision.db")  
        cursor = connection.execute("SELECT email from COMPANY where ID= '{}'".format(user))
        em="0"
        for names in cursor:
            em=names[0]
        cursor.execute("SELECT email FROM COMPANY where email= '{}'".format(msg)) 
        jobs= cursor.fetchall()
        c=len(jobs)
        if msg==em:
            c=0
        if c ==0:
            connection = mysql.connector.connect(host='koinplug.com',
                database='i7587954_wp1',
                user='telebot',
                password='raja1260')
            mycursor = connection.cursor()
            sqla="SELECT customer_id FROM wp_wc_customer_lookup WHERE email ='{}'".format(msg)
            mycursor.execute(sqla)
            myresult = mycursor.fetchall()
            a=myresult[0][0]
            print(a)
            sqla="SELECT date_created FROM wp_wc_order_product_lookup WHERE customer_id= {}".format(a)
            mycursor.execute(sqla)
            myresult = mycursor.fetchall()
            for names in myresult:
                dty=names[0]   
            print(dty)        
            dt=dty+ relativedelta(months=1)
            vb=datetime.datetime.now().utcnow()
            if dt>vb:
                print("in")
                member = ctx.message.author.id
                guild=await bot.fetch_guild(871729338733690910)
                mem=await guild.fetch_member(int(member))
                role = discord.utils.get(guild.roles, name='Koin Plug Pro')
                print(role)
                await mem.add_roles(role)
                m = await mm.reply("Éxito, ahora tiene acceso a salas privadas de koin plug alertas.")
                connection = sqlite3.connect("vision.db")  
                cursor = connection.cursor()  
                cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(user)) 
                jobs = cursor.fetchall()
                if len(jobs) ==0:
                    conn = sqlite3.connect('vision.db')
                    conn.execute("INSERT INTO COMPANY (ID,email,customer_id) \
                        VALUES ('{}', '{}','{}')".format(user,msg,str(a)))
                    conn.commit()
                    conn.close() 

                else:
                    conn = sqlite3.connect('vision.db')
                    conn.execute("UPDATE COMPANY set email= '{}', customer_id= '{}' where ID = '{}'".format(msg,str(a),user))
                    conn.commit()
            else:
                await mm.reply("Su suscripción ha caducado")
        else:
            await mm.reply("Usuario ya registrado con este correo electrónico")  
    except:    
        await mm.reply("Lo sentimos, no se encontró ninguna suscripción en el correo electrónico proporcionado, escriba /iniciar a intentarlo de nuevo.")

@bot.event
async def on_member_join(member):
    print(member) 
    if str(member.guild.id)=="875527884830306314":
     await member.send("Please send /start to access private channels or visit koinplug.com to start receiving trading alerts today.")
    else:
     await member.send("Envíe /iniciar para acceder a los canales privados o visite koinplug.com para comenzar a recibir alertas hoy.")

@tasks.loop(seconds = 85400)
async def test():
    connection = sqlite3.connect("vision.db")  
    cursor = connection.execute("SELECT id,customer_id FROM COMPANY")
    for names in cursor:        
        try:
            idd=names[0]
            ed=names[1]
            connection = mysql.connector.connect(host='koinplug.com',
                database='i7587954_wp1',
                user='telebot',
                password='raja1260')
            mycursor = connection.cursor()
            sqla="SELECT date_created FROM wp_wc_order_product_lookup WHERE customer_id= {}".format(int(ed))
            mycursor.execute(sqla)
            myresult = mycursor.fetchall()
            for names in myresult:
                dty=names[0]
            dt=dty+ relativedelta(months=1)
            vb=datetime.datetime.now().utcnow()
            if vb>dt:
                conn = sqlite3.connect('vision.db')
                conn.execute("DELETE from COMPANY where ID = {};".format(idd))
                conn.commit()
        
                try:
                    guild=await bot.fetch_guild(875527884830306314)
                    mem=await guild.fetch_member(int(idd))
                    role = discord.utils.get(guild.roles, name='Koin Plug Pro')
                    await mem.remove_roles(role)
                except:
                    a=1
                try:
                    guild = await bot.fetch_guild(871729338733690910)
                    mem=await guild.fetch_member(int(idd))
                    role = discord.utils.get(guild.roles, name='Koin Plug Pro')
                    await mem.remove_roles(role)
                except:
                    a=1
                user=await bot.fetch_user(int(idd))
                await user.send("You have been removed from the channel. Please subscribe again at https://koinplug.com/")

                await user.send("Te han eliminado del canal. Vuelva a suscribirse en https://koinplug.com/")

            elif dt==vb:
                    user=await bot.fetch_user(int(idd))
                    await user.send("Your subscription will expire soon. To remain in the channel, please subscribe again at https://koinplug.com")
            
                    await bot.send_message(int(idd),"Tu suscripción caducará pronto. Para permanecer en el canal, suscríbase nuevamente en https://koinplug.com")
        except:
            print("error")
test.start()
bot.run('OTA4MzkzMTkxMzI4MzI5NzQ4.YY1FFQ.Q2ULcd7dU283HVcP6CLKanFLeHA')