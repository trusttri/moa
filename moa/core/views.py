from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Experience, Tag, Identity
import json

def index(request):
	print("core")
	return render(request, "core/index.html")


def render_experience_write(request):
	template_name = "write.html"
	tag_list = Tag.objects.all()
	identity_list = Identity.objects.all()

	return render(request, template_name, {'tag_list': tag_list, 'identity_list': identity_list})


def experiences(request):
	experience_list = Experience.objects.all()
	template_name = "experiences.html"
	return render(request, template_name, {'experience_list': experience_list})


def submit_experience(request):
	# if request.is_ajax():
	title = request.GET.get('title', 'None')
	description = request.GET.get('description', 'None')
	print(title, description)
	e = Experience.objects.create(title=title, text=description, author=request.user)

	json_data = {'title': title, 'description': description}

	return HttpResponse(json_data, content_type='application/json')