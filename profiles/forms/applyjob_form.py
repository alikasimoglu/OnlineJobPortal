from django import forms
from mainsite.models.applicants import Applicants


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicants
        fields = ("job",)
