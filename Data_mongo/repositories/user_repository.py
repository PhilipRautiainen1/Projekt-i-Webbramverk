from Data_mongo.models import User


def get_user(username):
    return User.find(username=username).first_or_none()


def add_user(email, username, hashed_password):
    user = User({
            'email': email,
            'username': username,
            'password': hashed_password,
            'score': 0,
            'friends': []
        })
    user.save()


def get_all_users():
    return User.all()
