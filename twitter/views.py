from django.shortcuts import render
import tweepy
from twitter.forms import TopicForm
from django.http import HttpResponse, HttpResponseRedirect
from .twitter_handler import twitter_access

def index(request):
	form = TopicForm(request.POST)
	return render(request,'twitter/topic.html',{'form': form})
# Create your views here.
def process(request):
	
	if(request.method == 'POST'):
		form = TopicForm(request.POST)
		if form.is_valid():
			search_topic = form.cleaned_data['topic']
			twitter_instance = twitter_access()
			twitter_instance.get_stream(search_topic)
			return HttpResponse("Topic created successfully!!")
	else:
		return HttpResponse("Only POST is supported")

	return HttpResponse("Error")

