from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Django Quiz App</h1>')