from django.http import HttpResponse


class MiddleWareLifeCycle:

    def __init__(self, get_response):  # name should be get_response only
        self.get_response = get_response

    def __call__(self, request):
        print("Before the view is executed")
        response = self.get_response(request)  # This will pass the request to next middleware in chain if there is any.
        # You can check in the settings.py in MIDDLEWARE list
        print("After the view is executed")
        return response


class ExceptionHandlingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        return HttpResponse('<b>We are currently facing technical Issue. It will be fixed soon</b>')
