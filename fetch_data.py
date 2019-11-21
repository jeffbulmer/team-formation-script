# -*- coding: utf-8 -*-
import canvasapi
import click
from team_formation import config
from team_formation.data_helpers import process_canvas_course, process_canvas_sections, \
    process_canvas_students
from team_formation.prompts import course_prompt


@click.command()
@click.option('--store_data',
    default=False,
    is_flag=True,
    help='Store data fetched into `.csv` files. [default: False]',
    envvar='CANVAS_STORE_DATA_LOCALLY')
@click.option('--course_id',
    help='Canvas Course ID.',
    type=int,
    envvar='CANVAS_COURSE_ID')
@click.option('--token',
    prompt=False,
    default=config.TOKEN,
    hide_input=True,
    help='Canvas API token.',
    required=True,
    envvar='CANVAS_API_TOKEN')
@click.option('--url',
    default='https://canvas.ubc.ca',
    # default='https://ubc.test.instructure.com',
    help='Canvas Url. [default: https://canvas.ubc.ca]',
    # help='Canvas Url. [default: https://ubc.test.instructure.com]',
    required=True,
    envvar='CANVAS_BASE_URL')
def fetch_data(url, token, course_id, store_data):
    config.STORE_DATA_LOCALLY = store_data
    _fetch_data(url, token, course_id)

def _fetch_data(url, token, course_id):
    canvas = canvasapi.Canvas(url, token)
    data = {}

    if not course_id:
        # prompt user to select a course they have access to (paginated)
        course_id = course_prompt(canvas)

    # get course by id
    course = canvas.get_course(course_id, include=['total_students'])
    data['course_df'] = process_canvas_course(course)

    sections = course.get_sections(include=['students'], per_page=config.PER_PAGE)
    data['sections_df'] = process_canvas_sections(sections)

    students = course.get_users(enrollment_type=['student'], enrollment_stat=['active'], per_page=config.PER_PAGE)
    data['students_df'] = process_canvas_students(students)

    modules = course.get_modules()
    for module in modules:
        module_items =module.get_module_items()
        module_items = [module_item for module_item in module_items]
        for mi in module_items:
            print(mi)

    return (course, data)

def fetch_student_survey_data(course, student_id, quiz_id):
    survey = course.get_quiz(quiz_id)
    students = course.get_users(enrollment_state=['active']);
    student = None;
    for s in students:
        if(s.id == student_id):
            student = s;
            break
    submissions = survey.get_submissions()
    submission = None
    for x in submissions:
        if(x.user_id == student_id):
            submission = x
            break;
    q_data=[]
    if(submission is None):
        return None
    for y in submission.get_submission_events():
        if(y.event_type == 'question_answered'):
            q_data += y.event_data

    read_data = [];
    for z in q_data:
        # print(z);
        q = survey.get_question(int(z['quiz_question_id'])).question_text
        for a in survey.get_question(int(z['quiz_question_id'])).answers:
            if z['answer'] is not None and a['id'] == int(z['answer']):
                # print({'Question':q,'Answer':a['text']})
                read_data.append({'Question':q,'Answer':a['text']});
                break;

    return {'student_name':student.name, 'title':survey.title, 'answers': read_data}

# def fetch_all_survey_data(course, quiz_id):


if __name__ == '__main__':
    fetch_data()