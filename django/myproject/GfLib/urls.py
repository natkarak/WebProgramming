from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^register/', views.register, name='register'),
	url(r'^search/', views.search, name='search'),
	url(r'^searchResult/', views.searchResult, name='searchResult'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^login/$', views.login_view, name = 'login'),
	url(r'^([0-9]+)/$', views.detail, name = 'detail'),
]