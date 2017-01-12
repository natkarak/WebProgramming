from django.shortcuts import render


# Create your views here.

def index(request):
	context = {}
	return render(request, 'GfLib/index.html')


def dashboard(request):
	return render(request, 'GfLib/dashboard.html')

def register(request):
	return render(request, 'GfLib/register.html')

def search(request):
	return render(request, 'GfLib/search.html')

def statistics(request):
	return render(request, 'GfLib/statistics.html')