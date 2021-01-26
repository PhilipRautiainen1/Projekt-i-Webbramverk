from flask import Flask, render_template, redirect, url_for, request
import json
from flask import session as flask_session
from Data_mongo.repositories.question_repository import get_questions
from controllers import question_controller as qc
from controllers import user_controller as uc
from view.tools import login_required
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "supersecret"
app.permanent_session_lifetime = timedelta(minutes=10)


@app.before_request
def check():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/')
def index():
    if 'username' in flask_session:
        return render_template('index_user.html')
    return render_template('index.html')


@app.route('/logged-in')
def logged_in():
    return render_template('profile.html')


@app.route('/my-page')
@login_required('index')
def my_page():
    return render_template('my_page.html')


@app.route('/add-question', methods=['GET', 'POST'])
@login_required('index')
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
        qc.check_and_add_q(question)
        return render_template('add_question.html')

    # GET: Serve Add-question page
    return render_template('add_question.html')


@app.route('/highscore')
def highscore():
    users = uc.get_users_highscore()
    if 'username' in flask_session:
        return render_template("highscore_user.html", users=users)
    return render_template("highscore.html", users=users)


@app.route('/game', methods=['GET', 'POST'])
# @login_required('index')
def game():
    no = 5
    questions_list = get_questions(no)

    question = questions_list[0].question

    answers = questions_list[0].answers
    a1 = answers[0]
    a2 = answers[1]
    a3 = answers[2]
    a4 = answers[3]
    if request.method == 'POST':
        for i, a in enumerate([a1, a2, a3, a4]):
            no = request.values['user_answer'][-1]
            response = False
            if a['correctBool']:
                if i+1 == int(no):
                    response=True
                    break

        return app.response_class(response=json.dumps({'response': response}), status=200, mimetype='application/json')
    return render_template('game.html', question=question, a1=a1, a2=a2, a3=a3, a4=a4)


@app.route('/sign_in')
def sign_in():
    return render_template('login.html')


@app.route('/sign_in', methods=["POST"])
def sign_in_post():
    username = request.form['username']
    password = request.form['password']
    if uc.login_check(username, password):
        flask_session.permanent = True
        return redirect(url_for('profile'))
    login_error = 'Felaktigt användarnamn eller lösenord'
    return render_template('login.html', login_error=login_error)


@app.route('/profile')
def profile():
    username = flask_session['username']
    user = uc.get_user(username)
    friends = user.friends
    return render_template('profile.html', user=user, friends=friends)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=["POST"])
def signup_post():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password1']
    if uc.signup_user(email, username, password):
        return redirect(url_for('sign_in'))
    username_error = 'Det finns redan en användare med det här användarnamnet'
    return render_template('signup.html', username_error=username_error)


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/signout')
def signout():
    flask_session.clear()
    return redirect(url_for('index'))

@app.route('/setup')
def setup():
    return render_template('setup.html')
