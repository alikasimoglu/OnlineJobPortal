from django.db import models
from profiles.models.recruiter import Recruiter
from profiles.models.skills import Skill
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse


JOB_INSIGHT_CHOICES = (
    ('Tam Zamanlı', 'Tam Zamanlı'),
    ('Yarı Zamanlı', 'Yarı Zamanlı'),
    ('Uzaktan Tam Zamanlı', 'Uzaktan Tam Zamanlı'),
    ('Uzaktan Yarı Zamanlı', 'Uzaktan Yarı Zamanlı'),
    ('Hibrit', 'Hibrit'),
)


class Job(models.Model):
    is_active = models.BooleanField("Durum (Aktif/Pasif)", default=True)
    job_title = models.CharField(max_length=155)
    company = models.CharField("Firma", max_length=100)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.RESTRICT, related_name='jobs')
    location = models.CharField(max_length=100)
    skills_req = models.ManyToManyField(Skill, verbose_name="İstenilen Beceriler")
    job_insight = models.CharField("Çalışma Şekli", max_length=30, choices=JOB_INSIGHT_CHOICES, default='Full Time', null=True)
    description = RichTextUploadingField("İş Açıklaması")
    slug = models.SlugField("Slug", help_text="Bu alan otomatik olarak oluşturulmaktadır.", max_length=60, unique=True, allow_unicode=True)
    updated = models.DateTimeField("Güncellenme Tarihi", auto_now=True)
    date_added = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)

    def __str__(self):
        return self.job_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.pk) + "-" + str(self.job_title))
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mainsite:jobs-detail', args=[self.slug])

    class Meta:
        verbose_name_plural = "İşler"
        verbose_name = "İş"
        ordering = ("-updated",)
