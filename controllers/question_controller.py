from difflib import SequenceMatcher
from flask import flash
from Data_mongo.repositories import question_repository as qr


def add_question(question):
    qr.add_question(question)


def check_and_add_q(new_question):
    category, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3 = new_question
    questions = qr.get_questions()

    for q in questions:
        seq = SequenceMatcher(None, question, q.question)
        s = seq.ratio()
        if s < 0.75:
            continue
        else:
            return flash('Din fråga är för lik en som redan existerar!')

    wrong_answers = wrong_answer1, wrong_answer2, wrong_answer3
    if all(a != right_answer for a in wrong_answers):
        if len(wrong_answers) == len(set(wrong_answers)):
            qr.add_question(new_question)
            return flash('Frågan har blivit tillagd!')
        else:
            return flash('Felaktiga svar måste vara unika!')
    else:
        return flash('Ett rätt svar kan inte vara samma som ett felaktigt svar!')



