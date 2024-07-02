from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(
        label="experience title", 
        max_length=200, 
        required=False,
        initial=False
    )

    description = forms.CharField(label="experience description", widget=forms.Textarea)

    YEAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'), 
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]

    TOPIC_CHOICES= [
        (1, "credit issue"),
        (2, "fraud"),
        (3, "ghosting"),
        (4, "harassment"),
        (5, "microaggression"),
        (6, "micromanagement"),
        (7, "threat")   
    ]

    EXPERIENCE_CHOICES= [
        (1, "credit issue"),
        (2, "fraud"),
        (3, "ghosting"),
        (4, "harassment"),
        (5, "microaggression"),
        (6, "micromanagement"),
        (7, "threat")   
    ]

    topic_tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="Tag(s) for informing other users about the topic",
        choices=TOPIC_CHOICES,
        required=False,
        initial=False
    )

    phd_year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="who are in their X year in PhD (select from below)",
        choices=YEAR_CHOICES,
        required=False,
        initial=False
    )

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

    experience_tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="who have experienced the following (select from below)",
        choices=EXPERIENCE_CHOICES,
        required=False,
        initial=False
    )

    username_pseudo = forms.CharField(required=False, initial=False)

    other_info = forms.CharField(
        required=False,
        initial=False
    )

    reference_note = forms.CharField(required=False, initial=False)


class AccountConsentBoundaryForm(forms.Form):
    # phd_year = forms.IntegerField()

    YEAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'), 
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]

    EXPERIENCE_CHOICES= [
        (1, "credit issue"),
        (2, "fraud"),
        (3, "ghosting"),
        (4, "harassment"),
        (5, "microaggression"),
        (6, "micromanagement"),
        (7, "threat")   
    ]

    username = forms.CharField()

    phd_year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="who are in their X year in PhD (select from below)",
        choices=YEAR_CHOICES,
        required=False,
        initial=False
    )

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

    experience_tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="who have experienced the following (select from below)",
        choices=EXPERIENCE_CHOICES,
        required=False,
        initial=False
    )

    other_info = forms.CharField()

    
    