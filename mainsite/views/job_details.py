from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from mainsite.models import Job


@method_decorator([login_required(login_url=reverse_lazy("profiles:login"))], name='dispatch')
class JobDetailView(DetailView):
    model = Job
    template_name = 'mainsite/job_detail.html'
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
