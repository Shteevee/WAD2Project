from django.conf.urls import url
from DrinkingBuddy import views
from DrinkingBuddy.models import Page


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'contactUs$', views.contactUs, name='contactUs'),
    url(r'barPages$', views.barPages, name='barPages'),
    url(r'signUp$', views.signUp, name='signUp'),
    url(r'barPages/(?P<page_name_slug>[\w\-]+)/$', views.bar, name='bar'),
    url(r'myAccount/$', views.myAccount, name='myAccount'),
	url(r'myAccount/addBar/$', views.addBar, name='addBar'),
	url(r'logIn$', views.logIn, name='logIn'),
	url(r'logOut$', views.logOut, name='logOut')
    ]