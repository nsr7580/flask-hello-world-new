from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! from Flask'

@app.route('/about')
def about():
    return 'About this flask app'