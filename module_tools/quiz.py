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
            answers.append({'weight':weight, 'answer_text':line.replace('Answer:', '').replace('[TRUE]', '').replace('[FALSE]', '')})
        line = f.readline()

    qq['answers'] = answers
    quiz.create_question(question=qq)
    f.close()

    return quiz.__getattribute__('id')

def create_attributes_survey(course):
    quiz = course.create_quiz(quiz={'title':"Attributes Survey", 'quiz_type':'survey'})

    qid = quiz.__getattribute__('id')

    quiz.create_question(question={
        'question_name': 'Gender',
        'question_type': 'multiple_choice_question',
        'question_text': 'Which gender do you identify as?',
        'points_possible': '0.0',
        'correct_comments': '',
        'incorrect_comments': '',
        'neutral_comments': '',
        'correct_comments_html': '',
        'incorrect_comments_html': '',
        'neutral_comments_html': '',
        'answers': [{'answer_text':'Male', 'weight':0.0}
                    ,{'answer_text':'Female', 'weight':0.0}
                    ,{'answer_text':'Other', 'weight':0.0}
                    ,{'answer_text':'Prefer not to say', 'weight':0.0}
                    ]
    })

    quiz.create_question(question={
        'question_name': 'Race',
        'question_type': 'multiple_choice_question',
        'question_text': "Which race do you most identify with?",
        'points_possible': '0.0',
        'correct_comments': '',
        'incorrect_comments': '',
        'neutral_comments': '',
        'correct_comments_html': '',
        'incorrect_comments_html': '',
        'neutral_comments_html': '',
        'answers': [{'answer_text': 'African', 'weight': 0.0}, {'answer_text': 'Asian', 'weight': 0.0},
                    {'answer_text': 'Caucasian', 'weight': 0.0}, {'answer_text': 'First Nations/Native American', 'weight': 0.0},
                    {'answer_text': 'Polynesian', 'weight': 0.0}]
    })

    quiz.create_question(question={
        'question_name': 'Faculty',
        'question_type': 'multiple_choice_question',
        'question_text': "Which faculty do you belong to?",
        'points_possible': '0.0',
        'correct_comments': '',
        'incorrect_comments': '',
        'neutral_comments': '',
        'correct_comments_html': '',
        'incorrect_comments_html': '',
        'neutral_comments_html': '',
        'answers': [{'answer_text': 'Arts', 'weight': 0.0}, {'answer_text': 'Sciences', 'weight': 0.0},
                    {'answer_text': 'Management', 'weight': 0.0},
                    {'answer_text': 'Nursing', 'weight': 0.0},
                    {'answer_text': 'Education', 'weight': 0.0}]
    })

    quiz.create_question(question={
        'question_name': 'Year',
        'question_type': 'multiple_choice_question',
        'question_text': "How many years of University have you completed?",
        'points_possible': '0.0',
        'correct_comments': '',
        'incorrect_comments': '',
        'neutral_comments': '',
        'correct_comments_html': '',
        'incorrect_comments_html': '',
        'neutral_comments_html': '',
        'answers': [{'answer_text': '0 - I am a first year', 'weight': 0.0}, {'answer_text': '1 - I am a second year', 'weight': 0.0},
                    {'answer_text': '2 - I am a third year', 'weight': 0.0},
                    {'answer_text': '3 - I am a fourth year', 'weight': 0.0}, {'answer_text': '4 or more - I am an undergraduate', 'weight': 0.0},
                    {'answer_text': 'I am a graduate student', 'weight': 0.0}]
    })

    return qid



