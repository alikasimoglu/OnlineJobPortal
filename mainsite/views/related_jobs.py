from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from mainsite.models import Job
from profiles.models import JobSeeker, user_is_jobseeker


@method_decorator([login_required(login_url=reverse_lazy("profiles:login")), user_is_jobseeker], name='dispatch')
class RelatedJobsView(ListView):
    model = Job
    template_name = "mainsite/related_jobs.html"
    context_object_name = "jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = JobSeeker.objects.get(profile_id=self.request.user.id)
        object_list = Job.objects.filter(skills_req__profiles__profile_id=user_obj.pk)
        context['related_jobs'] = object_list.distinct()
        return context
