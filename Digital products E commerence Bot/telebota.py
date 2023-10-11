import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler

import imaplib
import email

def email_check(nm):
    try:
        imap_server = 'imap.gmail.com'
        username = 'Markfelix1495@gmail.com'
        password = 'jbwhrtxxqovnmzrp'

        # Connect to the Gmail IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)

        # Login to the Gmail account
        mail.login(username, password)

        # Select the mailbox you want to search emails in (e.g., 'INBOX')
        mailbox = 'INBOX'
        mail.select(mailbox)

        # Search for emails containing specific keywords in the body
        search_criteria = '(BODY "{}")'.format(nm)
        status, data = mail.search(None, search_criteria)

        # Get the list of matching email IDs
        email_ids = data[0].split()
        if email_ids:
            # Fetch the most recent email from the search results
            latest_email_id = email_ids[-1]
            status, data = mail.fetch(latest_email_id, '(RFC822)')
            raw_email = data[0][1]

            # Parse the raw email
            email_message = email.message_from_bytes(raw_email)

            # Print the email body
            if email_message.is_multipart():
                for part in email_message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        a=part.get_payload(decode=True).decode('utf-8')
            else:
                a=email_message.get_payload(decode=True).decode('utf-8')

        # Close the connection
        mail.logout()
        return a
    except:
        return None

def start(update, context):
     context.bot.send_message(chat_id=update.effective_user.id,text="Please Send your phone number in order to get the details.")
def get(update, context):
     context.bot.send_message(chat_id=update.effective_user.id,text="Please Send your phone number in order to get the details.")
def menu(update, context):
    msg=update.message.text
    try:
        msg=int(msg)
        b=email_check(msg)
        if b==None:
         context.bot.send_message(chat_id=update.effective_user.id,text="Nothing found on this number.")
        else:
            context.bot.send_message(chat_id=update.effective_user.id,text=b)

    except:
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid phone number! please send correct format number like 3366242675")



def main():  
  updater = Updater("6396347702:AAFgzoG6R31C7to6utF3bspt6dqFQ0W4pg0", use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("get", get))
  dp.add_handler(MessageHandler(Filters.text, menu))
  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
    main()
    