from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	Author = models.ForeignKey('Author')
	AddedDate = models.DateTimeField(blank=True, null=True)
	Genre = models.CharField(max_length=100)
	Label = models.CharField(max_length=100)
	NPrints = models.PositiveSmallIntegerField(default = 1)
	Publisher = models.ForeignKey('Publisher')
	PubYear = models.PositiveSmallIntegerField(default = 0)
	TimesBorrowed = models.PositiveIntegerField(default = 0)
	Title =	models.CharField(max_length=200)
	Status = models.CharField(max_length=10)

	def publish(self):
		self.AddedDate = timezone.now()
		self.save()

	def __str__(self):
		return self.Title

class Author(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	
	def __str__(self):
		return self.Surname 

class Publisher(models.Model):
	Name = models.CharField(max_length=150)
	Country = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

