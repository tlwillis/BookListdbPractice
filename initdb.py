import sqlite3

connection = sqlite3.connect('database.db')
print('Opened successfully')

connection.execute('CREATE TABLE books (name TEXT, author TEXT, year_published INTEGER, pages INTEGER)')
print('Table created')

connection.close()