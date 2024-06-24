from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import IntegerField, CharField, EmailField, TextField
import uuid

class Tag(models.Model):
	keyword = models.CharField(max_length=100)
	explanation = models.TextField(blank=True)
	created_at = models.DateTimeField(null=True, blank=True)
	
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
	experience_tags = models.ManyToManyField(Tag)
	created_at = models.DateTimeField(null=True, blank=True)

	phd_year = models.JSONField(null=True, blank=True)
	international_student = models.BooleanField(null=True, blank=True)
	first_gen = models.BooleanField(null=True, blank=True)
	other_info = models.TextField(null=True, blank=True)

	# reference = models.ManyToManyField('Note')
	seed_note = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
	level = models.IntegerField(default=0)


	def __str__(self):
		return self.text

	# def get_absolute_url(self):
	# 	return reverse("experience", args=[str(self.id)])