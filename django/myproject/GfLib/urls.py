from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^register/', views.register, name='register'),
	url(r'^search/', views.search, name='search'),
#	url(r'^searchResult/', views.searchResult, name='searchResult'),
	url(r'^statistics/', views.statistics, name='statistics'),
]