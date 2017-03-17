from django.shortcuts import render
from django.http import HttpResponse
from DrinkingBuddy.models import Page


def index(request):
    return HttpResponse("Hello World!")


def contactUs(request):
    return HttpResponse("Contact Us!")


def barPages(request):
    # Need to get the search term and filter by it
    # we will need to think of a way to do this
    # page_list = Page.object.filter(address = search_term)
    # context_dict['pages'] = page_list
    return HttpResponse("Bar Pages")


def signUp(request):
    return HttpResponse("Sign Up!")


def bar(request, page_name_slug):
    context_dict = {}

    try:
        #Puts all the page object in the context dictionary
        #ready to pass them with render
        page = Page.objects.get(slug = page_name_slug)
        context_dict['page'] = page

    except Page.DoesNotExist:
        context_dict['page'] = None
    #return HttpResponse(Page.objects.get(slug = page_name_slug))
    return HttpResponse("It worked!")


# def myAccount(request, user_name_slug):