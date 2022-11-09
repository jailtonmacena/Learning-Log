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


	# Page to add a new subject
	re_path(r'^new_topic/$', views.new_topic, name='new_topic'),


	# Page for add a new entry
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
