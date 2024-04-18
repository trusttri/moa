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
	title = request.GET.get('title')
	description = request.GET.get('description')
	tags = request.GET.get('tags')
	data = {}

	if title != '' and description != '':
		e = Experience.objects.create(title=title, text=description, author=request.user)

		tags = json.loads(tags)
		for tag in tags:
			t = Tag.objects.filter(keyword=tag)[0]
			e.tags.add(t)
			e.save()

		data = {'id': e.id}
		json_data = json.dumps(data)
		print(json_data)

	return HttpResponse(json_data, content_type='application/json')

# def select_experience_tag(request):
# 	return HttpResponse({}, content_type='application/json')