from pyramid.view import view_config, forbidden_view_config, notfound_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound

from freeworld.resources import Root, Questions, Question


QUESTIONS = {
    '0': {
        'id': 0,
        'date_added': '',
        'category': 'environment',
        'question': "Do you believe action should be taken to protect our environment?"
    },
    '1': {
        'id': 1,
        'date_added': '',
        'category': 'politics',
        'question': "Are you happy with Trump's victory?"
    }
}


@view_config(request_method='PATCH', context=Question, renderer='json')
def update_question(context, request):
    r = context.update(request.json_body, True)

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8'
    )


@view_config(request_method='GET', context=Question, renderer='json')
def get_question(context, request):
    r = context.retrieve()

    if r is None:
        raise HTTPNotFound()
    else:
        return r


@view_config(request_method='DELETE', context=Question, renderer='json')
def delete_question(context, request):
    context.delete()

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8'
    )


@view_config(request_method='PUT', context=Questions, renderer='json')
def create_question(context, request):
    r = context.create(request.json_body)

    return Response(
        status='201 Created',
        content_type='application/json; charset=UTF-8'
    )


@view_config(request_method="GET", context=Questions, renderer='json')
def list_questions(context, request):
    return context.retrieve()


@notfound_view_config()
def notfound(request):
    return Response(
        body=jspon.dumps({'message': 'Page not found.'}),
        status='404 Not Found',
        content_type='application/json; charset=UTF-8'
    )


@view_config(renderer='json', context=Root)
def home(context, request):
    return {'info': 'Free world, find your voice.'}