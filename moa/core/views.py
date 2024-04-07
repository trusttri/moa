from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Experience, Tag, Identity
import json

def index(request):
	print("core")
	return render(request, "core/index.html")


def write_experience(request):
	template_name = "write.html"
	tag_list = Tag.objects.all()
	identity_list = Identity.objects.all()

	return render(request, template_name, {'tag_list': tag_list, 'identity_list': identity_list})

def experiences(request):
	experience_list = Experience.objects.all()
	template_name = "experiences.html"
	return render(request, template_name, {'experience_list': experience_list})