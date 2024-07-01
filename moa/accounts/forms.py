from django import forms
from django.contrib.auth import get_user_model # this imports CustomUser -- looks to the AUTH_USER_MODEL config in settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit, HTML, Div



class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(
        	label="email", max_length=30, required=True, widget=forms.TextInput(), 
			help_text="Use your institution email for verification purposes. The system does NOT store your raw email address."
    	)
	username = forms.CharField(
		label="username", max_length=30, required=True, widget=forms.TextInput(), 
		help_text="This will be your default username shown to other users. You can set different usernames per discussion."
	)
	
	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"username",
			"password1",
			"password2",
		)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Fieldset(
				"",
				Field("email"),
				Field("username"),
				Field("password1"),
				Field("password2"),
			)
		)

class CustomUserChangeForm(UserChangeForm):
	email = forms.EmailField(
        	label="email", max_length=30, required=True, widget=forms.TextInput(), 
			help_text="Use your institution email for verification purposes. The system does NOT store your raw email address."
    	)
	username = forms.CharField(
		label="username", max_length=30, required=True, widget=forms.TextInput(), 
		help_text="This will be your default username shown to other users. You can set different usernames per discussion."
	)

	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"username",
		)

# class RegisterForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

# class Meta:
# 	model = User
# 	#fields = ["username", "email", "password1", "password2"]
# 	username = forms.CharField()
# 	email = forms.EmailField()
# 	password1 = forms.CharField()
# 	password2 = forms.CharField()