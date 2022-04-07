from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from profiles.forms import JobSeekerSignUpForm
from profiles.models import Profile


class JobSeekerSignUpView(CreateView):
    model = Profile
    form_class = JobSeekerSignUpForm
    template_name = 'profiles/jobseeker_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainsite:index')
