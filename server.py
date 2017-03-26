from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/new-book', methods = ['POST'])
def newBook():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	name = request.form['name']
	author = request.form['author']
	yearPublished = request.form['yearPublished']
	pages = request.form['pages']

	try:
		cursor.execute('INSERT INTO books(name, author, year_published, pages) VALUES (?,?,?,?)', (name, author, yearPublished, pages))
		connection.commit()
		message = 'Success'
	except Exception as err:
		print(err)
		connection.rollback()
		message = 'Error'
	finally:
		connection.close()
		return message

@app.route('/books')
def getBooks():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM books')
	petslist = cursor.fetchall()

	connection.close()

	return jsonify(petslist)


app.run(debug = True)