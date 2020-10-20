from django.shortcuts import render
from django.http import HttpResponse


def homepage_view(request):
    return HttpResponse('<h1>Hello, World!</h1>')
