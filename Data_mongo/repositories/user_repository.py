from Data_mongo.models import User
from bson.objectid import ObjectId


def get_user(username):
    return User.find(username=username).first_or_none()


def get_user_by_id(_id):
    return User.find(_id=_id).first_or_none()


def add_user(email, username, hashed_password):
    user = User({
            'email': email,
            'username': username,
            'password': hashed_password,
            'score': 0,
            'friends': []
        })
    user.save()


def add_friend(user, friend):
    friends = user.friends
    friends.append(friend._id)
    user.collection.update({"_id": user._id}, {"$set": {'friends': friends}}, upsert=True)


def remove_friend(user, friend_id):
    user.collection.update_one({'_id': user._id}, {'$pull': {'friends': ObjectId(friend_id)}})


def get_all_users():
    return User.all()


def save_score(score, user):
    new_score = score + user.score
    user.collection.update({"_id": user._id}, {"$set": {'score': new_score}}, upsert=True)


def delete_user(user):
    user.collection.delete_one({"_id": user._id})