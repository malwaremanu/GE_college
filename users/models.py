from django.db import models
import datetime

# Create your models here.
class User(models.Model):
	username= None
	email = models.EmailField(unique=True)
	name = models.TextField()
	password=models.TextField()

	uid = models.UUIDField(
	default=None,
	blank=True,
	null=True,
	unique=True,
	)

	posts = [(10,'SUPERADMIN'), (5,'ACCOUNTS'), (7,'ADMIN'), (3,'STAFF'), (1,'LIBRARY')]

	department = ['empty']
	
	name = models.TextField()

	post = models.CharField(choices = posts,max_length=2, default=1)
	is_active=models.BooleanField(default=True)

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	# created_by = models.ForeignKey("self", on_delete=models.CASCADE)
	
	is_superuser = False
	is_admin = False
	is_staff = False
	is_anonymous = False
	is_authenticated = False

	created_on = datetime.datetime.now()

	# def __str__(self):
	# 	return str(self.uid)

	# def show_all(self):
	# 	context = {
	# 		"username" : self.username,
	# 		"password" : self.username
	# 	}
	# 	return context
	

