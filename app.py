import bcrypt

from Data_mongo.models import Question
from Data_mysql.db import engine, Base
from view import app, add_user
from Data_mysql.models.users import User
from Data_mysql.models.friends import Friend

def add_test_question():
    answers = [{
        "answer": "195",
        "correctBool": True
    },
        {
            "answer": "190",
            "correctBool": False
        },
        {
            "answer": "200",
            "correctBool": False
        },
        {
            "answer": "185",
            "correctBool": False
        }
    ]

    question = Question({
        "question": "Hur många länder finns det i världen?",
        "category": "Geografi",
        "diff": 1,
        "answers": answers
    })

    question.save()

def sql():
    Base.metadata.create_all(engine)
    email='simon@email.com'
    username='simon'
    password='s3cr37'
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(str.encode(password), salt)
    add_user(email, username, hashed_password)

#add_test_question()

if __name__ == '__main__':
   app.run(debug=True)
