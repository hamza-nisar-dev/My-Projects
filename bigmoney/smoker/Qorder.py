import sqlite3 

conn = sqlite3.connect('Qorder.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ID          TEXT    NOT NULL,
         username          TEXT    NOT NULL,
         price        TEXT    NOT NULL,
         oid         TEXT    NOT NULL,
         type         TEXT    NOT NULL,
         date         TEXT    NOT NULL,
         pnam   TEXT    NOT NULL,
         productID   TEXT    NOT NULL
);''')
print ("Table created successfully")