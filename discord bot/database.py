import sqlite3
conn = sqlite3.connect('white.db')
conn.execute('''CREATE TABLE COMPANY
         (
         id   text    NOT NULL,
         name   text    NOT NULL,
         wallet   TEXT    NOT NULL
         );''')
conn.close()


