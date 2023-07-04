from django.shortcuts import render,HttpResponse
class SimpleMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        print('sakib first')

    def __call__(self, request):
        url = 'http://127.0.0.1:8000/hello'
        print('sakib')

        response = self.get_response(request)

        return HttpResponse("how are you")
        print('mollah')

        return response