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


def signup(request):
	template_name = "account/signup.html"
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, template_name)


class ConfirmEmailPageView(generic.CreateView):
	success_url = reverse_lazy("account_consent_boundary")
