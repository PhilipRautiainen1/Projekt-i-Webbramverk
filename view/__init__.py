from flask import Flask, render_template, redirect, url_for

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


@app.route('/highscore')
def highscore():
    return render_template("highscore.html")


@app.route('/game')
def game():
    #questions_list = get_questions()
    return render_template('game.html')#, questions_list=questions_list)


@app.route('/sign_in/')
def sign_in():
    return render_template('login.html')


@app.route('/sign_in/', methods=["POST"])
def sign_in_post():
    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/signup/', methods=["POST"])
def signup_post():
    return redirect(url_for('sign_in'))
