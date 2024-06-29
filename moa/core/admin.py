from django.contrib import admin
from .models import Note, Experience

# Register your models here.
class NoteInline(admin.TabularInline):
	model = Note

class NoteAdmin(admin.ModelAdmin):
	list_display = ("title", "text", "author")

admin.site.register(Note, NoteAdmin)

class ExperienceInline(admin.TabularInline):
	model = Experience

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ("keyword", "explanation", "choice_id")

admin.site.register(Experience, ExperienceAdmin)
