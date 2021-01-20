import bcrypt
from Data_mongo.models import Question, User
from Data_mongo.repositories.question_repository import get_questions, question_api_load
from view import app


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

# add_test_question()


def test_user():
    user = User ({
        'email': 'test',
        'username': 'test',
        'password': 'test',
        'score': 123,
        'friends': []
    })
    user.save()


# test_user()
question_api_load()
get_questions(5)
if __name__ == '__main__':
   app.run(debug=True)
