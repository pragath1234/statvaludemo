from django.shortcuts import render
from django.http import HttpResponse

def pages(request):
    return HttpResponse('!!!! Welcome to StatValu Blog !!')

