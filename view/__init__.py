from flask import Flask, render_template, redirect, url_for, request, flash
from flask import session as flask_session
import bcrypt
from functools import wraps
from controllers import question_controller as qc
from Data_mongo.models import User, Question


app = Flask(__name__)
app.secret_key = "supersecret"


def login_required(default_page):
    def decorator(route):
        @wraps(route)
        def wrapper(*args, **kwargs):
            if 'username' in flask_session:
                return route(*args, **kwargs)
            flash('Du måste vara inloggad för att visa denna sidan')
            return redirect(url_for(default_page))
        return wrapper
    return decorator


def sign_in_status():
    return 'username' in flask_session


@app.before_request
def check():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logged-in')
def logged_in():
    return render_template('profile.html')


@app.route('/my-page')
#@login_required
def my_page():
    return render_template('my_page.html')


@app.route('/add-question', methods=['GET', 'POST'])
#@login_required('index')
def add_question():
    # POST: Add a question to the database
    if request.method == 'POST':
        category = request.form['category']
        question = request.form['question']
        right_answer = request.form['right_answer']
        wrong_answer1 = request.form['wrong_answer1']
        wrong_answer2 = request.form['wrong_answer2']
        wrong_answer3 = request.form['wrong_answer3']

        question = category, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3
        qc.add_question(question)
        flash('Frågan har blivit tillagd!')

    # GET: Serve Add-question page
    return render_template('add_question.html')


@app.route('/highscore')
def highscore():
    users = get_username_score()

    return render_template("highscore.html", users=users)


def get_username_score():
    users = User.all()
    sorted_users = sorted(users, key=lambda u: u.score)

        # .sort().limit(10)
    return sorted_users


@app.route('/game')
# @login_required
def game():
    #questions_list = get_questions()
    return render_template('game.html')#, questions_list=questions_list)


@app.route('/sign_in')
def sign_in():
    return render_template('login.html')


@app.route('/sign_in', methods=["POST"])
def sign_in_post():
    username = request.form['username']
    password = request.form['password']
    user = User.find(username=username).first_or_none()

    if user is not None:
        if bcrypt.checkpw(str.encode(password), user.password):
            return redirect(url_for('logged_in'))
    return redirect(url_for('error'))


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=["POST"])
def signup_post():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password1']
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(str.encode(password), salt)
    add_user(email, username, hashed_password)
    return redirect(url_for('sign_in'))


def add_user(email, username, hashed_password):
    user = User(
        {
            'email': email,
            'username': username,
            'password': hashed_password,
            'score': 0,
            'friends': []
        }
    )
    user.save()


@app.route('/error')
def error():
    return render_template('error.html')
