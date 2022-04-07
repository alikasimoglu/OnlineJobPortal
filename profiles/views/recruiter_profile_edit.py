from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from profiles.models import Recruiter, user_is_recruiter


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_recruiter], name='dispatch')
class RecruiterProfileUpdateView(UpdateView):
    model = Recruiter
    fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'avatar', 'profession_title',
              'company')
    context_object_name = "recruiter"
    template_name = 'profiles/recruiter_profile_edit.html'

    def form_valid(self, form):
        messages.success(self.request, 'İş arayan bilgileri başarıyla güncellendi!')
        return super().form_valid(form)
