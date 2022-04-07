from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from mainsite.models import Applicants
from profiles.models import user_is_recruiter


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_recruiter], name='dispatch')
class AppliedApplicantsView(ListView):
    model = Applicants
    template_name = "mainsite/applied_applicants.html"
    context_object_name = "applicants"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
