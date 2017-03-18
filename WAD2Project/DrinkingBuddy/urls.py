from django.conf.urls import url
from DrinkingBuddy import views
from DrinkingBuddy.models import Page

app_name = 'DrinkingBuddy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'contactUs$', views.contactUs, name='contactUs'),
    url(r'barPages$', views.barPages, name='barPages'),
    url(r'signUp$', views.signUp, name='signUp'),
    url(r'barPages/(?P<page_name_slug>[\w\-]+)/$', views.bar, name='bar'),
    url(r'myAccount/(?P<user_name_slug>[\w\-]+)/$', views.myAccount, name='myAccount'),
	url(r'logIn$', views.logIn, name='logIn'),
	url(r'logOut$', views.logOut, name='logOut')
    ]