from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from DrinkingBuddy.models import Page, Comment, UserProfile
from DrinkingBuddy.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
#from DrinkingBuddy.contactus import send_mail

def index(request):
    context_dict = {}
    recently_added = Page.objects.order_by("-added")[:5]
    context_dict["recent"] = recently_added
    highest_rated = Page.objects.order_by("-avgRating")[:5]
    context_dict["highest_rated"] = highest_rated
    return render(request, "DrinkingBuddy/index.html", context_dict)


def contactUs(request):
    return render(request, "DrinkingBuddy/contactUs.html", {})


def barPages(request):
    context_dict = {}
    if request.method == "POST":
        search_term = request.POST.get("search_term")
        page_list = Page.objects.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term) | Q(address__icontains=search_term)).order_by("-avgRating")
    else:
        page_list = Page.objects.all().order_by("-avgRating")
    context_dict["pages"] = page_list
    return render(request, "DrinkingBuddy/barPages.html", context_dict)


def signUp(request):
	context_dict = {}
	registered = False
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(request.POST, request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()
			registered = True
			userLogin = authenticate(username=user.username,password=user.password)
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	context_dict["user_form"] = user_form
	context_dict["profile_form"] = profile_form
	context_dict["registered"] = registered
	return render(request, "DrinkingBuddy/signUp.html", context_dict)


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
		return HttpResponseRedirect(reverse('index'))


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
		#Postcode to be used my mapsapi
		postcode = page.address.split(", ")[len(page.address.split(", "))-1]
		context_dict['postcode']=postcode
		#Adds all comments for the bar to the context dictionary
		comments = Comment.objects.filter(page=page)
		context_dict["comments"] = comments
		# Adds ratings form to context dict
		rform = RatingForm(prefix="rform")
		context_dict["rating_form"] = rform
		# Adds comment form to context dict
		cform = CommentForm(prefix="cform")
		context_dict["comment_form"] = cform
		#Checks if the user is the owner, for editting purposes
		if request.user.is_authenticated:
		    user_profile = UserProfile.objects.get(user=request.user)
		    editForm = PageEditorForm(prefix='eform')
		    if user_profile != None:
		        if page.owner == user_profile:
		            context_dict['page_editor_form'] = editForm

		if request.method =="POST":
			rform = RatingForm(request.POST, prefix="rform")
			if rform.is_valid():
				# Check each rating exists, add to list in model
				if rform["priceRating"].value():
					page.price = page.price + "," + rform["priceRating"].value()
				if rform["qualityRating"].value():
					page.quality = page.quality + "," + rform["qualityRating"].value()
				if rform["atmosphereRating"].value():
					page.atmosphere = page.atmosphere + "," + rform["atmosphereRating"].value()
				page.save()
			cform = CommentForm(request.POST, prefix="cform")
			if cform.is_valid():
				comment = cform.save(commit=False)
				comment.page = page
				comment.commenter = UserProfile.objects.get(user=request.user)
				comment.save()
			else:
				print(cform.errors)

            #get the image from the form and set it
			editForm = PageEditorForm(request.POST, request.FILES)
			if editForm.is_valid():
			    print request.FILES
			    if 'eform-picture' in request.FILES:
			        page.picture = request.FILES['eform-picture']
		            page.save()


    except Page.DoesNotExist:
		context_dict['page'] = None
		context_dict["comments"] = None
		context_dict["rating_form"] = None
		context_dict["comment_form"] = None
    return render(request, "DrinkingBuddy/bar.html", context_dict)


@login_required
def addBar(request):
	form = PageForm()
	if request.method == "POST":
		form = PageForm(request.POST, request.FILES)
		if form.is_valid():
			page = form.save(commit=False)
			page.owner = UserProfile.objects.get(user = request.user)
			page.save()
			return myAccount(request)
		else:
			print(form.errors)
	return render(request, "DrinkingBuddy/add-bar.html", {"page_form": form})


@login_required
def myAccount(request):
	context_dict = {}

	try:
		#Puts UserProfile object into context dictionary
		profile = UserProfile.objects.get(user = request.user)
		context_dict["profile"] = profile
		form = UserEditorForm()
		context_dict["user_editor_form"] = form
		if profile.owner:
			try:
				own_bar = Page.objects.get(owner = profile)
				context_dict["own_bar"] = own_bar
			except Page.DoesNotExist:
				context_dict["own_bar"] = None

		if request.method =="POST":
		    form = UserEditorForm(request.POST, request.FILES)
		    if form.is_valid():
		        if 'picture' in request.FILES:
		            profile.picture = request.FILES['picture']
		            profile.save()
		            return myAccount(request)

	except UserProfile.DoesNotExist:
		context_dict["profile"] = None
		context_dict["own_bar"] = None
	return render(request, "DrinkingBuddy/account.html", context_dict)