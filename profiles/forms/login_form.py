from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from profiles.models import Profile, JobSeeker, Skill
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields["username"].widget.attrs.update({"placeholder": "Kullanıcı Adınız"})
        self.fields["password"].widget.attrs.update({"placeholder": "Şifreniz"})

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username=username, password=password)

            if self.user is None:
                raise forms.ValidationError("Böyle bir kullanıcı bulunmamaktadır.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Bu kullanıcı için girdiğiniz şifre uyuşmuyor.")
            if not self.user.is_active:
                raise forms.ValidationError("Kullanıcı aktif değil")
        return super(LoginForm, forms).clean(*args, **kwargs)

    def get_user(self):
        return self.user

