from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import path, include
from . import views
from django.conf.urls import url 

urlpatterns = [
	path('api/users', views.users, name="users_list"),
	url(r'^api/list$', views.users),
	#path('api/users/login', views.login, name="users_login"),
	#path('api/users/register', views.register, name="users_register"),	
]