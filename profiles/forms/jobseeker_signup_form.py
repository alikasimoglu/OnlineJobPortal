from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from profiles.models import Profile, JobSeeker, Skill


class JobSeekerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="İsim")
    last_name = forms.CharField(required=True, label="Soyisim")
    phone = forms.CharField(required=False, label="Telefon")
    country = forms.CharField(required=True, label="Ülke")
    city = forms.CharField(required=False, label="Şehir")
    avatar = forms.ImageField(required=False, label="Profil Resmi")
    profession_title = forms.CharField(required=True, label="Başlık/Uzmanlık Alanı")
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Beceriler"
    )
    short_resume = forms.CharField(widget=forms.Textarea, required=False, label="Kısa Özgeçmiş")
    cv_file = forms.FileField(required=False, label="CV")

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        jobseeker = JobSeeker.objects.create(profile=user)
        jobseeker.email = self.cleaned_data.get('email')
        jobseeker.first_name = self.cleaned_data.get('first_name')
        jobseeker.last_name = self.cleaned_data.get('last_name')
        jobseeker.phone = self.cleaned_data.get('phone')
        jobseeker.country = self.cleaned_data.get('country')
        jobseeker.city = self.cleaned_data.get('city')
        jobseeker.avatar = self.cleaned_data.get('avatar')
        jobseeker.profession_title = self.cleaned_data.get('profession_title')
        jobseeker.skills.add(*self.cleaned_data.get('skills'))
        jobseeker.short_resume = self.cleaned_data.get('short_resume')
        jobseeker.cv_file = self.cleaned_data.get('cv_file')
        jobseeker.slug = self.cleaned_data.get('slug')
        jobseeker.save()
        return user

