import json
import random
from flask import Flask, render_template, redirect, url_for, request, flash
from flask import session as flask_session
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
@login_required('index')
def game():
    if request.method == 'GET':
        if 'question_list' in flask_session:
            question_list = flask_session['question_list']
            current_question = flask_session['current_question']
            flask_session['current_question'] += 1

            if flask_session['current_question'] > len(question_list)-1:
                flask_session['last_turn'] = True

            last_turn = flask_session['last_turn']
            question = question_list[current_question]['question']
            answers = question_list[current_question]['answers']

            num = [0, 1, 2, 3]
            random.shuffle(num)
            a1 = answers[num[0]]
            a2 = answers[num[1]]
            a3 = answers[num[2]]
            a4 = answers[num[3]]
            flask_session['answer_order'] = [a1, a2, a3, a4]
            return render_template('game.html', question=question, a1=a1, a2=a2, a3=a3, a4=a4, last_turn=last_turn)
        return redirect(url_for('setup'))

    if request.method == 'POST':
        a1, a2, a3, a4 = flask_session.pop('answer_order', None)
        for i, a in enumerate([a1, a2, a3, a4]):
            no = request.values['user_answer'][-1]
            response = False
            if a['correctBool']:
                correct = i + 1
                if i + 1 == int(no):
                    flask_session['score'] += 50
                    response = True
                    break

        return app.response_class(response=json.dumps({'response': response, 'correct': correct}), status=200,
                                  mimetype='application/json')


@app.route('/start_game')
@login_required('index')
def start_game():
    category = flask_session['category']
    no = flask_session['no']
    flask_session['question_list'] = qc.get_questions(category, no)
    flask_session['current_question'] = 0
    flask_session['score'] = 0
    flask_session['last_turn'] = False
    return redirect(url_for('game'))


@app.route('/setup', methods=['GET', 'POST'])
@login_required('index')
def setup():
    if request.method == 'POST':
        category = request.form['category']
        no = int(request.form['number'])
        flask_session['category'] = category
        flask_session['no'] = no
        return redirect(url_for('start_game'))
    return render_template('setup.html')


@app.route('/end_game', methods=['GET'])
@login_required('index')
def end_game():
    score = flask_session['score']
    correct = int(score/50)
    nr_quest = flask_session['no']

    username = flask_session['username']
    user = uc.get_user(username)
    uc.save_score(score, user)
    [flask_session.pop(key) for key in ('category', 'no', 'question_list', 'current_question', 'score', 'last_turn')]

    return app.response_class(response=json.dumps({'score': score, 'correct': correct, 'nr_quest': nr_quest}),
                              status=200, mimetype='application/json')


@app.route('/multiplayer')
@login_required('index')
def multiplayer():
    flash('Kommer snart! Multiplayer har ännu inte lanserats.')
    return redirect(url_for('index'))


@app.route('/sign_in')
def sign_in():
    return render_template('login.html')


@app.route('/sign_in', methods=["POST"])
def sign_in_post():
    username = request.form['username']
    password = request.form['password']
    if uc.login_check(username, password):
        flask_session.permanent = True
        return redirect(url_for('index'))
    login_error = 'Felaktigt användarnamn eller lösenord'
    return render_template('login.html', login_error=login_error)


@app.route('/profile', methods=['GET', 'POST'])
@login_required('index')
def profile():
    if request.method == 'POST':
        friend_name = request.form['friend_name']
        f_user = uc.get_user(friend_name)

        if f_user != None:
            username = flask_session['username']
            user = uc.get_user(username)
            uc.add_friend(user, f_user)
            return redirect(url_for('profile'))
        else:
            return redirect(url_for('profile'))
    else:
        username = flask_session['username']
        user = uc.get_user(username)
        friends = user.friends
        friend_list = []
        for id in friends:
            friend_list.append(uc.get_user_by_id(id))
        return render_template('profile.html', user=user, friends=friend_list)


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


@app.errorhandler(404)
def handler404(e):
    return render_template('error.html', e=e)


@app.errorhandler(500)
def handler500(e):
    return render_template('error.html', e=e)


@app.errorhandler(502)
def handler502(e):
    return render_template('error.html', e=e)


@app.route('/signout')
def signout():
    flask_session.clear()
    return redirect(url_for('index'))
