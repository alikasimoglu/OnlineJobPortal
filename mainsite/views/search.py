from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic import ListView
from mainsite.models import Job


@method_decorator([login_required(login_url=reverse_lazy("profiles:login"))], name='dispatch')
class SearchResultsView(ListView):
    template_name = "mainsite/search_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            object_list = Job.objects.filter(
                Q(job_title__icontains=query) | Q(skills_req__skill_name__icontains=query)
            ).distinct()
            return object_list
