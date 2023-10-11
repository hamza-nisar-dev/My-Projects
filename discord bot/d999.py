
from discord import member, user
from discord.ext import commands
import datetime
import mysql.connector
from mysql.connector import Error
import discord
import sqlite3
from datetime import datetime as dn
from dateutil.relativedelta import relativedelta
from discord.ext.commands import context
from discord.ext import tasks
from discord.utils import get
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('/'),intents=discord.Intents.all())

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label='English', style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Please provide your email used to subscribe at https://koinplug.com', ephemeral=True)
        mm= await bot.wait_for('message')
        user=mm.author.id
        connection = sqlite3.connect("lang.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT id FROM COMPANY where id= {}".format(user)) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            conn = sqlite3.connect('lang.db')
            conn.execute("INSERT INTO COMPANY (ID,lang) \
                VALUES ({}, '{}')".format(user,"en"))
            conn.commit()
            conn.close()
        else:
            conn= sqlite3.connect("lang.db")
            conn.execute("UPDATE COMPANY set lang = 'en' where ID = {}".format(user))
            conn.commit()
            conn.close()
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
                    m = await mm.reply("click on below links to join:\n\nhttps://discord.gg/UR8TKtHcyc")
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
            await mm.reply("Nothing found on this email")
        self.value = True
        self.stop()

    @discord.ui.button(label='Spanish', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Proporciotx.usene el correo electrónico que utilizó para suscribirse en https://koinplug.com', ephemeral=True)
        mm= await bot.wait_for('message')
        user=mm.author.id
        connection = sqlite3.connect("lang.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT id FROM COMPANY where id= {}".format(user)) 
        jobs = cursor.fetchall()
        if len(jobs) ==0:
            conn = sqlite3.connect('lang.db')
            conn.execute("INSERT INTO COMPANY (ID,lang) \
                VALUES ({}, '{}')".format(user,"sp"))
            conn.commit()
            conn.close()
        else:
            conn= sqlite3.connect("lang.db")
            conn.execute("UPDATE COMPANY set lang = 'sp' where ID = {}".format(user))
            conn.commit()
            conn.close()
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
                    m = await mm.reply("Haga clic a continuación para unirse\n\nhttps://discord.gg/pR5CzxWEWM")
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
            await mm.reply("No se encontró nada en este correo electrónico")
        self.value = False
        self.stop()


bot = Bot()
@bot.event
async def on_member_join(member):
    try:
        user=member.id
        connection = sqlite3.connect("vision.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT id FROM COMPANY where id= '{}'".format(user)) 
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            role = get(member.guild.roles, name="paid_member")
            print(role)
            await member.add_roles(role)
    except:
        pass

@tasks.loop(seconds = 85400)
async def test():
    connection = sqlite3.connect("vision.db")  
    cursor = connection.execute("SELECT id,customer_id FROM COMPANY")
    for names in cursor:        
        try:
            idd=names[0]
            ed=names[1]
            connection = sqlite3.connect("lang.db")  
            cursor = connection.execute("SELECT lang from COMPANY where ID= '{}'".format(idd))
            for names in cursor:
                la=names[0]
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
                    role = discord.utils.get(guild.roles, name='paid_member')
                    await mem.remove_roles(role)
                except:
                    a=1
                try:
                    guild = await bot.fetch_guild(871729338733690910)
                    mem=await guild.fetch_member(int(idd))
                    role = discord.utils.get(guild.roles, name='paid_member')
                    await mem.remove_roles(role)
                except:
                    a=1
                if la=="en":
                    user=await bot.fetch_user(int(idd))
                    await user.send("You have been removed from the channel. Please subscribe again at https://koinplug.com/")
                else:
                    user=await bot.fetch_user(int(idd))
                    await user.send("Te han eliminado del canal. Vuelva a suscribirse en https://koinplug.com/")

            elif dt==vb:
                if la=="en":
                    user=await bot.fetch_user(int(idd))
                    await user.send("Your subscription will expire soon. To remain in the channel, please subscribe again at https://koinplug.com")
                else:
                    user=await bot.fetch_user(int(idd))
                    await bot.send_message(int(idd),"Tu suscripción caducará pronto. Para permanecer en el canal, suscríbase nuevamente en https://koinplug.com")
        except:
            print("error")

@bot.command()
async def start(ctx: commands.Context):
    author = ctx.message.author
    print(author)
    view = Confirm()
    await ctx.send('Select Your Language.', view=view)
    await view.wait()
    if view.value is None:
        await ctx.send('Time out! please send /start again')

    
   

test.start()
bot.run('OTA4MzkzMTkxMzI4MzI5NzQ4.YY1FFQ.Q2ULcd7dU283HVcP6CLKanFLeHA')