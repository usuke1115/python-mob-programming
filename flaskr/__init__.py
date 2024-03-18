from flask import Flask
app = Flask(__name__)
import flaskr.main

if __name__ == "__main__":
    app.run()