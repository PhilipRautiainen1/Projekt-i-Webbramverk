from difflib import SequenceMatcher

from flask import flash

from Data_mongo.models import Question
from Data_mongo.repositories import question_repository as qr


def add_question(question):
    qr.add_question(question)


def check_and_add_q(question):
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

    questions = qr.get_questions()

    for q in questions:
        seq = SequenceMatcher(None, question, q)
        s = seq.ratio()
    if s < 0.85:
        wrong_answers = [question['wrong_answer1'], question['wrong_answer2'], ['wrong_answer3']]
        if all(a != question['correct_answer'] for a in wrong_answers):
            if len(wrong_answers) == len(set(wrong_answers)):
                qr.save_question(question)
                flash('Frågan har blivit tillagd!')
            else:
                flash('Felaktiga svar måste vara unika!')
        else:
            flash('Ett rätt svar kan inte vara ett som är fel!')
    else:
        flash('Din fråga är för lik en som redan existerar!')