import sqlite3
conn = sqlite3.connect('mystock.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT    NOT NULL,
         Stock        TEXT    NOT NULL,
         status          TEXT    NOT NULL,
         price_bought      TEXT    NOT NULL,
         amount           TEXT    NOT NULL
);''')
print ("Table created successfully")



conn.execute('''CREATE TABLE wallet
         (ID INT    NOT NULL,
          wallet           TEXT    NOT NULL,
          quantity           TEXT    NOT NULL
);''')
print ("Table created successfully")

conn.close()