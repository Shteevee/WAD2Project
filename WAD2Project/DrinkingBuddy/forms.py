from django import forms
from django.contrib.auth.models import User
from DrinkingBuddy import models


class PageForm(forms.ModelForm):
    name = forms.CharField(max_length = Page.name_max_length,
                           help_text = "Please enter the bar's name.")
    # The address needs separated into how address forms look
    address = forms.CharField(max_length = Page.addr_max_length,
                              help_text = "Please enter adress.")
    description = forms.CharField(max_length = Page.desc_max_length,
                                  help_text = "Please enter a description.")
    picture = forms.ImageField(help_text = "Please add an image of the bar.")

    # This may need changing?
    price = forms.TextField(widget = forms.HiddenInput(), initial=[])
    quality = forms.TextField(widget=forms.HiddenInput(), initial=[])
    atmosphere = forms.TextField(widget=forms.HiddenInput(), initial=[])

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        fields = ('name','address','description')


class UserForm(form.ModelForm):
    password = forms.CharField(widget = forms)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(form.ModelForm):
    class Meta:
        model = UserProfile
        fields('picture', 'owner')
