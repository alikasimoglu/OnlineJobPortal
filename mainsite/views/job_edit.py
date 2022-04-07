from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from mainsite.models import Job
from profiles.models import user_is_jobseeker, JobSeeker


# @method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_jobseeker], name='dispatch')
class JobUpdateView(UpdateView):
    model = Job
    fields = ('job_title', 'company', 'job_insight', 'location', 'skills_req', 'description')
    context_object_name = "job"
    template_name = 'mainsite/job_edit.html'

    def form_valid(self, form):
        messages.success(self.request, 'İş ilanı bilgileri başarıyla güncellendi!')
        return super().form_valid(form)
