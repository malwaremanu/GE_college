from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
	#db = 
	
	context = {
		"msg" : "success"
	}
	return JsonResponse(context)
