import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD2Project.settings')

import django
django.setup()
from DrinkingBuddy.models import Page

def populate():
	## Example details for testing purposes.
	## Should be changed before submission/presentation
	bars = [
		{"name": "Bar 1",
		 "desc": "A bar.",
		 "addr": "123 Fake St",
		 "price": "1,2,3,4,5",
		 "atmos": "1,2,3,4,5",
		 "qual": "1,2,3,4,5"},
		{"name": "Bar 2",
		 "desc": "A second bar.",
		 "addr": "456 Fake St",
		 "price": "1,1,1,1,1",
		 "atmos": "1,1,1,1,1",
		 "qual": "1,1,1,1,1"},
		 {"name": "Bar 3",
		 "desc": "A third bar.",
		 "addr": "789 Fake St",
		 "price": "5,5,5,5,5",
		 "atmos": "5,5,5,5,5",
		 "qual": "5,5,5,5,5"} ]
		 
	for bar in bars:
		add_bar(bar["name"], bar["desc"], bar["addr"], bar["price"], bar["atmos"], bar["qual"])
		
	for b in Page.objects.all():
		print("- {0}".format(unicode(b)))
		
def add_bar(name, desc, addr, price, atmos, qual):
	b = Page.objects.get_or_create(name=name)[0]
	b.description = desc
	b.address = addr
	b.price = price
	b.atmosphere = atmos
	b.quality = qual
	b.save()
	return b
	
if __name__ == '__main__':
	print("Starting Drinking Buddy population script...")
	populate()