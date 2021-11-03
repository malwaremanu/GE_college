from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password

from rest_framework import authentication, permissions

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework.decorators import api_view


from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
#from rest_framework import serializers as ASD

from django.core import serializers
from . import models

# Create your views here.
def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


@api_view(['GET', 'POST', 'DELETE'])
def users(request):
	msg = ""
	if request.method == 'GET':
		users = models.User.objects.all()
		#print(users)
		uid = request.query_params.get('uid', None)

		if uid is not None:
			users = users.filter(uid__icontains=uid)

		users_serializer = UserSerializer(users, many=True)
		print(users_serializer)
		
		d = serializers.serialize('json', models.User.objects.all())
		msg = "success"
		#return JsonResponse(safe=False)
		return JsonResponse(d, safe=False)
	if request.method == "PUT":

		pass

	if request.method == "POST":

		pass
	
	if request.method == "DELETE":

		pass

	