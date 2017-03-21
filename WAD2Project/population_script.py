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
	bar4_comments = [
		{"comment": "Good beer, good food, nice staff",
		 "user": "CommenterA"},
		{"comment": "Spacious place, vegan, live music.",
		 "user": "CommenterC"}]
	bar5_comments = [
		{"comment": "I like this pub for the pure convenience of it and cheap drinks.",
		 "user": "CommenterB"},
		{"comment": "Their food is good and they have a nice selection of beers.",
		 "user": "CommenterC"}]
	bar6_comments = [
		{"comment": "I love the music, they seem to do a broad mix and yet I know every third song.",
		 "user": "CommenterB"},
		{"comment": "It's good to be able to get decent bar snacks until late on.",
		 "user": "CommenterA"}]
	
	users = [
		{"username": "Adam Murphy",
		 "password": "1q2w3e4r5t",
		 "email": "barowner@example.com",
		 "owner": True},
		{"username": "Alan Turing",
		 "password": "1q2w3e4r5t",
		 "email": "barowner2@example.com",
		 "owner": True}, 
		{"username": "Marie Curie",
		 "password": "1q2w3e4r5t",
		 "email": "barowner3@example.com",
		 "owner": True}, 
		 {"username": "Albert Einstein",
		 "password": "1q2w3e4r5t",
		 "email": "barowner@example.com",
		 "owner": True},
		{"username": "Nikola Tesla",
		 "password": "1q2w3e4r5t",
		 "email": "barowner2@example.com",
		 "owner": True}, 
		{"username": "Blaise Pascal",
		 "password": "1q2w3e4r5t",
		 "email": "barowner3@example.com",
		 "owner": True}, 
		 {"username": "Isaac Newton",
		 "password": "1q2w3e4r5t",
		 "email": "barowner@example.com",
		 "owner": True},
		{"username": "Felix Browder",
		 "password": "1q2w3e4r5t",
		 "email": "barowner2@example.com",
		 "owner": True}, 
		{"username": "David Blackwell",
		 "password": "1q2w3e4r5t",
		 "email": "barowner3@example.com",
		 "owner": True}, 
		 {"username": "Ronald Graham",
		 "password": "1q2w3e4r5t",
		 "email": "barowner3@example.com",
		 "owner": True}, 
		 {"username": "Jesse Douglas",
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
		{"name": "The Pot Still",
		 "desc": "A bar.",
		 "addr": "154 Hope Street, G2  2TH",
		 "price": "1,2,3,4,5",
		 "atmos": "1,2,3,4,5",
		 "qual": "1,2,3,4,5",
		 "owner": "Adam Murphy",
		 "picture": "bar_images/pot_still.jpg",
		 "comments": bar1_comments},
		{"name": "Tabac",
		 "desc": "A second bar.",
		 "addr": "10 Mitchell Lane, G1 3NU",
		 "price": "1,1,1,1,1",
		 "atmos": "1,1,1,1,1",
		 "qual": "1,1,1,1,1",
		 "owner": "Alan Turing",
		 "picture": "bar_images/tabac.jpg",
		 "comments": bar2_comments},
		 {"name": "Oran Mor",
		 "desc": "A third bar.",
		 "addr": "731-735 Great Western Road, G12 8QX",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "Marie Curie",
		 "picture": "bar_images/oran_mor.jpg",
		 "comments": bar3_comments},
		 {"name": "Sloans",
		 "desc": "A bar.",
		 "addr": "62 Argyll Arcade, G2 8BG",
		 "price": "1,2,3,4,5",
		 "atmos": "1,2,3,4,5",
		 "qual": "1,2,3,4,5",
		 "owner": "Albert Einstein",
		 "picture": "bar_images/sloans.jpg",
		 "comments": bar4_comments},
		{"name": "The Flying Duck",
		 "desc": "A second bar.",
		 "addr": "142 Renfield Street, G2 3AU",
		 "price": "1,1,1,1,1",
		 "atmos": "1,1,1,1,1",
		 "qual": "1,1,1,1,1",
		 "owner": "Nikola Tesla",
		 "picture": "bar_images/flying_duck.jpg",
		 "comments": bar5_comments},
		 {"name": "Blackfriars",
		 "desc": "A third bar.",
		 "addr": "36 Bell Street, G1 1LG ",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "Blaise Pascal",
		 "picture": "bar_images/oran_mor.jpg",
		 "comments": bar6_comments},
		 {"name": "Curlers Rest",
		 "desc": "A bar.",
		 "addr": "256-260 Byres Road, G12 8SH",
		 "price": "1,2,3,4,5",
		 "atmos": "1,2,3,4,5",
		 "qual": "1,2,3,4,5",
		 "owner": "Isaac Newton",
		 "picture": "bar_images/curlers.jpg",
		 "comments": bar1_comments},
		{"name": "The Rock",
		 "desc": "A second bar.",
		 "addr": "205 Hyndland Road, G12 9HE",
		 "price": "1,1,1,1,1",
		 "atmos": "1,1,1,1,1",
		 "qual": "1,1,1,1,1",
		 "owner": "Felix Browder",
		 "picture": "bar_images/rock.jpg",
		 "comments": bar2_comments},
		 {"name": "Hummingbird",
		 "desc": "A third bar.",
		 "addr": "186 Bath Street, G2 4HG",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "David Blackwell",
		 "picture": "bar_images/humming_bird.jpg",
		 "comments": bar3_comments},
		 {"name": "The Sparkle Horse",
		 "desc": "A third bar.",
		 "addr": "16 Dowanhill Street, G11 5QS",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "Ronald Graham",
		 "picture": "bar_images/sparkle_horse.jpg",
		 "comments": bar4_comments},
		 {"name": "The Lab",
		 "desc": "A third bar.",
		 "addr": "26 Springfield Court, G1  3DQ",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5",
		 "owner": "Jesse Douglas",
		 "picture": "bar_images/lab.jpg",
		 "comments": bar5_comments},
		 ]
		 
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