from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.index, name="master_index")
]