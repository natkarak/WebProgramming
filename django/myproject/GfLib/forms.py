from django import forms

from .models import Book

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=60)
	password = forms.CharField(max_length=60, widget=forms.PasswordInput())

class SearchForm(forms.Form):
	title = forms.CharField(label = 'Title', max_length= 100)



