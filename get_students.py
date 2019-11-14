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


def get_students(url, token, course_id):
    canvas = canvasapi.Canvas(url, token)

    if not course_id:
        # prompt user to select a course they have access to (paginated)
        course_id = course_prompt(canvas)

    course = canvas.get_course(course_id)
    enrollments = course.get_enrollments()
    enrollments = [enrollment for enrollment in enrollments]



