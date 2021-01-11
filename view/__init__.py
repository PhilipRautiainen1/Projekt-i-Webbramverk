from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logged-in')
def logged_in():
    return render_template('base_user.html')


@app.route('/my-page')
def my_page():
    return render_template('my_page.html')


@app.route('/add-question')
def add_question():
    return render_template('add_question.html')


@app.route('/not-logged-in')
def not_logged_in():
    return render_template('not_logged_in.html')


@app.route('/game')
def game():
    #questions_list = get_questions()
    return render_template('game.html')#, questions_list=questions_list)
