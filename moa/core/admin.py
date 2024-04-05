from django.contrib import admin
from .models import Experience

# Register your models here.
class ExperienceInline(admin.TabularInline):
	model = Experience

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ("title", "author")

admin.site.register(Experience, ExperienceAdmin)