from django import forms

class ExperienceForm(forms.Form):
    title = forms.CharField(label="experience title", max_length=200)
    description = forms.CharField(label="experience description", widget=forms.Textarea)

class AccountConsentBoundaryForm(forms.Form):
	phd_year = forms.IntegerField()
	# gender = 
	# institution = 
	# advisor = 