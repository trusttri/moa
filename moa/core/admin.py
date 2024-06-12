from django.contrib import admin
from .models import Note, Tag

# Register your models here.
class NoteInline(admin.TabularInline):
	model = Note

class NoteAdmin(admin.ModelAdmin):
	list_display = ("title", "text", "author")

admin.site.register(Note, NoteAdmin)

class TagInline(admin.TabularInline):
	model = Tag

class TagAdmin(admin.ModelAdmin):
	list_display = ("keyword", "explanation")

admin.site.register(Tag, TagAdmin)
