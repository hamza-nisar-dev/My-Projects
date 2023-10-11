import sqlite3 



a=["Crypto accounts","GUIDES","PayPal accounts", "Cookie & user agent","Physical Cloned Visa Cards", "Software"] 
for names in a:
    connection = sqlite3.connect("database.db")  
    cursor = connection.cursor() 
    cursor.execute("INSERT INTO catagories (name) \
    VALUES ('{}')".format(names))
    connection.commit()