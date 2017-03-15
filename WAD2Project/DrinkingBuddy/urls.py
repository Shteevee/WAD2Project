from django.conf.urls import url
from DrinkingBuddy import views

app_name = 'DrinkingBuddy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'contactUs$', views.contactUs, name='contactUs'),
    url(r'barPages$', views.barPages, name='barPages'),
    url(r'signUp$', views.signUp, name='signUp'),
    ]