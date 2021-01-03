from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logga in')
def inlogning():
    return render_template('login.html')
