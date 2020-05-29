from wsgi_cors_middleware import CorsMiddleware


class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response