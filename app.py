from Data_mongo.models import Question
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

#add_test_question()

if __name__ == '__main__':
    app.run()
