import canvasapi
import click

from team_formation import config
from team_formation.prompts import course_prompt
from module_tools import quiz
from module_tools import page

@click.command()
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
    # default='https://canvas.ubc.ca',
    default='https://ubc.test.instructure.com',
    # help='Canvas Url. [default: https://canvas.ubc.ca]',
    help='Canvas Url. [default: https://ubc.test.instructure.com]',
    required=True,
    envvar='CANVAS_BASE_URL')
@click.option('--location',
    help='File Folder containing module content',
    prompt=True,
    required=True)


def create_module(url, token, course_id, location):
    canvas = canvasapi.Canvas(url, token)

    if not course_id:
        # prompt user to select a course they have access to (paginated)
        course_id = course_prompt(canvas)

    course = canvas.get_course(course_id)
    module = course.create_module(module={'name':'test module'})
    # create learning outcomes
    lo = page.create_page(course, "Learning Outcomes", location+'/Learning Outcomes.txt')
    # create pre-test
    # pret = course.create_quiz(quiz={'title':'pre-test'})
    pret = quiz.create_quiz(course, 'Pre-Test', loc=location+'/Quizformat.txt')
    # create post-test
    # postt = course.create_quiz(quiz={'title':'post-test'})
    postt = quiz.create_quiz(course, 'Post-Test', loc=location+'/Quizformat.txt')
    # create readings
    rea = page.create_page(course, 'Readings', loc=location+'/Readings.txt')
    # add videos
    #
    #add slides

    module.create_module_item(module_item={'title':'Learning Outcomes', 'type':'Page', \
                                           'content_id':None, 'page_url':lo})
    module.create_module_item(module_item={'title':'Pre-Test', 'type':'Quiz', \
                                           'content_id':pret})
    module.create_module_item(module_item={'title':'Post-Test', 'type':'Quiz', \
                                           'content_id':postt})
    module.create_module_item(module_item={'title':'Readings', 'type':'Page', \
                                           'content_id':None, 'page_url':rea})

if __name__ == '__main__':
    create_module()