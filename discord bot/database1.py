import sqlite3
conn = sqlite3.connect('lead.db')
conn.execute('''CREATE TABLE COMPANY
         (
         id   text    NOT NULL,
         username   text    NOT NULL,
         email   TEXT    NOT NULL,
         captcha   TEXT    NOT NULL
         );''')
conn.close()

