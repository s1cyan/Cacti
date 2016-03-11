from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context_dict = {
            'page_title': 'Cacti'
            }
    return render(request, 'greetings.html', context_dict)
