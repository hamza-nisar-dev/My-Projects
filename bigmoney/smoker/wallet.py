import sqlite3 

conn = sqlite3.connect('wallet.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         balance         TEXT    NOT NULL,
         code          TEXT    NOT NULL,
         link           TEXT    NOT NULL,
         name           TEXT    NOT NULL,
         amount           TEXT    NOT NULL

);''')
print ("Table created successfully")

conn.close()