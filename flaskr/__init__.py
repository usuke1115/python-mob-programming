from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.create_books_table()

if __name__ == "__main__":
    app.run()