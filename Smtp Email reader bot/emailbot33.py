
import telegram.ext
import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
def start(update, context):
    a=str(update.effective_user.id)
    if a=="537601358" or a=="1243148434" or a=="680507745" or a=="537601358":
      context.bot.send_message(chat_id=update.effective_user.id,text="Send /info to get payments details\n\nSend /reset to reset database")

def reset(update, context):
    a=str(update.effective_user.id)
    if a=="537601358" or a=="1243148434" or a=="680507745" or a=="537601358":
        conn = sqlite3.connect('email3.db') 
        cursor = conn.cursor()  
        cursor.execute("DELETE FROM COMPANY") 
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id=update.effective_user.id,text="Database reset sucessfully")
def info(update, context):
    a=str(update.effective_user.id)
    if a=="537601358" or a=="1243148434" or a=="680507745" or a=="537601358":
        conn = sqlite3.connect('email3.db') 
        cursor = conn.cursor()  
        cursor.execute("SELECT sum(amount) FROM COMPANY") 
        jobs = cursor.fetchall()
        for names in jobs:
            total=names[0]
        cursor.execute("SELECT sum(amount) FROM COMPANY where service='Venmo'") 
        jobs = cursor.fetchall()
        for names in jobs:
            venom=names[0]
        cursor.execute("SELECT sum(amount) FROM COMPANY where service='CashApp'") 
        jobs = cursor.fetchall()
        for names in jobs:
            cashapp=names[0]
        cursor.execute("SELECT sum(amount) FROM COMPANY where service='Zelle'") 
        jobs = cursor.fetchall()
        for names in jobs:
            zilla=names[0]
        text="𝐓𝐨𝐭𝐚𝐥 𝐂𝐚𝐬𝐡𝐚𝐩𝐩 : ${}\n\n𝐓𝐨𝐭𝐚𝐥 𝐕𝐞𝐧𝐦𝐨 : ${}\n\n𝐓𝐨𝐭𝐚𝐥 𝐙𝐞𝐥𝐥𝐞 : ${}\n\n𝐓𝐨𝐭𝐚𝐥 𝐨𝐟 𝐚𝐥𝐥 𝟑 : ${}".format(cashapp,venom,zilla,total)
        print(text)
        context.bot.send_message(chat_id=update.effective_user.id,text=text)
def main():
    updater = Updater("5333591790:AAFZmdPM37vDkt3bILk_6WG8MaXYa8Pnv1g", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("reset", reset))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
