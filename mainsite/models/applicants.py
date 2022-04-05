from django.db import models
from mainsite.models import Job
from profiles.models.jobseeker import JobSeeker


class Applicants(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="İş İlanı", related_name='applicants')
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name="İş Arayan Profili", related_name='applied')
    date_posted = models.DateTimeField("Başvuru Tarihi", auto_now_add=True)

    def __str__(self):
        return self.applicant

    class Meta:
        verbose_name_plural = "Başvuranlar"
        verbose_name = "Başvuru Ekle"
        ordering = ("-date_posted",)
