from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from mainsite.models.applicants import Applicants
from profiles.forms import ApplyJobForm
from django.contrib import messages
from profiles.models import JobSeeker, user_is_jobseeker


@login_required(login_url=reverse_lazy('profiles:login'))
@user_is_jobseeker
def apply_job_view(request, job_id):
    form = ApplyJobForm(request.POST or None)
    user = get_object_or_404(JobSeeker, profile_id=request.user.id)
    applicant = Applicants.objects.filter(applicant__profile=user, job=job_id)

    if not applicant:
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.applicant = user
                instance.save()
                messages.success(
                    request, 'İlana başarıyla başvuru yaptınız!')
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request, 'Bu ilana zaten başvurmuştunuz!')
        return redirect(request.META.get("HTTP_REFERER"))
