from django.db import models
from profiles.models import JobSeeker


class AppliedJobs(models.Model):
    job = models.ForeignKey('mainsite.Job', on_delete=models.CASCADE, verbose_name="İş İlanı", related_name='applied_jobs')
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name="İş Arayan Profili", related_name='applied_user')
    date_applied = models.DateTimeField("Başvuru Tarihi", auto_now_add=True)

    def __str__(self):
        return self.job.job_title

    class Meta:
        verbose_name_plural = "Başvurulan İş İlanları"
        verbose_name = "İş İlanına Başvur"
        ordering = ("-date_applied",)
