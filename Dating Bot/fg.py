import sqlite3
import sqlite3
conn = sqlite3.connect('verify.db')
conn.execute('''CREATE TABLE COMPANY
         (
         id   text    NOT NULL,
         verify_by   text    NOT NULL
         );''')
conn.close()