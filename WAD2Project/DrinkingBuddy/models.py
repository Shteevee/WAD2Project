from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    owner = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
	# Users need a slug for the account page
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Page(models.Model):
    name_max_length = 50
    desc_max_length = 200
    addr_max_length = 100
    name = models.CharField(max_length=name_max_length, unique=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='bar_images', blank=True)
    description = models.CharField(max_length=desc_max_length)
    address = models.CharField(max_length=addr_max_length)
    added = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(UserProfile, limit_choices_to={"owner": True}, on_delete=models.CASCADE)
	## Bars are deleted from website if owner deletes account
    price = models.TextField(validators=[validate_comma_separated_integer_list])
    quality = models.TextField(validators=[validate_comma_separated_integer_list])
    atmosphere = models.TextField(validators=[validate_comma_separated_integer_list])
    ## Ratings are stored as comma seperated lists of integers
    avgPrice = models.FloatField(default=0.0)
    avgQuality = models.FloatField(default=0.0)
    avgAtmos = models.FloatField(default=0.0)
	## Averages calculated when model is saved
    avgRating = models.FloatField(default=0.0)
	## Average of all 3 categories

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.avgPrice = 0.0
        self.avgQuality = 0.0
        self.avgAtmos = 0.0
        if self.price != "":
            pRatings = self.price.split(",")
            for rating in pRatings:
                if rating != '':
                    self.avgPrice += int(rating)
            self.avgPrice = self.avgPrice / len(pRatings)
        if self.quality != "":
            qRatings = self.quality.split(",")
            for rating in qRatings:
                if rating != '':
                    self.avgQuality += int(rating)
            self.avgQuality = self.avgQuality / len(qRatings)
        if self.atmosphere != "":
            aRatings = self.atmosphere.split(",")
            for rating in aRatings:
                if rating != '':
                    self.avgAtmos += int(rating)
            self.avgAtmos = self.avgAtmos / len(aRatings)
        self.avgRating = (self.avgPrice + self.avgQuality + self.avgAtmos) / 3
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    comment_max_length = 200
    comment = models.CharField(max_length=comment_max_length)
    date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    ## Comments are deleted when the user who wrote it
    ## or the page commented on is deleted.

    def __str__(self):
##        return self.comment  ## May need changed?
		return str(self.commenter) + ''': "''' + self.comment[:40] + '''..."'''

    def __unicode__(self):
##		return self.comment ## May need changed?
		return unicode(self.commenter) + ''': "''' + self.comment[:40] + '''..."'''