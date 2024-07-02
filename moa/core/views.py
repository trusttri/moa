from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note, Experience, Topic
import json
from .forms import NoteForm, AccountConsentBoundaryForm
import datetime
from uuid import UUID
from accounts.models import CustomUser


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)

def index(request):
	return render(request, "core/index.html")

# temporary code for learning channels
def room(request, room_name):
	return render(request, "chat/room.html", {"room_name": room_name})

@login_required
def write_seed_note(request):
	template_name = "write.html"

	author = request.user
	data = {'consent_form': AccountConsentBoundaryForm,
		 	'note_form': NoteForm,
			'phd_year': author.phd_year,
			'phd_year_boundary': author.phd_year_boundary,
			'international_student': author.international_student,
			'first_gen': author.first_gen,
			'other_info': author.other_info,
			'experience_tags': author.get_experiences(),
			'all_topic_tags': Topic.objects.all(),
	}

	# return render(request, template_name, {'tag_list': tag_list, 'identity_list': identity_list})
	return render(request, template_name, data)


def is_visible_to_user(note, user):
	phd_year_boundary = note.phd_year
	international_student = note.international_student
	first_gen = note.first_gen
	experience_tags = [ e.keyword for e in note.experiences.all() ]
	if phd_year_boundary:
		if str(user.phd_year) not in phd_year_boundary:
			return False
	if international_student and international_student is True:
		if user.is_international_student != international_student:
			return False
	if first_gen and first_gen is True:
		if user.is_first_gen != first_gen:
			return False
	if experience_tags:
		if not any(e in user.get_experiences() for e in experience_tags):
			return False
	return True

@login_required
def search_phd_students(note):
	author = note.author
	phd_year_boundary = note.phd_year_boundary
	international_student = note.international_student
	first_gen = note.first_gen
	experience_tags = [ e.keyword for e in note.experiences.all() ]
	students_to_notify = list()
	for student in CustomUser.objects.all():
		if student.author == author:
			continue
		if phd_year_boundary:
			if str(student.phd_year) not in phd_year_boundary:
				continue
		if international_student and international_student is True:
			if student.is_international_student != international_student:
				continue
		if first_gen and first_gen is True:
			if student.is_first_gen != first_gen:
				continue
		if experience_tags:
			if not any(e in student.get_experiences() for e in experience_tags):
				continue
		students_to_notify.append(student)
	return(students_to_notify)

@login_required
def notes(request):
	note_list = Note.objects.filter(level=0).order_by('created_at')
	template_name = "notes.html"
	return render(request, template_name, {'note_list': note_list})


@login_required
def note(request):
	n_id = request.GET.get('id')
	seed_note = Note.objects.filter(id=n_id)[0]
	if request.user.is_superuser or is_visible_to_user(seed_note, request.user):
		experience_tag_list = Experience.objects.all()
		branch_notes_candidates = Note.objects.filter(seed_note=seed_note).order_by('created_at')
		branch_notes = []
		if request.user.is_superuser:
			branch_notes = branch_notes_candidates
		else:
			for branch_note in branch_notes_candidates:
				if is_visible_to_user(branch_note, request.user):
					branch_notes.append(branch_note)
		author = seed_note.author

		if seed_note.username_pseudo:
			username = seed_note.username_pseudo
		else:
			username = seed_note.author.username

		template_name = "note.html"
		data = {'seed_note': seed_note, 
				'branch_notes': branch_notes, 
				'note_form': NoteForm,
				'seed_note_id': n_id,
				'experience_tag_list': experience_tag_list,
				'phd_year': author.phd_year,
				'phd_year_boundary': author.phd_year_boundary,
				'international_student': author.international_student,
				'first_gen': author.first_gen,
				'username': username
				}
	else:
		template_name = "restricted.html"
		data = {'message': 'You do not have access to this note.'}

	return render(request, template_name, data)

