from django.views import generic
from misiproba.models import User, UserForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class IndexView(generic.ListView):
	template_name = 'misiproba/index.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		return User.objects.all()

def newuser(request):
	"""Add new user"""
	#return render(request,'misiproba/newuser.html')	#vegul a view adja vissza magat a html-t	
	if request.method == 'POST':
		form = UserForm(request.POST)
		
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return HttpResponseRedirect(reverse('misiproba:index'))
	else:
		form = UserForm()
	return render(request,'misiproba/newuser.html',{'form': form},)

def edituser(request, user_id):
	user = get_object_or_404(User,pk=user_id)
	if request.POST:
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return HttpResponseRedirect(reverse('misiproba:index'))
	else:
		form = UserForm(instance=user)	
		return render(request,'misiproba/edituser.html',{'form': form},)
		
def deleteuser(request, user_id):
	user = get_object_or_404(User,pk=user_id)
	user.delete()
	return HttpResponseRedirect(reverse('misiproba:index'))
	
	