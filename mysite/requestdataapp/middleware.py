def suor_middleware(get_response):
    def middleware(request):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        return response

    return middleware
def suor_middleware(get_response):
    def middleware(request):
        request


class CRMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rq = 0
        self.rs = 0
        self.ec = 0

    def __call__(self, request):
        self.rq += 1
        response = self.get_response(request)
        self.rs += 1
        print(self.rq, self.rs)
        return response

    def get_ex(self, request, exception):
        self.ec += 1
        print(self.ec)
