import sqlite3
conn = sqlite3.connect('lang.db')
conn.execute('''CREATE TABLE COMPANY
         (ID TEXT    NOT NULL,
          lang        TEXT    NOT NULL
         );''')
conn.close()
