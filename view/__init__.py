from flask import Flask, render_template, redirect, url_for, request, flash
from flask import session as flask_session
from controllers import question_controller as qc
from controllers import user_controller as uc
from Data_mongo.models import User, Question
from view.tools import login_required
from difflib import SequenceMatcher

app = Flask(__name__)
app.secret_key = "supersecret"


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

        wrong_answers = [wrong_answer1, wrong_answer2, wrong_answer3]

    questions = Question.all()

    def check_q(question):
        for q in questions:
            seq = SequenceMatcher(None, question, q)
            s = seq.ratio()
            if s < 0.85:
                if all(a != right_answer for a in wrong_answers):
                    if len(wrong_answers) == len(set(wrong_answers)):
                        question = category, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3
                        qc.add_question(question)
                        flash('Frågan har blivit tillagd!')
                        return render_template('add_question.html')
                    else:
                        flash('Ett felaktigt svar kan inte vara samma som ett annat!')
                        return render_template('add_question.html')
                else:
                    flash('Ett rätt svar kan inte vara ett som är fel!')
                    return render_template('add_question.html')
            else:
                flash('Din fråga är för lik en som redan existerar!')
                return render_template('add_question.html')




       # else:
        #     flash('Frågan finns redan!')
    # return render_template('add_question.html')
    # GET: Serve Add-question page

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
# @login_required('index')
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
    if uc.login_check(username, password):
        return redirect(url_for('profile'))
    login_error = 'Felaktigt användarnamn eller lösenord'
    return render_template('login.html', login_error=login_error)


@app.route('/profile')
def profile():
    username = flask_session['username']
    user = uc.get_user(username)
    return render_template('profile.html', user=user)


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
