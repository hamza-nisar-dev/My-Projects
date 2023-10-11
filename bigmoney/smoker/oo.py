import sqlite3 

conn = sqlite3.connect('oo.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ID          TEXT    NOT NULL,
         pid TEXT    NOT NULL,
         amount TEXT    NOT NULL,
         pname TEXT    NOT NULL,
         type TEXT    NOT NULL
);''')
print ("Table created successfully")
