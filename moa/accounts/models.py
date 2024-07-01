from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Experience

# Create your models here.
class CustomUser(AbstractUser):
	phd_year = models.IntegerField(null=True, blank=True)
	# gender =
	# race =  
	# institution = 
	phd_year = models.IntegerField(null=True, blank=True)
	is_international_student = models.BooleanField(null=True, blank=True)
	is_first_gen = models.BooleanField(null=True, blank=True)

	phd_year_boundary = models.JSONField(null=True, blank=True)
	international_student = models.BooleanField(null=True, blank=True)
	first_gen = models.BooleanField(null=True, blank=True)
	other_info = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(null=True, blank=True)
	experiences = models.ManyToManyField(Experience)

	def get_experiences(self):
		return "\n".join([t.keyword for t in self.experiences.all()])