from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note, Tag
import json
from .forms import NoteForm, AccountConsentBoundaryForm
import datetime

def index(request):
	return render(request, "core/index.html")

# temporary code for learning channels
def room(request, room_name):
	return render(request, "chat/room.html", {"room_name": room_name})

@login_required
def write_seed_note(request):
	template_name = "write.html"
	tag_list = Tag.objects.all()

	author = request.user
	data = {'consent_form': AccountConsentBoundaryForm,
			'phd_year': author.phd_year,
			'phd_year_boundary': author.phd_year_boundary,
			'international_student': author.international_student,
			'first_gen': author.first_gen,
			'other_info': author.other_info,
			'tag_list': tag_list
	}

	# return render(request, template_name, {'tag_list': tag_list, 'identity_list': identity_list})
	return render(request, template_name, data)

@login_required
def notifications(request):
	template_name = "notifications.html"
	return render(request, template_name)

@login_required
def notes(request):
	note_list = Note.objects.filter(level=0).order_by('created_at')
	template_name = "notes.html"
	return render(request, template_name, {'note_list': note_list})


@login_required
def note(request):
	n_id = request.GET.get('id')
	print(n_id)
	seed_note = Note.objects.filter(id=n_id)[0]
	branch_notes = Note.objects.filter(seed_note=seed_note).order_by('created_at')
	template_name = "note.html"
	data = {'seed_note': seed_note, 
			'branch_notes': branch_notes, 
			'note_form': NoteForm,
			'conversation_name': n_id
			}

	return render(request, template_name, data)


@login_required
def send_seed_note(request):
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		print("here")
		# create a form instance and populate it with data from the request:
		form = NoteForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# store the data
			title = form.cleaned_data["title"]
			description = form.cleaned_data["description"]
			print(title, description)
			e = Note.objects.create(title=title, text=description, author=request.user, level=0, created_at=datetime.datetime.now())
			e.phd_year_boundary = form.cleaned_data["phd_year"]
			e.other_info = form.cleaned_data["other_info"]
			e.international_student = form.cleaned_data["international_student"]
			e.first_gen = form.cleaned_data["first_gen"]
			e.save()
		else:
			for field in form:
				print("Field Error:", field.name,  field.errors)

			return redirect("/notes")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NoteForm()
	# return render(request, "write.html", {"form": form})
	return redirect("/notes")



@login_required
def send_note(request):
	data = 'Fail'
	if request.method == "POST":
		note_text = request.POST['note']
		note_seed_id = request.POST['seed_id']
		created_at = request.POST['created_at']
		n = Note.objects.create(text=note_text, author=request.user, created_at=datetime.datetime.now())
		n.seed_note = Note.objects.get(id=note_seed_id)
		n.level = n.seed_note.level + 1
		n.save()
		data = {'state': 'SUCCESS', 'result': 'Successfully stored.'}
		# form = NoteForm(request.POST)
		# if form.is_valid():
		# 	description = form.cleaned_data["description"]
		# 	n = Note.objects.create(text=description, author=request.user, is_seed_note=False)
		# 	n.phd_year_boundary = form.cleaned_data["phd_year"]
		# 	n.international_student = form.cleaned_data["international_student"]
		# 	n.first_gen = form.cleaned_data["first_gen"]
		# 	n.seed_note = Note.objects.get(id=n_id)
		# 	n.save()
		# 	data = {'state': 'SUCCESS', 'result': 'Successfully stored.'}
		# else:
		# 	for field in form:
		# 		print("Field Error:", field.name,  field.errors)
		# 		data = {'state': 'ERROR', 'result': 'Error in field.'}
	else:
		form = NoteForm()
		
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

# @login_required
# def search_phd_students(notes):
# 	pass

# @login_required
# def send_message(notes):
# 	search_phd_students(notes)
# 	pass

@login_required
def account_consent_boundary(request):
	template_name = "consent_boundary.html"
	author = request.user
	tag_list = Tag.objects.all()
	data = {'consent_form': AccountConsentBoundaryForm,
			'phd_year': author.phd_year,
			'phd_year_boundary': author.phd_year_boundary,
			'international_student': author.international_student,
			'first_gen': author.first_gen,
			'other_info': author.other_info,
			'tag_list': tag_list,

	}

	return render(request, template_name, data)

@login_required
def set_account_consent_boundary(request):
	if request.method == "POST":
		form = AccountConsentBoundaryForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			author = request.user
			author.phd_year_boundary = form.cleaned_data["phd_year"]
			author.other_info = form.cleaned_data["other_info"]
			author.international_student = form.cleaned_data["international_student"]
			author.first_gen = form.cleaned_data["first_gen"]

			author.save()
			return redirect("/consent_boundary")
	else:
		form = AccountConsentBoundaryForm()
	return render(request, "consent_boundary.html", {"form": form})


