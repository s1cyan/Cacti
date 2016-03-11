from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
    return render(request, 'templates/greetings.html')
