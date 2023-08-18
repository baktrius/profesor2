from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

def lesson(request, temp_id):
    return HttpResponse("You're looking at question %s." % temp_id)