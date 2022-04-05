from django.db import models
from mainsite.models import Job
from profiles.models.jobseeker import JobSeeker


class Selected(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="İş İlanı", related_name='select_job')
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name="İş Arayan Profili", related_name='select_applicant')
    date_posted = models.DateTimeField("Başvuru Tarihi", auto_now_add=True)

    def __str__(self):
        return self.applicant

    class Meta:
        verbose_name_plural = "Seçilenler"
        verbose_name = "Birini Seç"
        ordering = ("-date_posted",)
