import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD2Project.settings')

import django
django.setup()
from DrinkingBuddy.models import Page, UserProfile, Comment
from django.contrib.auth.models import User

def populate():
	## Example details for testing purposes.
	## Should be changed before submission/presentation
	bar1_comments = [
		{"comment": "A good bar in my opinion, some people like it, some don't.",
		 "user": "CommenterA"},
		{"comment": "People have told me good things about this place, but I didn't have a good time.",
		 "user": "CommenterB"}]
	bar2_comments = [
		{"comment": "Terrible bar, far too expensive and it's not even good drinks either.",
		 "user": "CommenterB"},
		{"comment": "Had a pretty bad time last I was here, wouldn't go again.",
		 "user": "CommenterC"}]
	bar3_comments = [
		{"comment": "One of the best bars I've ever been to.",
		 "user": "CommenterC"},
		{"comment": "Really cheap bar, good drinks, nice people there. Became one of my favourites.",
		 "user": "CommenterA"}]
	
	users = [
		{"username": "BarOwnerA",
		 "password": "1q2w3e4r5t",
		 "email": "barowner@example.com",
		 "owner": True},
		{"username": "BarOwnerB",
		 "password": "1q2w3e4r5t",
		 "email": "barowner2@example.com",
		 "owner": True}, 
		{"username": "BarOwnerC",
		 "password": "1q2w3e4r5t",
		 "email": "barowner3@example.com",
		 "owner": True}, 
		{"username": "CommenterA",
		 "password": "1q2w3e4r5t",
		 "email": "commenter1@example.com",
		 "owner": False}, 
		{"username": "CommenterB",
		 "password": "1q2w3e4r5t",
		 "email": "commenter2@example.com",
		 "owner": False}, 
		{"username": "CommenterC",
		 "password": "1q2w3e4r5t",
		 "email": "commenter3@example.com",
		 "owner": False} ]
	bars = [
		{"name": "Bar 1",
		 "desc": "A bar.",
		 "addr": "123 Fake St",
		 "price": "1,2,3,4,5",
		 "atmos": "1,2,3,4,5",
		 "qual": "1,2,3,4,5",
		 "owner": "BarOwnerA",
		 "comments": bar1_comments},
		{"name": "Bar 2",
		 "desc": "A second bar.",
		 "addr": "456 Fake St",
		 "price": "1,1,1,1,1",
		 "atmos": "1,1,1,1,1",
		 "qual": "1,1,1,1,1",
		 "owner": "BarOwnerB",
		 "comments": bar2_comments},
		 {"name": "Bar 3",
		 "desc": "A third bar.",
		 "addr": "789 Fake St",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "BarOwnerC",
		 "comments": bar3_comments} ]
		 
	for user in users:
		add_user(user["username"], user["password"], user["email"], user["owner"])
	for bar in bars:
		page = add_bar(bar["name"], bar["desc"], bar["addr"], bar["owner"], bar["price"], bar["atmos"], bar["qual"])
		for comment in bar["comments"]:
			add_comment(comment["comment"], comment["user"], page)
		
	for b in Page.objects.all():
		print("- {0}".format(unicode(b)))
		for c in Comment.objects.filter(page=b):
			print("-- {0}".format(unicode(c)))
	for u in UserProfile.objects.all():
		print("- {0}".format(unicode(u)))
		
def add_user(username, password, email, owner):
	u, created = User.objects.get_or_create(username=username, email=email)
	if not created:
		u.set_password(password)
	up = UserProfile.objects.get_or_create(user=u)[0]
	up.owner = owner
	up.save()
	return up
	
		
def add_bar(name, desc, addr, owner, price, atmos, qual):
	owner = UserProfile.objects.get(user=User.objects.get(username=owner))
	b = Page.objects.get_or_create(name=name, owner=owner)[0]
	b.description = desc
	b.address = addr
	b.price = price
	b.atmosphere = atmos
	b.quality = qual
	b.save()
	return b
	
def add_comment(comment, user, page):
	commenter = UserProfile.objects.get(user=User.objects.get(username=user))
	c = Comment.objects.get_or_create(comment=comment, commenter=commenter, page=page)[0]
	c.save()
	return c
	
if __name__ == '__main__':
	print("Starting Drinking Buddy population script...")
	populate()