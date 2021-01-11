from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/highscore')
def highscore():
    return render_template("highscore.html")

@app.route('/game')
def game():
    #questions_list = get_questions()
    return render_template('game.html')#, questions_list=questions_list)

