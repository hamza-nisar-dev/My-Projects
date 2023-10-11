import sqlite3
conn = sqlite3.connect('email1.db')
conn.execute('''CREATE TABLE COMPANY
         (
         name   NOT NULL,
         amount   FLOAT NOT NULL,
         date   TEXT NOT NULL,
         service  TEXT NOT NULL
         );''')
conn.close()

