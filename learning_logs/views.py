from django.shortcuts import render


def index(request):
	"""The home page of Learning Log"""
	return render(request, 'learning_logs/index.html')
