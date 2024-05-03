from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Experience, Tag, Identity
import json
from .forms import NameForm

def index(request):
	print("core")
	return render(request, "core/index.html")

@login_required
def experience_write(request):
	template_name = "write.html"
	tag_list = Tag.objects.all()
	identity_list = Identity.objects.all()

	return render(request, template_name, {'tag_list': tag_list, 'identity_list': identity_list})

@login_required
def experiences(request):
	print('experiences page')
	experience_list = Experience.objects.all()
	template_name = "experiences.html"
	return render(request, template_name, {'experience_list': experience_list})

@login_required
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
		messages.success(request, "Experience is sent to those who meet your consent boundary criteria.", extra_tags='alert')
		return redirect("experiences")		
	
	return HttpResponse(request, "write.html")


@login_required
def experience(request):
	e_id = request.GET.get('id')
	print(e_id)
	experience = Experience.objects.filter(id=e_id)[0]
	print(experience.title)
	print(experience)
	template_name = "experience.html"

	return render(request, template_name, {'experience': experience})

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
	print("get name function")
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# store the data
			name = form.cleaned_data["your_name"]
			e = Experience.objects.create(title=name, text=name, author=request.user)
			e.save()
			messages.success(request, "Experience is sent to those who meet your consent boundary criteria.", extra_tags='alert')
			return redirect("/experiences")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
	return render(request, "write.html", {"form": form})