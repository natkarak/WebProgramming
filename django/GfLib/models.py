from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User') 
	pubYear = #year
	added = models.DateTimeField( default=datetime.now ) #check thiiiiiiiiiissssss
	timesBorrowed = models.PositiveIntegerField()
	status = models.CharField(max_length=10) #borrowed/free
	label = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	publisher = models.CharField(max_length=150)
	nPrints = models.PositiveSmallIntegerField()
	

class Author(models.Model):
	name = 
	surname = 
	activeFrom =
	activeTill = 

#class User(models.Model)
