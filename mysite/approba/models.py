from django.db import models
import datetime
from django import forms
import django.contrib.auth.models

class Machine(models.Model):
	machine_name = models.CharField(max_length=100)
	machine_description = models.CharField(max_length=1000)
	created_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	created_by = models.ForeignKey(django.contrib.auth.models.User,related_name='user_created_by')
	updated_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	updated_by = models.ForeignKey(django.contrib.auth.models.User,related_name='user_updated_by')
	
	class Meta:
		unique_together = ("machine_name", "created_by")
	
class MachineForm(forms.ModelForm):
	machine_name = forms.CharField(max_length=100)
	machine_description = forms.CharField(max_length=1000)
	
	class Meta:
		model = Machine
		fields = ['machine_name','machine_description']
		
class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(),min_length=8, max_length=30)
	password_repeat = forms.CharField(widget=forms.PasswordInput(),max_length=30)
	class Meta:
		model = django.contrib.auth.models.User
		fields = ['username','first_name','last_name','email','password']
		
	#test
	def password_match(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password_repeat')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError(_("The two password fields didn't match."))
		return password1
	#/test
	
class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	class Meta:
		model = django.contrib.auth.models.User
		fields = ['first_name','last_name','email']

class PasswordChangeForm(forms.ModuleForm):
	old_password = forms.CharField(widget=forms.PasswordInput(),min_length=8, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(),min_length=8, max_length=30)
	password_repeat = forms.CharField(widget=forms.PasswordInput(),max_length=30)
	class Meta:
		model = django.contrib.auth.models.User
		fields = ['password']
		
	#Using example from http://stackoverflow.com/questions/3226197/why-is-checking-if-two-passwords-match-in-django-so-complicated
	def password_match(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password_repeat')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError(_("The two password fields didn't match."))
		return password1

