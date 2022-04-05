from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from profiles.forms import RecruiterSignUpForm
from profiles.models import Profile


class RecruiterSignUpView(CreateView):
    model = Profile
    form_class = RecruiterSignUpForm
    template_name = 'profiles/recruiter_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'recruiter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles:signup')
