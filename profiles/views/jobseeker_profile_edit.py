from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from profiles.models import user_is_jobseeker, JobSeeker


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_jobseeker], name='dispatch')
class JobSeekerProfileUpdateView(UpdateView):
    model = JobSeeker
    fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'city', 'avatar', 'profession_title',
              'skills', 'short_resume', 'cv_file')
    context_object_name = "jobseeker"
    template_name = 'profiles/jobseeker_profile_edit.html'

    def form_valid(self, form):
        messages.success(self.request, 'İş arayan bilgileri başarıyla güncellendi!')
        return super().form_valid(form)
