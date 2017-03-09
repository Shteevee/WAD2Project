from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_seperated_integer_list

class Page(models.Model):
	name_max_length = 50
	desc_max_length = 200
	addr_max_length = 100
	name = models.CharField(max_length=name_max_length, unique=True)
	slug = models.SlugField(unique=True)
	picture = models.ImageField(upload_to='bar_images', blank=True)
	description = models.CharField(max_length=desc_max_length)
	address = models.CharField(max_length=addr_max_length)
	## Ratings are stored as comma seperated lists of integers
	## Averages must be calculated when page is loaded
	price = models.TextField(validators=[validate_comma_seperated_integer_list])
	quality = models.TextField(validators=[validate_comma_seperated_integer_list])
	atmosphere = models.TextField(validators=[validate_comma_seperated_integer_list])
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Page, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name
		
	def __unicode__(self):
		return self.name
		
		
class Comment(models.Model):
	comment_max_length = 200
	comment = models.CharField(max_length=comment_max_length)
	date = models.DateTimeField(auto_add_now=True)
	commenter = models.ForeignKey(UserProfile, on_delete=CASCADE)
	page = models.ForeignKey(Page, on_delete=CASCADE)
	## Comments are deleted when the user who wrote it
	## or the page commented on is deleted.
	
	def __str__(self):
		return self.comment		## May need changed?
		
	def __unicode__(self):
		return self.comment		## May need changed?
		
		
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	owner = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.username
		
	def __unicode__(self):
		return self.user.username