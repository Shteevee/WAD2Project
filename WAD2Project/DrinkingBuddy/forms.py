from django import forms
from django.contrib.auth.models import User
from DrinkingBuddy.models import Page, UserProfile, Comment


class PageForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control input-lg"}), 
                           max_length = Page.name_max_length,
                           help_text = "Please enter the bar's name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # The address needs separated into how address forms look
    address = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control input-lg"}), 
                              max_length = Page.addr_max_length,
                              help_text = "Please enter adress.")
    description = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control input-lg"}), 
                                  max_length = Page.desc_max_length,
                                  help_text = "Please enter a description.")
    picture = forms.ImageField(help_text = "Please add an image of the bar.", required=False)

    price = forms.CharField(widget=forms.HiddenInput(), initial="", required=False)
    quality = forms.CharField(widget=forms.HiddenInput(), initial="", required=False)
    atmosphere = forms.CharField(widget=forms.HiddenInput(), initial="", required=False)
    avgPrice = forms.CharField(widget=forms.HiddenInput(), initial=0)
    avgQuality = forms.CharField(widget=forms.HiddenInput(), initial=0)
    avgAtmos = forms.CharField(widget=forms.HiddenInput(), initial=0)
    avgRating = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        fields = ('name','address','description','picture')
        exclude = ('owner',)


class RatingForm(forms.Form):
	RATING_CHOICES = (("1", "1 Glass"), ("2", "2 Glasses"), ("3", "3 Glasses"), ("4", "4 Glasses"), ("5", "5 Glasses"))
	priceRating = forms.ChoiceField(choices = RATING_CHOICES, label="Price")
	qualityRating = forms.ChoiceField(choices = RATING_CHOICES, label="Quality")
	atmosphereRating = forms.ChoiceField(choices = RATING_CHOICES, label="Atmosphere")


class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control input-lg"}), max_length = Comment.comment_max_length, label="Comment (max. 200 characters)")
	
	class Meta:
		model = Comment
		fields = ('comment',)

		
class UserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control input-lg"}))
    email = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control input-lg"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class": "form-control input-lg"}))
	
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'owner')
