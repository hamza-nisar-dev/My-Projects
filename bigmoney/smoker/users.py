import sqlite3 

conn = sqlite3.connect('users.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL

);''')
print ("Table created successfully")

conn.close()