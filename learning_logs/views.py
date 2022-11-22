from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
	"""The home page of Learning Log"""
	return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
	"""Show all subjects"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
	"""Shows a single subject and all of its entries."""
	topic = Topic.objects.get(id=topic_id)
	# Ensures that the subject belongs to the current user
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


@login_required
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


@login_required
def new_entry(request, topic_id):
	"""Adds a new entry for a particular subject"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# No data submitted; create blank form
		form = EntryForm()
	else:
		# Submitted POST data; process the data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',
				args=[topic_id]))


	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# initial request; pre-populate the form with the current input
		form = EntryForm(instance=entry)
	else:
		# Submitted POST data; process the data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',
				args=[topic.id]))
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
