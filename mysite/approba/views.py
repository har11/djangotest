from django.views import generic
from approba.models import Machine, MachineForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
	template_name = 'approba/index.html'
	context_object_name = 'machine_list'
	
	def get_queryset(self):
		return Machine.objects.all()

@login_required (login_url='/approba/login')
def newmachine(request):
	"""Add new machine"""
	if request.method == 'POST':
		form = MachineForm(request.POST)
		
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return HttpResponseRedirect(reverse('approba:index'))
	else:
		form = MachineForm()
	return render(request,'approba/newmachine.html',{'form': form},)

def editmachine(request, machine_id):
	machine = get_object_or_404(Machine,pk=machine_id)
	machine.updated_at = datetime.datetime.now()
	if request.POST:
		form = MachineForm(request.POST, instance=machine)
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return HttpResponseRedirect(reverse('approba:index'))
	else:
		form = MachineForm(instance=machine)	
		return render(request,'approba/editmachine.html',{'form': form},)
		
def deletemachine(request, machine_id):
	machine = get_object_or_404(Machine,pk=machine_id)
	machine.delete()
	return HttpResponseRedirect(reverse('approba:index'))
	
def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect(reverse('approba:index'))
			 # Redirect to a success page.
		else:
			# Return a 'disabled account' error message
			pass
	else:
		 # Return an 'invalid login' error message.
		 pass
			
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('approba:index'))
	 # Redirect to a success page.