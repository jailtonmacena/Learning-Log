"""Defines URL patterns for learning_logs."""


from django.urls import path, re_path


from . import views


app_name = 'learning_logs'
urlpatterns = [
	# Initial page
	re_path(r'^$', views.index, name='index'),


	# Show all subjects
	re_path(r'^topics/$', views.topics, name='topics'),


	# Details page for a single subject
	re_path(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),
]
