from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import messages



# Create your views here.
class SignupPageView(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy("login")
	template_name = "registration/signup.html"
# def accounts(response):
# 	if response.method == "POST":
# 		form = CustomUserCreationForm(response.POST)
# 	elif response.method == "GET":
# 		form = CustomUserCreationForm(response.GET)

# 	if form.is_valid():
# 		user = User.objects.create(stored_at=timezone.now(), 
# 			email = form.cleaned_data['email'], 
# 			password = make_password(form.cleaned_data['password']))

# 		# login(request, user, backend=None)
# 		return redirect(reverse("main"), {"form":form})
# 	else:
# 		form = CustomUserCreationForm()
# 		return render(response, "accounts/register.html", {"form":form})
