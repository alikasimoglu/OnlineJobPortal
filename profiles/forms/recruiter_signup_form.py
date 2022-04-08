from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from profiles.models import Profile, Recruiter


class RecruiterSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="İsim")
    last_name = forms.CharField(required=True, label="Soyisim")
    phone = forms.CharField(required=False, label="Telefon")
    country = forms.CharField(required=True, label="Ülke")
    avatar = forms.ImageField(required=False, label="Profil Resmi")
    profession_title = forms.CharField(required=True, label="Başlık/Uzmanlık Alanı")
    company = forms.CharField(required=True, label="Firma")

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True
        user.save()
        recruiter = Recruiter.objects.create(profile=user)
        recruiter.email = self.cleaned_data.get('email')
        recruiter.first_name = self.cleaned_data.get('first_name')
        recruiter.last_name = self.cleaned_data.get('last_name')
        recruiter.phone = self.cleaned_data.get('phone')
        recruiter.country = self.cleaned_data.get('country')
        recruiter.avatar = self.cleaned_data.get('avatar')
        recruiter.profession_title = self.cleaned_data.get('profession_title')
        recruiter.company = self.cleaned_data.get('company')
        recruiter.slug = self.cleaned_data.get('slug')
        recruiter.save()
        return user
