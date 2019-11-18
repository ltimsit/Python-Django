from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # print(request)
    return render(request, 'ex00/index.html')
    # return HttpResponse("Hello world")

# Create your views here.
