from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

import sys

from .models import Book

from .forms import LoginForm



# Create your views here.

def index(request):
	return render(request, 'GfLib/index.html')

def login_view(request):
	context = {'loginForm':LoginForm()}
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print("The account has been disabled!")
			else:
				print("The username and password were incorrect.")	
	else:
		form = LoginForm()
	context['loginForm'] = form
	return render(request, 'GfLib/login.html', {'form': form})
	

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def dashboard(request):
	books = Book.objects.all()
	return render(request, 'GfLib/dashboard.html', {'books' : books})

def register(request):
	return render(request, 'GfLib/register.html')

def search(request):
	return render(request, 'GfLib/search.html')

def statistics(request):
	return render(request, 'GfLib/statistics.html')
