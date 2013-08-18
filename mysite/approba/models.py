from django.db import models
import datetime
from django import forms

class Machine(models.Model):
	machine_name = models.CharField(max_length=100, unique=True)
	machine_description = models.CharField(max_length=1000)
	created_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	updated_at = models.DateTimeField(editable=False, default=datetime.datetime.now)
	
class MachineForm(forms.ModelForm):
	machine_name = forms.CharField(max_length=100)
	machine_description = forms.CharField(max_length=1000)
	class Meta:
		model = Machine
		fields = ['machine_name','machine_description']