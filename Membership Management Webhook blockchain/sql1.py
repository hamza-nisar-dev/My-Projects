import sqlite3
conn = sqlite3.connect('sql1.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
          ID INT PRIMARY KEY      NOT NULL, 
          exp        TEXT    NOT NULL
);''')
print ("Table created successfully")