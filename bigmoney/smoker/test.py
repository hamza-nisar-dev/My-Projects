import sqlite3
conn = sqlite3.connect('shop.db')
cursor = conn.execute("SELECT productID from COMPANY")
jobs = cursor.fetchall()
print(jobs)