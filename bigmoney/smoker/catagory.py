import sqlite3 

conn = sqlite3.connect('cata.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (cat     TEXT    NOT NULL,
          type    TEXT    NOT NULL
);''')
print ("Table created successfully")

conn.close()