from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'GfLib/index.html', {'TEMPERATURE':'-0.5'})