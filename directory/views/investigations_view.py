from django.http import request
from django.shortcuts import render
from directory.models import Investigation


def index(request):
    investigations = Investigation.objects.all()
    context_dict = {'investigations': investigations}
    return render(request, 'investigations.html', context_dict)
 

