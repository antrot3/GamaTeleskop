from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo
from pymongo import MongoClient
from pyramid.response import Response
from cta_project.resources import Root
import csv

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.add_view('cta_project.views.my_view',
                    context='cta_project:resources.Root',
                    renderer='cta_project:templates/mytemplate.pt')
    config.add_static_view('static', 'cta_project:static')
    config.include('pyramid_chameleon')
    config.add_route('csv2' , '/csv2')
    config.add_view('cta_project.views.csvview', route_name = 'csv2')
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.MongoClient
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.MongoClient):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('cta_project')
    return config.make_wsgi_app()
