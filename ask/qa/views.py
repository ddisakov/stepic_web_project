from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('Hello,world. You are at the qa test')
# Create your views here.

def login(request, *args, **kwargs):
    return HttpResponse('Hello, you are at login')

def signup(request, *args, **kwargs):
    return HttpResponse('Hello, you are at signup')

def question(request, *args, **kwargs):
    return HttpResponse('Hello, you are at question')

def ask(request, *args, **kwargs):
    return HttpResponse('Hello, you are at ask')

def popular(request, *args, **kwargs):
    return HttpResponse('Hello, you are at popular')

def new(request, *args, **kwargs):
    return HttpResponse('Hello, you are at new')