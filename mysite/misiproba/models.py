from django.db import models
from django.core.validators import validate_email
import datetime
from django import forms

class User(models.Model):
	"""It describes the end users of the application"""
	user_name = models.CharField(max_length=100, unique = True)
	user_email = models.EmailField(validators=[validate_email])
	user_first_name = models.CharField(max_length=50)
	user_last_name = models.CharField(max_length=50)
	created_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	updated_at = models.DateTimeField(editable=False, default=datetime.datetime.now)

class UserForm(forms.ModelForm):
	user_name = forms.CharField(max_length=100)
	user_email = forms.EmailField()
	user_first_name = forms.CharField(max_length=50)
	user_last_name = forms.CharField(max_length=50)
	class Meta:
		model = User
		fields = ['user_name','user_email','user_first_name','user_last_name']