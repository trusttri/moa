from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Experience, Tag, Identity
import json
from .forms import ExperienceForm

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
def experience(request):
	e_id = request.GET.get('id')
	print(e_id)
	experience = Experience.objects.filter(id=e_id)[0]
	print(experience.title)
	print(experience)
	template_name = "experience.html"

	return render(request, template_name, {'experience': experience})


@login_required
def submit_experience(request):
	print("get name function")
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		print("here")
		# create a form instance and populate it with data from the request:
		form = ExperienceForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# store the data
			title = form.cleaned_data["title"]
			description = form.cleaned_data["description"]
			print(title, description)
			e = Experience.objects.create(title=title, text=description, author=request.user)
			e.save()
			return redirect("/experiences")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ExperienceForm()
	return render(request, "write.html", {"form": form})