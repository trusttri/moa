from django import forms

class ExperienceForm(forms.Form):
    title = forms.CharField(label="experience title", max_length=200)
    description = forms.CharField(label="experience description", widget=forms.Textarea)

    phd_year = forms.IntegerField()

    international_student = forms.BooleanField(
        widget=forms.CheckboxInput,
        label="who is an international student",
        required=False,
        initial=False
    )

    first_gen = forms.BooleanField(
        widget=forms.CheckboxInput,
        label="who is an first-gen student",
        required=False,
        initial=False
    )

    other_info = forms.CharField()


class AccountConsentBoundaryForm(forms.Form):
    phd_year = forms.IntegerField()

    international_student = forms.BooleanField(
        widget=forms.CheckboxInput,
        label="who is an international student",
        required=False,
        initial=False
    )

    first_gen = forms.BooleanField(
        widget=forms.CheckboxInput,
        label="who is an first-gen student",
        required=False,
        initial=False
    )

    other_info = forms.CharField()

    
    