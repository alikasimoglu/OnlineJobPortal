from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "profiles/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
