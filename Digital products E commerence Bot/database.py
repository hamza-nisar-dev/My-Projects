import sqlite3 

conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE products
         (
         ID          TEXT    NOT NULL,
         name        TEXT    NOT NULL,
         price        TEXT    NOT NULL,
         catagory     TEXT    NOT NULL,
         description        TEXT    NOT NULL                
);''')
print ("Table created successfully")

conn.execute('''CREATE TABLE catagories
         (

        name       TEXT    NOT NULL                
);''')
print ("Table created successfully")


