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
		
class Note(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	author = models.ForeignKey(
				get_user_model(),
				on_delete=models.CASCADE,
		)
	title = models.CharField(max_length=200, null=True, blank=True)
	text = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag) 

	phd_year = models.IntegerField(null=True, blank=True)
	international_student = models.BooleanField(null=True, blank=True)
	first_gen = models.BooleanField(null=True, blank=True)
	other_info = models.TextField(null=True, blank=True)

	# reference = models.ManyToManyField('Note')
	seed_note = models.ForeignKey('Note', on_delete=models.CASCADE, null=True, blank=True)
	is_seed_note = models.BooleanField()


	def __str__(self):
		return self.text

	# def get_absolute_url(self):
	# 	return reverse("experience", args=[str(self.id)])