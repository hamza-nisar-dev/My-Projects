import sqlite3
conn = sqlite3.connect('mystock.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE wallet
         (ID INT    NOT NULL,
          wallet           TEXT    NOT NULL
);''')
print ("Table created successfully")

conn.close()