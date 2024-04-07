from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import IntegerField, CharField, EmailField, TextField
import uuid

class Tag(models.Model):
	keyword = models.CharField(max_length=100)
	explanation = models.TextField(blank=True)
	
	class Meta:
		ordering = ["keyword"]

	def __str__(self):
		return self.keyword

class Identity(models.Model):
	category = models.CharField(max_length=100)
	explanation = models.TextField(blank=True)
	
	class Meta:
		ordering = ["category"]

	def __str__(self):
		return self.category
		
class Experience(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
				get_user_model(),
				on_delete=models.CASCADE,
		)
	text = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag) 
	identites = models.ManyToManyField(Identity)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse("experience", args=[str(self.id)])

