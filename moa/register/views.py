
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.urls import reverse



# Create your views here.
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
	elif response.method == "GET":
		form = RegisterForm(response.GET)

	if form.is_valid():
		user = User.objects.create(stored_at=timezone.now(), 
			email = form.cleaned_data['email'], 
			password = make_password(form.cleaned_data['password']))
		context = {"email": user.email}
		# return HttpResponseRedirect("../core")
		print(context)
		return redirect(reverse("main"), context)
	else:
		form = RegisterForm()
		return render(response, "register/register.html", {"form":form})


def index(request):
	return render(request, "register/register.html")