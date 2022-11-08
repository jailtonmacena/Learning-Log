from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Topic
from .forms import TopicForm


def index(request):
	"""The home page of Learning Log"""
	return render(request, 'learning_logs/index.html')


def topics(request):
	"""Show all subjects"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	"""Shows a single subject and all of its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
	"""add a new subject."""
	if request.method != 'POST':
		# No data submitted; create blank form
		form = TopicForm()
	else:
		# Submitted POST data; process the data
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)
