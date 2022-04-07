from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import TextInput
from mainsite.models import Job
from profiles.models import Skill


class JobCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label="İş Açıklaması")
    skills_req = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="İstenilen Beceriler"
        )

    class Meta:
        model = Job
        fields = ('job_title', 'company', 'recruiter', 'location', 'job_insight', 'skills_req', 'description')

        widgets = {
            'recruiter': TextInput(attrs={'readonly': 'readonly'}),
        }
