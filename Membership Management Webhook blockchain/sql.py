import sqlite3
conn = sqlite3.connect('sql.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
          ID INT PRIMARY KEY      NOT NULL, 
          Trx       TEXT    NOT NULL,
          tref       TEXT    NOT NULL,
          balance       TEXT    NOT NULL,
          refby       TEXT    NOT NULL,
          amount       TEXT    NOT NULL,
          exp        TEXT    NOT NULL
);''')
print ("Table created successfully")