import canvasapi

def create_page(course, title, loc):
    body = ''

    f = open(loc, 'r')

    line = f.readline()

    while(line):
        body += line
        line = f.readline()

    f.close()
    page = course.create_page(wiki_page={'title':title, 'body':body})

    return page.__getattribute__('url')