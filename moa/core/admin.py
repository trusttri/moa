from django.contrib import admin
from .models import Note, Experience, Topic

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

class TopicInline(admin.TabularInline):
	model = Topic

class TopicAdmin(admin.ModelAdmin):
	list_display = ("name", "description")

admin.site.register(Topic, TopicAdmin)
