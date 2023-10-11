import sqlite3
from unicodedata import name
connection = sqlite3.connect("code.db")  
cursor = connection.execute("SELECT id,code FROM COMPANY")
for names in cursor:
    print(names)