@login_required
def send_seed_note(request):
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		form = NoteForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# store the data
			title = form.cleaned_data["title"]
			description = form.cleaned_data["description"]
			print(title, description)
			n = Note.objects.create(title=title, text=description, author=request.user, level=0, created_at=datetime.datetime.now())
			n.phd_year = form.cleaned_data["phd_year"]
			n.other_info = form.cleaned_data["other_info"]
			n.international_student = form.cleaned_data["international_student"]
			n.first_gen = form.cleaned_data["first_gen"]
			n.username_pseudo = form.cleaned_data["username_pseudo"]
			advising_experience_tags = form.cleaned_data['experience_tags']
			topic_tags = form.cleaned_data['topic_tags']
			for e_id in advising_experience_tags:
				e = Experience.objects.get(choice_id=int(e_id))
				n.experiences.add(e)
			for t_id in topic_tags:
				t = Topic.objects.get(id=int(t_id))
				n.topics.add(t)
			n.save()
		else:
			for field in form:
				print("Field Error:", field.name,  field.errors)

			return redirect("/notes")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NoteForm()
	# return render(request, "write.html", {"form": form})
	return redirect("/notes")


def branch_note_view(request, note_id):
	note = Note.objects.get(id=note_id)
	render_result = render(request, 'branch_note.html', {'note': note})
	return render_result


@login_required
def send_note(request):
	data = 'Fail'
	if request.method == "POST":
		note_text = request.POST['note']
		note_seed_id = request.POST['seed_id']
		created_at = request.POST['created_at']
		parent_id = request.POST['parent_id']
		advising_experience_tags = []
		if request.POST['advising_experience'] != "":
			advising_experience_tags = request.POST['advising_experience'].split(",")
	
		n = Note.objects.create(text=note_text, author=request.user, created_at=datetime.datetime.now())
		n.seed_note = Note.objects.get(id=parent_id)
		n.level = n.seed_note.level + 1
		n.phd_year = request.POST['phd_year'].split(",")
		n.international_student = request.POST['international_student'] == 'true'
		n.first_gen = request.POST['first_gen'] == 'true'
		print("debugging")
		print(advising_experience_tags)
		for experience_tag in advising_experience_tags:
			e = Experience.objects.get(keyword=experience_tag)
			n.experiences.add(e)
		n.save()
		data = {'state': 'SUCCESS', 'noteID': str(n.id), 'parentID': str(parent_id)}
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
	print(json_data)
	return HttpResponse(json_data, content_type='application/json')


@login_required
def notifications(request):
	template_name = "notifications.html"
	return render(request, template_name)


@login_required
def notify_message(note):
	students_to_notify = search_phd_students(note)
# 	pass


@login_required
def account_consent_boundary(request):
	template_name = "account_consent_boundary.html"
	author = request.user
	data = {'consent_form': AccountConsentBoundaryForm,
			'phd_year': author.phd_year,
			'phd_year_boundary': author.phd_year_boundary,
			'international_student': author.international_student,
			'first_gen': author.first_gen,
			'other_info': author.other_info,
			'experience_tags': author.get_experiences(),
	}

	return render(request, template_name, data)


@login_required
def set_account_consent_boundary(request):
	if request.method == "POST":
		form = AccountConsentBoundaryForm(request.POST)
		if form.is_valid():
			print("---SET ACCOUNT CONSENT BOUNDARY---")
			print(form.cleaned_data)
			author = request.user
			author.username = form.cleaned_data["username"]
			author.phd_year_boundary = form.cleaned_data["phd_year"]
			author.other_info = form.cleaned_data["other_info"]
			author.international_student = form.cleaned_data["international_student"]
			author.first_gen = form.cleaned_data["first_gen"]

			advising_experience_tags = form.cleaned_data['experience_tags']
			for e_id in advising_experience_tags:
				e = Experience.objects.get(choice_id=int(e_id))
				author.experiences.add(e)

			author.save()
		else:
			for field in form:
				print("Field Error:", field.name,  field.errors)
		return redirect("/consent_boundary")
	else:
		form = AccountConsentBoundaryForm()
	return render(request, "account_consent_boundary.html", {"form": form})


