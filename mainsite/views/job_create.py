from django.views.generic import CreateView
from mainsite.forms import JobCreateForm
from mainsite.models import Job
from profiles.models import Recruiter


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'mainsite/job_create_form.html'

    def get_initial(self):
        user = self.request.user
        initial = super(JobCreateView, self).get_initial()
        initial['recruiter'] = Recruiter.objects.get(profile=user)
        return initial

