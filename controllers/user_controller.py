import bcrypt
from flask import session as flask_session
from Data_mongo.repositories import user_repository as ur


def get_user(username):
    return ur.get_user(username)


def login_check(username, password):
    user = ur.get_user(username)
    if user is not None:
        if bcrypt.checkpw(str.encode(password), user.password):
            flask_session['username'] = user.username
            return True


def signup_user(email, username, password):
    user = ur.get_user(username)
    if user is None:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str.encode(password), salt)
        ur.add_user(email, username, hashed_password)
        return True


def get_users_highscore():
    users = ur.get_all_users()
    sorted_users = sorted(users, key=lambda u: u.score, reverse=True)
    limited_users = sorted_users[:10]
    return limited_users




