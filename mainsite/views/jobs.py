from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from mainsite.models import Job


@method_decorator([login_required(login_url=reverse_lazy("profiles:login"))], name='dispatch')
class JobsView(ListView):
    model = Job
    template_name = "mainsite/jobs.html"
    context_object_name = "jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
