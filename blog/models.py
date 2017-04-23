from django.db import models

class post(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField()
	pub_date = models.DateTimeField()

