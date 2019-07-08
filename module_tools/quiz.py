import canvasapi


def create_quiz(course, title, loc):
    quiz = course.create_quiz(quiz={'title':title, 'quiz_type':'assignment'})

    qid = quiz.__getattribute__('id')

    f = open(loc, 'r')

    questions = []

    line = f.readline();
    answers = []
    qq = {}
    i = 1
    while line:
        # print(line)
        if line.lower().startswith('question'):
            if(len(qq) > 0):
                qq['answers'] = answers
                quiz.create_question(question=qq)

                qq = {}
                answers = []
            qq = {
                'question_name': 'Question '+str(i),
                'question_type': 'multiple_choice_question',
                'question_text': line.replace('question:', ''),
                'points_possible': '1.0',
                'correct_comments': '',
                'incorrect_comments': '',
                'neutral_comments': '',
                'correct_comments_html': '',
                'incorrect_comments_html': '',
                'neutral_comments_html': '',
                'answers': []
            }
            i = i+1
        elif line.lower().startswith('answer'):
            weight = 0.0
            if line.__contains__('[TRUE]'):
                weight = 100.0
            answers.append({'answer_text':line.replace('Answer:', '').replace('[TRUE]', '').replace('[FALSE]', ''), 'weight':weight})
        line = f.readline()

    qq['answers'] = answers
    quiz.create_question(question=qq)
    f.close()

    return quiz.__getattribute__('id')
