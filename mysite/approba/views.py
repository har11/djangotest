from django.views import generic
from approba.models import Machine, MachineForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

class IndexView(generic.TemplateView):
	template_name = 'approba/index.html'

class machinelist(generic.ListView):
	template_name = 'approba/machinelist.html'
	context_object_name = 'machine_list'
	
	def get_queryset(self):
		return Machine.objects.filter(created_by=self.request.user)
	

@login_required (login_url='/approba/login')
def newmachine(request):
	"""Add new machine"""
	if request.method == 'POST':
		form = MachineForm(request.POST)
		
		if form.is_valid():
			p = form.save(commit=False)
			p.created_by = request.user
			p.updated_by = p.created_by

			try:
				p.save()
			except IntegrityError:
				form.errors["machine_name"] = ["You cannot register more machines with same name"]
			else:
				return HttpResponseRedirect(reverse('approba:machinelist'))
	else:
		form = MachineForm()
	return render(request,'approba/newmachine.html',{'form': form},)

@login_required (login_url='/approba/login')
def editmachine(request, machine_id):
	machine = get_object_or_404(Machine,pk=machine_id)
	
	machine.updated_at = datetime.datetime.now()
	if request.POST:
		form = MachineForm(request.POST, instance=machine)
	
		if form.is_valid():
			p = form.save(commit=False)
			p.updated_by = request.user
			
		try:		
			p.save()
		except IntegrityError:
			form.errors["machine_name"] = ["You cannot register more machines with same name"]			

			#In case of edit this extra row was needed for the validation comparing with the validation of the create form. I do not know why yet.
			return render(request,'approba/editmachine.html',{'form': form},)
		else:		
			return HttpResponseRedirect(reverse('approba:machinelist'))
	else:
		form = MachineForm(instance=machine)	
		return render(request,'approba/editmachine.html',{'form': form},)

@login_required (login_url='/approba/login')		
def deletemachine(request, machine_id):
	machine = get_object_or_404(Machine,pk=machine_id)
	machine.delete()
	return HttpResponseRedirect(reverse('approba:machinelist'))
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('approba:index'))
	 # Redirect to a success page.
	 