# Create your views here.

from django.http import HttpResponseRedirect #HttpResponse, Http404 - commented out introducing generic view 
#from django.template import RequestContext, loader
#instead of this above:
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
#Introducing with generic views
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'
	
	def get_queryset(self):
		"""Return the last five published polls"""
		#return Poll.objects.order_by('-pub_date')[:5]
		return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'
	def get_queryset(self):
		"""
		Excludes any polls that aren't published yet.
		"""
		return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
    	selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    	# Redisplay the poll voting form.
    	return render(request, 'polls/detail.html',{
    	'poll':p,
    	'error_message':'You did not select a choice'
    	})
    else:
    	selected_choice.votes += 1
    	selected_choice.save() 
    	# Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
    	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))  	          	
	    #return HttpResponse("You're voting on poll %s." % poll_id)


# Before introducing generic view we used it for index

#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    context = {'latest_poll_list': latest_poll_list}    
#    return render(request,'polls/index.html',context)	
	 
	#These are outdated with importing render	 
	#latest_poll_list = Poll.objects.order_by('-pub_date')[:5]        
   #template = loader.get_template('polls/index.html')
   #context = RequestContext(request, {'latest_poll_list': latest_poll_list,})
   #return HttpResponse(template.render(context))

    
	#It was just for writing out a raw output	
	#output = ', '.join([p.question for p in latest_poll_list])
	#return HttpResponse(output)
	
	#It was just the first step to write something	
	#return HttpResponse("Hello, world. You are at the poll index.")
	
# Before introducing generic view we used it for details
#def detail(request, poll_id):
#	#usage 404 with get_object_or_404
#	poll = get_object_or_404(Poll,pk=poll_id)	
#	
#	#Basic usage of 404
#	#try:
#	#	poll = Poll.objects.get(pk=poll_id)
#	#except Poll.DoesNotExist:
#	#	raise Http404	
#	return render(request,'polls/detail.html',{'poll':poll})
	  
    #Outdated with introducing 404 handling
    #return HttpResponse("You're looking at poll %s." % poll_id)

# Before introducing generic view we used it for result

#def results(request, poll_id):
#	poll = get_object_or_404(Poll, pk=poll_id)
#	return render(request, 'polls/results.html',{'poll':poll})  
#   #return HttpResponse("You're looking at the results of poll %s." % poll_id)

