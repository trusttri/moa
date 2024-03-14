
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)

		if form.is_valid():
			pass
		else:
			form = RegisterForm()
	return render(response, "register/register.html", {"form":form})


def index(request):
	return render(request, "register/register.html")