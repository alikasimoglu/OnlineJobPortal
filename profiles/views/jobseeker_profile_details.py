from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from profiles.models import user_is_jobseeker, JobSeeker


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_jobseeker], name='dispatch')
class JobSeekerProfileView(DetailView):
    model = JobSeeker
    context_object_name = "jobseeker"
    template_name = 'profiles/jobseeker_profile_detail.html'

    def get_object(self):
        return self.request.user.jobseeker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
