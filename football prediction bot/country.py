import sqlite3
conn = sqlite3.connect('selection.db')
conn.execute('''CREATE TABLE COMPANY
         (
          ID   NOT NULL,
          continent NOT NULL,
          Country NOT NULL,
          exp NOT NULL
         );''')
conn.close()