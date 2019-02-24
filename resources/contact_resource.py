import json
import falcon

from services import contact_service


class Collection(object):

    def on_get(self, req, resp):
        resp.body = json.dumps(contact_service.find_all_contacts())
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = json.dumps(contact_service.create_contact(**req.context['json_body']))
        resp.status = falcon.HTTP_200


class Item(object):

    def on_get(self, req, resp, id):
        contact = contact_service.get_contact(id)

        if contact:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(contact)
        else:
            resp.status = falcon.HTTP_404

    def on_patch(self, req, resp, id):
        updated_contact = contact_service.update_contact(id, req.context['json_body'])
        if updated_contact:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(updated_contact)
        else:
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, id):
        success = contact_service.delete_contact(id)
        resp.status = falcon.HTTP_200 if success else falcon.HTTP_404
