from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def contactUs(request):
    return HttpResponse("Contact Us!")

def barPages(request):
    return HttpResponse("Bar Pages")

def signUp(request):
    return HttpResponse("Sign Up!")