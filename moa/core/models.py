from django.db import models
from django.db.models import IntegerField, CharField, EmailField, TextField
import uuid

# Create your models here.
class User(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	stored_at = models.DateTimeField(null=False)
	email = models.EmailField(max_length=254)
	password = models.TextField()