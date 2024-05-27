from django import forms

class ExperienceForm(forms.Form):
    title = forms.CharField(label="experience title", max_length=200)
    description = forms.CharField(label="experience description", widget=forms.Textarea)

class AccountConsentBoundaryForm(forms.Form):
    phd_year = forms.IntegerField()

    INTERNATIONAL_STUDENT_CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    international_student = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=INTERNATIONAL_STUDENT_CHOICES, 
        label="Who is an international student",
    )

    FIRST_GEN_CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    first_gen = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=FIRST_GEN_CHOICES, 
        label="Who is an first-gen student",
    )

    other_info = forms.CharField()

    
    # gender = 
    # institution = 
    # advisor = 