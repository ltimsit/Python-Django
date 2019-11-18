from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django(request):
    return render(request, 'ex01/django.html')
    # return HttpResponse('Bonjour')

def affichage(request):
    test = "bonjour"
    return render(request, 'ex01/affichage.html')
    # return HttpResponse('test1')

def templates(request):
    return render(request, 'ex01/templates.html')
    # return HttpResponse('test2')
