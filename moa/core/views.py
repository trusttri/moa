from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.

def index(request):
	print("core")
	# email= body_decoded.get('email', 'None')
	# print(email)
	return render(request, "core/index.html")


def main(request):
	print("main")
	return render(request, "core/main.html")