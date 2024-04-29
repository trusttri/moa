from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import messages



# Create your views here.
class SignupPageView(generic.CreateView):
	print("testing!")
	form_class = CustomUserCreationForm
	success_url = reverse_lazy("account_consent_boundary")
	# template_name = "account/signup.html" # double check this

class ConfirmEmailPageView(generic.CreateView):
	print("testing...")
	success_url = reverse_lazy("account_consent_boundary")

def account_consent_boundary(request):
	template_name = "account/consent_boundary.html"
	print("test consent boundary page")
	return render(request, template_name, {})