from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse("this is main_index page.")