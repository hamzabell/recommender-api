import sqlite3 as sql


connection = sql.connect('database.db')



with open('schema.sql') as f:
    connection.executescript(f.read())


connection.commit()
connection.close()

