from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	phd_year = models.IntegerField(null=True, blank=True)