from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Tag

# Create your models here.
class CustomUser(AbstractUser):
	phd_year = models.IntegerField(null=True, blank=True)
	# gender =
	# race =  
	# institution = 
	phd_year_boundary = models.JSONField(null=True, blank=True)
	international_student = models.BooleanField(null=True, blank=True)
	first_gen = models.BooleanField(null=True, blank=True)
	other_info = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(null=True, blank=True)
	experience_tags = models.ManyToManyField(Tag)

	def get_experience_tags(self):
		return "\n".join([t.keyword for t in self.experience_tags.all()])