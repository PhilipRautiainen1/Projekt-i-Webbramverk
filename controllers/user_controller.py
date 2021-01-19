import bcrypt
from flask import session as flask_session
from Data_mongo.repositories import user_repository as ur


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




