from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import IntegerField, CharField, EmailField, TextField
import uuid

# Create your models here.
class Experience(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
				get_user_model(),
				on_delete=models.CASCADE,
		)
	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse("experience", args=[str(self.id)])
