import json

class Request:
    def __init__(self, django_request):
        self.method = django_request.method
        self.headers = dict(django_request.headers)
        self.query = django_request.GET.dict()
        try:
            # Handle empty body for GET requests to avoid decoding errors
            self.body = json.loads(django_request.body) if django_request.body else {}
            self.valid_json = True
        except json.JSONDecodeError:
            self.body = {}
            self.valid_json = False

class Response:
    def __init__(self):
        self.status = 200
        self.data = {}

    def json(self, data, status=200):
        self.data = data
        self.status = status
        return self
