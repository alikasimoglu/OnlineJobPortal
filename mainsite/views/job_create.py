from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from mainsite.forms import JobCreateForm
from mainsite.models import Job
from profiles.models import Recruiter, user_is_recruiter


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_recruiter], name='dispatch')
class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'mainsite/job_create_form.html'

    def get_initial(self):
        user = self.request.user
        initial = super(JobCreateView, self).get_initial()
        initial['recruiter'] = Recruiter.objects.get(profile=user)
        return initial

