from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from DrinkingBuddy.models import Page, Comment, UserProfile
from DrinkingBuddy.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("Hello World!")


def contactUs(request):
    return HttpResponse("Contact Us!")
##    return render(request, "DrinkingBuddy/contactUs.html", {})


def barPages(request):
    # Need to get the search term and filter by it
    # we will need to think of a way to do this
    # page_list = Page.object.filter(address = search_term)
    # context_dict['pages'] = page_list
    return HttpResponse("Bar Pages")


def signUp(request):
	context_dict = {}
	registered = False
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if "picture" in request.FILES:
				profile.pictures = request.FILES["picture"]
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	context_dict["user_form"] = user_form
	context_dict["profile_form"] = profile_form
	context_dict["registered"] = registered
	return HttpResponse("Sign Up!")
##	return render(request, "DrinkingBuddy/signUp.html", context_dict)


def logIn(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your DrinkingBuddy account has been disabled")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Username or password incorrect.")
	else:
		return HttpResponse("Log in!")
##	return render(request, "DrinkingBuddy/logIn.html", {})


@login_required
def logOut(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def bar(request, page_name_slug):
    context_dict = {}

    try:
        #Puts all the page object in the context dictionary
        #ready to pass them with render
		page = Page.objects.get(slug = page_name_slug)
		context_dict['page'] = page
		#Processes ratings, converting from comma separated integer list
		#to array of integers, then taking the average and
		#passing the average to the template
		# Price
		pRatingList = page.price
		pRatings = pRatingList.split(",")
		avgRating = 0
		for rating in pRatings:
			avgRating += int(rating)
		avgRating = avgRating / len(pRatings)
		context_dict["priceRating"] = avgRating
		# Quality
		qRatingList = page.quality
		qRatings = qRatingList.split(",")
		avgRating = 0
		for rating in qRatings:
			avgRating += int(rating)
		avgRating = avgRating / len(qRatings)
		context_dict["qualityRating"] = avgRating
		# Atmosphere
		aRatingList = page.atmosphere
		aRatings = aRatingList.split(",")
		avgRating = 0
		for rating in aRatings:
			avgRating += int(rating)
		avgRating = avgRating / len(aRatings)
		context_dict["atmosphereRating"] = avgRating
		
		#Adds all comments for the bar to the context dictionary
		comments = Page.objects.filter(name=page)
		context_dict["comments"] = comments

    except Page.DoesNotExist:
		context_dict['page'] = None
		context_dict["comments"] = None
		context_dict["priceRating"] = None
		context_dict["qualityRating"] = None
		context_dict["atmosphereRating"] = None
    return HttpResponse(page_name_slug)
##    return render(request, "DrinkingBuddy/bar.html", context_dict)


def myAccount(request, user_name_slug):
	context_dict = {}
	try:
		#Puts UserProfile object into context dictionary
		profile = UserProfile.objects.get(slug = user_name_slug)
		context_dict["profile"] = profile
	except UserProfile.DoesNotExist:
		context_dict["profile"] = None
	return HttpResponse(user_name_slug)
##	return render(request, "DrinkingBuddy/myAccount.html", context_dict)