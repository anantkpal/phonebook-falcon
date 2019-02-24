import json
import falcon


class JSONMiddleWare(object):

    def process_request(self, req, resp):
        if req.method in ['POST', 'PUT', 'PATCH'] and falcon.MEDIA_JSON.startswith(getattr(req, 'content_type', '')):
            req.context['json_body'] = json.loads(req.stream.read())
