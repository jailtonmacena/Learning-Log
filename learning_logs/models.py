from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	"""A subject the user is learning about."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Returns a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""something specific learned about a subject."""
	topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = 'entries'


	def __str__(self):
		"""Returns a string representation of the model."""
		text = self.text

		#Adding an ellipsis only if the input is longer than 50 characters 
		if text[:50] < text[:51]:
			return text[:51] + " ..."
		else:
			return text[:50]
