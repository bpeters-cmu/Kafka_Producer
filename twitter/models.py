from django.db import models

# Create your models here.
class Topic(models.Model):
	twitter_data = models.CharField(max_length=255)
