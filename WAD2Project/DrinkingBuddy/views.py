from django.shortcuts import render
from django.http import HttpResponse
from DrinkingBuddy.models import Page

def index(request):
    return HttpResponse("Hello World!")

def contactUs(request):
    return HttpResponse("Contact Us!")

def barPages(request):
    return HttpResponse("Bar Pages")

def signUp(request):
    return HttpResponse("Sign Up!")

def bar(request, bar_name_slug):
    #context_dict = {}

    #try:
        #page = Page.objects.get(bar_name_slug)
        #context_dict['page'] = page

    #except Page.DoesNotExist:
        #context_dict['page'] = None
    #return HttpResponse(Page.objects.get(slug = bar_name_slug))
    return HttpResponse("It worked!")