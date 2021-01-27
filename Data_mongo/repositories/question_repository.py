import random
from Data_mongo.models import Question
from view.tools import unescape_dict
import json
import requests
import html


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


def add_questions():
    url = 'https://opentdb.com/api.php?amount=50&type=multiple'
    data = requests.get(url)
    if data.status_code == 200:
        json_data = json.loads(data.text)
        questions = json_data['results']

        for q in questions:
            q = unescape_dict(q)
            q['incorrect_answers'] = [html.unescape(answer) for answer in q['incorrect_answers']]
            question = Question({
                'question': q['question'],
                'category': q['category'],
                'diff': q['difficulty'],
                'answers': [
                    {'answer': q['correct_answer'],
                     'correctBool': True},
                    {'answer': q['incorrect_answers'][0],
                     'correctBool': False},
                    {'answer': q['incorrect_answers'][1],
                     'correctBool': False},
                    {'answer': q['incorrect_answers'][2],
                     'correctBool': False}
                ]})
            question.save()

    else:
        print('Could not reach the API')


def get_questions(category, no):
    quest = []
    cat_quest = []
    if category == 'Random':
        questions = Question.all()
        for i in range(20):
            random.shuffle(questions)
        for i in range(int(no)):
            quest.append(questions[i])
    else:
        questions = Question.all()
        for q in questions:
            if category in q.category.lower():
                cat_quest.append(q)
        random.shuffle(cat_quest)
        for i in range(int(no)):
            quest.append(cat_quest[i])

    return [q.to_dict() for q in quest]



