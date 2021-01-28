from Data_mongo.models import Question, User


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


def add_test_user():
    user = User({
        'email': 'test',
        'username': 'test',
        'password': 'test',
        'score': 123,
        'friends': []
    })
    user.save()
