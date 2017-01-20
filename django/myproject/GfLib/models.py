from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	"""Class representing a book- one instance of the class would be one physical copy of the book stored in the library database."""
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
		"""A function inside the class Book, to show the title of the book"""
		return self.title

class Author(models.Model):
	"""A class representing all the authors, whose books are in the library."""
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	
	def __str__(self):
		"""A function inside the class Author, to show the surname of the author"""
		return self.surname 

class Publisher(models.Model):
	"""A class representing a publisher. So here are saved all the names of companies that published at least one of the books in the library."""
	name = models.CharField(max_length=150)
	country = models.CharField(max_length=100)

	def __str__(self):
		"""A function inside the class Publisher, to show the name of the publisher"""
		return self.name

