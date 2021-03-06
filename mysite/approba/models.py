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
	
	def __unicode__(self):
		return u'%s' % (self.machine_name)
        
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
	password = forms.CharField(widget=forms.PasswordInput(),min_length=1, max_length=30)
	password_repeat = forms.CharField(widget=forms.PasswordInput(),max_length=30)
	class Meta:
		model = django.contrib.auth.models.User
		fields = ['username','first_name','last_name','email','password']

	def password_fields_check(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password_repeat')
		if password1 and password2:
			if password1 != password2:
				self.errors["password"] = ["The 2 passwords do not match!"]
				return False
			else:
				return True
				
	def email_unique_check(self):
		email_input = self.cleaned_data.get('email')
		
		users = django.contrib.auth.models.User.objects.filter(email=email_input)
		if len(users) == 0:
			return True
		else:
			self.errors["email"] = ["This email is used by another user"]
			return False

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	class Meta:
		model = django.contrib.auth.models.User
		fields = ['first_name','last_name','email']

class AgroField(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	created_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	created_by = models.ForeignKey(django.contrib.auth.models.User,related_name='agrofield_created_by')
	# a related_name NEM a hivatkozott mezo neve, hanem az FK neve!!!
	updated_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	updated_by = models.ForeignKey(django.contrib.auth.models.User,related_name='agrofield_updated_by')
	
	class Meta:
		unique_together = ("name", "created_by")

	def __unicode__(self):
		return u'%s' % (self.name)

		
class AgroFieldForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	description = forms.CharField(max_length=1000)
	
	class Meta:
		model = AgroField
		fields = ['name','description']
		
class FieldOperation(models.Model):
	machine = models.ForeignKey(Machine, related_name = 'fieldoperation_machine')
	agrofield = models.ForeignKey(AgroField, related_name = 'fieldoperation_agrofield')
	operation = models.CharField(max_length=100)
	quantity = models.PositiveIntegerField()
	date = models.DateField()
	created_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	created_by = models.ForeignKey(django.contrib.auth.models.User,related_name='fieldoperation_created_by')
	updated_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	updated_by = models.ForeignKey(django.contrib.auth.models.User,related_name='fieldoperation_updated_by')
	
class FieldOperationForm(forms.ModelForm):
	operation = forms.CharField(max_length=100)
	quantity = forms.IntegerField(min_value=0)
	date = forms.DateField
	class Meta:
		model = FieldOperation
		fields = ['machine','agrofield','operation','quantity','date']
	
	#This is the way how we can filter for master data based on the user	
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(FieldOperationForm, self).__init__(*args, **kwargs)
		self.fields['machine'].queryset = Machine.objects.filter(created_by=user)
		self.fields['agrofield'].queryset = AgroField.objects.filter(created_by=user)
