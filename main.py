from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! Hello, world! Het is me gelukt!'