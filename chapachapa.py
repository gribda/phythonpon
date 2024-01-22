import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE users (name TEXT)")

connection.close()