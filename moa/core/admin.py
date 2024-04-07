from django.contrib import admin
from .models import Experience, Tag

# Register your models here.
class ExperienceInline(admin.TabularInline):
	model = Experience

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ("title", "author")

admin.site.register(Experience, ExperienceAdmin)

class TagInline(admin.TabularInline):
	model = Tag

class TagAdmin(admin.ModelAdmin):
	list_display = ("keyword", "explanation")

admin.site.register(Tag, TagAdmin)