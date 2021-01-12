from Data_mongo.models import Question
from Data_mysql.db import engine, Base
from view import app
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

#add_test_question()
#Base.metadata.create_all(engine)

if __name__ == '__main__':
   app.run(debug=True)
