from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	"""One book"""
	title =	models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	free = models.BooleanField(default=True)
	addedDate = models.DateTimeField(blank=True, null=True)
	genre = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	publisher = models.ForeignKey('Publisher')
	pubYear = models.PositiveSmallIntegerField(default = 0)

	def publish(self):
		self.addedDate = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Author(models.Model):
	"""Author if the book"""
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	
	def __str__(self):
		return self.surname 

class Publisher(models.Model):
	"""Publisher - the company that printed the book"""
	name = models.CharField(max_length=150)
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.name

