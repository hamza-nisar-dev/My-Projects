import sqlite3 

conn = sqlite3.connect('cart.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID     TEXT    NOT NULL,
         productID          TEXT    NOT NULL,
         Price           TEXT    NOT NULL,
         name           TEXT    NOT NULL,
         quantity         TEXT    NOT NULL

);''')
print ("Table created successfully")

conn.close()