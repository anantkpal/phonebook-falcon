import falcon

from models.base import engine, Base
from middleware.json_middleware import JSONMiddleWare
from resources import contact_resource

# create all tables
Base.metadata.create_all(engine)

api = application = falcon.API(middleware=JSONMiddleWare())
api.add_route('/contacts', contact_resource.Collection())
api.add_route('/contacts/{id:int}', contact_resource.Item())
