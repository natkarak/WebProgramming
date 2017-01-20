from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
	username = forms.CharField(label=_('Username'), max_length=60, localize=True)
	password = forms.CharField(label=_('Password'), max_length=60, widget=forms.PasswordInput, localize=True)

class SearchForm(forms.Form):
	title = forms.CharField(label = _('Title'), max_length= 100, localize=True)