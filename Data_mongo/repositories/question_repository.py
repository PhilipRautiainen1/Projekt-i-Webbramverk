from Data_mongo.models import Question


def add_question(question):
    category, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3 = question
    question = Question({
        'category': category,
        'diff': None,
        'question': question,
        'answers': [
            {'answer': right_answer,
             'correctBool': True},
            {'answer': wrong_answer1,
             'correctBool': False},
            {'answer': wrong_answer2,
             'correctBool': False},
            {'answer': wrong_answer3,
             'correctBool': False}]
    })
    question.save()
