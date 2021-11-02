from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render

# from . import models
from django.core import serializers
import json, os

def index(request):

    return HttpResponse("master page index.")