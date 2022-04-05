from django.db import models
from profiles.models import JobSeeker


class SavedJobs(models.Model):
    job = models.ForeignKey('mainsite.Job', on_delete=models.CASCADE, verbose_name="İş İlanı", related_name='saved_jobs')
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name="İş Arayan Profili", related_name='saved')
    date_saved = models.DateTimeField("Eklenme Tarihi", auto_now_add=True)

    def __str__(self):
        return self.job.job_title

    class Meta:
        verbose_name_plural = "Kaydedilen İş İlanları"
        verbose_name = "İş İlanı Kaydet"
        ordering = ("-date_saved",)
