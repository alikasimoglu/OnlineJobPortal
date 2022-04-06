from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from profiles.models import Recruiter, user_is_recruiter


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_recruiter], name='dispatch')
class RecruiterProfileView(DetailView):
    model = Recruiter
    context_object_name = "recruiter"
    template_name = 'profiles/recruiter_profile_detail.html'

    def get_object(self):
        return self.request.user.recruiter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
