import sqlite3

conn = sqlite3.connect('usorders.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ID     TEXT    NOT NULL,
         username          TEXT    NOT NULL,
         name          TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         oid     TEXT    NOT NULL,
         address     TEXT    NOT NULL,
         date     TEXT    NOT NULL,
         pnam     TEXT    NOT NULL,
         quantity     TEXT    NOT NULL,
         productID    TEXT    NOT NULL,
         status     TEXT    NOT NULL         
);''')
print ("Table created successfully") 
conn.close()