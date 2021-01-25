from Data_mongo.repositories.question_repository import get_questions


def run():
    running = True
    while running:
        no = 5
        questions = get_questions(5)
        for q in questions:
            question = q.question
            answers = q.answers
            answers.append(q.correctanswer)



