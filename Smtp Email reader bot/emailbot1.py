import imaplib, smtplib, time, email, textwrap
import telegram.ext
import requests
from datetime import datetime
import sqlite3
import base64
from dateutil import parser
while(True):
    try:
        class Email_SMS_Notifier():
            """ Notifies by SMS of important Gmail emails """
            def __init__(self, username, password, restTime):
                self._connection = imaplib.IMAP4_SSL("imap.gmail.com", "993") # new connection
                self._connection.login(username, password) # login with username and password
                self._messageLst = []
                self._restTime = restTime
                self._username = username
                self._password = password

            def checkMail(self):
                """ Checks the mailbox for new important emails """ 
                self._connection.select("INBOX", readonly = True)
                messages = self._connection.search(None, 'UNSEEN')[1][0].split() 
            
                messages=messages[-1:]
                for message in messages:
                 if message not in self._messageLst: 
                    _ , data = self._connection.fetch(message, '(RFC822)')
                    mail = email.message_from_string(data[0][1].decode('utf-8')) 
                    text = ""
                    for part in mail.walk():
                        if part.get_content_type() == "text/plain":
                            text = part.get_payload() 
                            

                    self._messageLst.append(message)
                    sender = mail["From"].split("<")[0].rstrip() 
                    subject = mail["Subject"]
                    print(subject)
                    print(sender)
                    
                    print(text)
                        
                 
            

            def start(self):
                while True:
                    self.checkMail()
                    time.sleep(self._restTime)

        notifier = Email_SMS_Notifier("ticketping2022@gmail.com", "encdenfqnfzvbphz",1)
        notifier.start()

                
    except:
        print("error running again")
        