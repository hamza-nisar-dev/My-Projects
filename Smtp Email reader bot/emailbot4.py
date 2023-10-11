import imaplib, smtplib, time, email, textwrap
import telegram.ext
import requests
from datetime import datetime
import sqlite3
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
                            text = part.get_payload(decode=True) 

                    self._messageLst.append(message)
                    sender = mail["From"].split("<")[0].rstrip() 
                    subject = mail["Subject"]
                    print(subject)
                    try:
                        if "Zelle" in str(text) or "Zelle" in str(sender):
                            date=mail["Date"]
                            a=subject.split(" sent you ")
                            name_sender=a[0]
                            name_sender=name_sender.replace("Fwd: ","")
                            amount=a[1]
                            pov='Zelle'
                            am=amount.replace("$","")
                            am=float(am)
                            dt=parser.parse(date) 
                            dtt=str(dt) 
                            dtt=dtt.split(" ")
                            b=dtt[0]
                            a=dtt[1]
                            a=a.split("+")
                            a=a[0]
                            d = datetime.strptime(a, "%H:%M:%S")
                            vv=str(d).split(" ")
                            vv=vv[1]
                            fg=date.split(vv)
                            fg=fg[0]
                            d=d.strftime("%I:%M %p")
                            date=fg+" "+str(d)
                            connection = sqlite3.connect("email4.db")  
                            cursor = connection.cursor()  
                            cursor.execute("SELECT date FROM COMPANY where date= '{}'".format(date)) 
                            jobs = cursor.fetchall()
                            if len(jobs) ==0:
                                conn = sqlite3.connect('email4.db')
                                conn.execute("INSERT INTO COMPANY (name,amount,date,service) \
                                    VALUES ('{}',{},'{}','{}')".format(name_sender,am,date,pov))
                                conn.commit()
                                conn.close()
                                text="𝐒𝐞𝐧𝐝𝐞𝐫'𝐬 𝐧𝐚𝐦𝐞: {}\n\n𝐓𝐨𝐭𝐚𝐥 𝐀𝐦𝐨𝐮𝐧𝐭: {}\n\n𝐃𝐚𝐭𝐞: {}\n\n𝐒𝐞𝐫𝐯𝐢𝐜𝐞 𝐍𝐚𝐦𝐞: {}".format(name_sender,amount,date,pov)
                                print(text)  
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=680507745&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=1243148434&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=537601358&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=807516030&text={}".format(text)				
                                a=requests.get(hamza)
                 
                        elif "venmo" in str(text) or "Venmo" in str(sender):
                            date=mail["Date"]
                            a=subject.split(" paid you ")
                            name_sender=a[0]
                            name_sender=name_sender.replace("Fwd: ","")
                            amount=a[1]
                            pov='Venmo'
                            am=amount.replace("$","")
                            am=float(am)
                            dt=parser.parse(date) 
                            dtt=str(dt) 
                            dtt=dtt.split(" ")
                            b=dtt[0]
                            a=dtt[1]
                            a=a.split("+")
                            a=a[0]
                            d = datetime.strptime(a, "%H:%M:%S")
                            vv=str(d).split(" ")
                            vv=vv[1]
                            fg=date.split(vv)
                            fg=fg[0]
                            d=d.strftime("%I:%M %p")
                            date=fg+" "+str(d)
                            connection = sqlite3.connect("email4.db")  
                            cursor = connection.cursor()  
                            cursor.execute("SELECT date FROM COMPANY where date= '{}'".format(date)) 
                            jobs = cursor.fetchall()
                            if len(jobs) ==0:
                                conn = sqlite3.connect('email4.db')
                                conn.execute("INSERT INTO COMPANY (name,amount,date,service) \
                                    VALUES ('{}',{},'{}','{}')".format(name_sender,am,date,pov))
                                conn.commit()
                                conn.close()
                                text="𝐒𝐞𝐧𝐝𝐞𝐫'𝐬 𝐧𝐚𝐦𝐞: {}\n\n𝐓𝐨𝐭𝐚𝐥 𝐀𝐦𝐨𝐮𝐧𝐭: {}\n\n𝐃𝐚𝐭𝐞: {}\n\n𝐒𝐞𝐫𝐯𝐢𝐜𝐞 𝐍𝐚𝐦𝐞: {}".format(name_sender,amount,date,pov)
                                print(text)  
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=680507745&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=1243148434&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=537601358&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=807516030&text={}".format(text)				
                                a=requests.get(hamza)
                 
                        elif "Cash App" in str(text) or "Cash App" in str(sender):
                            date=mail["Date"]

                            a=subject.split(" sent you ")
                            name_sender=a[0]
                            name_sender=name_sender.replace("Fwd: ","")
                            amount=a[1]
                            if "for" in subject:
                               amount=amount.split(" for")
                               amount=amount[0]
                            pov='CashApp'
                            am=amount.replace("$","")
                            am=float(am)
                            dt=parser.parse(date) 
                            dtt=str(dt) 
                            dtt=dtt.split(" ")
                            b=dtt[0]
                            a=dtt[1]
                            a=a.split("+")
                            a=a[0]
                            d = datetime.strptime(a, "%H:%M:%S")
                            vv=str(d).split(" ")
                            vv=vv[1]
                            fg=date.split(vv)
                            fg=fg[0]
                            d=d.strftime("%I:%M %p")
                            date=fg+" "+str(d)
                            connection = sqlite3.connect("email4.db")  
                            cursor = connection.cursor()  
                            cursor.execute("SELECT date FROM COMPANY where date= '{}'".format(date)) 
                            jobs = cursor.fetchall()
                            if len(jobs) ==0:
                                conn = sqlite3.connect('email4.db')
                                conn.execute("INSERT INTO COMPANY (name,amount,date,service) \
                                    VALUES ('{}',{},'{}','{}')".format(name_sender,am,date,pov))
                                conn.commit()
                                conn.close()
                                text="𝐒𝐞𝐧𝐝𝐞𝐫'𝐬 𝐧𝐚𝐦𝐞: {}\n\n𝐓𝐨𝐭𝐚𝐥 𝐀𝐦𝐨𝐮𝐧𝐭: {}\n\n𝐃𝐚𝐭𝐞: {}\n\n𝐒𝐞𝐫𝐯𝐢𝐜𝐞 𝐍𝐚𝐦𝐞: {}".format(name_sender,amount,date,pov)
                                print(text)  
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=680507745&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=1243148434&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=537601358&text={}".format(text)				
                                a=requests.get(hamza)
                                hamza="https://api.telegram.org/bot5138631466:AAG0_CSY4-68mk-vgjf_dGGO1m1M0xrlxKI/sendMessage?chat_id=807516030&text={}".format(text)				
                                a=requests.get(hamza)
                    except:
                        pass

                 
            

            def start(self):
                while True:
                    self.checkMail()
                    time.sleep(self._restTime)

        notifier = Email_SMS_Notifier("andybotmen@gmail.com", "bxemclmemthghzfm",1)
        notifier.start()

                
    except:
        print("error running again")
        