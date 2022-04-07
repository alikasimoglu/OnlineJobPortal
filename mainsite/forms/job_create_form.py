from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import TextInput
from mainsite.models import Job


class JobCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Job
        fields = ('job_title', 'company', 'recruiter', 'location', 'job_insight', 'skills_req', 'description')

        widgets = {
            'recruiter': TextInput(attrs={'readonly': 'readonly'}),
        }
