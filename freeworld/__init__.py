from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('questions', '/questions')
    config.add_route('category_questions', '/questions/{category}')
    config.add_route('question', '/question/{id}')
    config.scan()
    return config.make_wsgi_app()
