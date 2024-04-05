from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Experience
import json

# Create your views here.

def index(request):
	print("core")
	# email= body_decoded.get('email', 'None')
	# print(email)
	return render(request, "core/index.html")


def main(request):
	print("main")
	print(request.POST.get('form'))
	if request.user.is_authenticated:
		print('hi')
	return render(request, "main.html")

def experiences(request):
	experience_list = Experience.objects.all()
	template_name = "experiences.html"
	return render(request, template_name, {'experience_list': experience_list})