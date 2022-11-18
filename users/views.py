from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
	"""Log out user"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
	"""Registers a new user."""
	if request.method != 'POST':
		# Display blank registration form
		form = UserCreationForm()
	else:
		# Process the completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Logs in the user and redirects him to the home page
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)
