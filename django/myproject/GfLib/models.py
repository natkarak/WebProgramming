from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	Author = models.ForeignKey('Author')
	AddedDate = models.DateTimeField(default=timezone.now)
	Genre = models.CharField(max_length=100)
	Label = models.CharField(max_length=100)
	NPrints = models.PositiveSmallIntegerField()
	Publisher = models.CharField(max_length=150)
#	PubYear =
	TimesBorrowed = models.PositiveIntegerField()
	Title =	models.CharField(max_length=200)
	Status = models.CharField(max_length=10)

class Author(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
#	ActiveFrom =
#	ActiveUntil = 
