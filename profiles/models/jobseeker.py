from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose
from profiles.models.skills import Skill
from django.utils.text import slugify
from django.urls import reverse


class JobSeeker(models.Model):
    is_active = models.BooleanField("Durum (Aktif/Pasif)", default=True)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Kullanıcı", primary_key=True)
    email = models.EmailField("Email Adresi", unique=True)
    first_name = models.CharField("İsim", max_length=50)
    last_name = models.CharField("Soyisim", max_length=50)
    phone = models.CharField("Telefon", max_length=15, help_text="Zorunlu alan değildir.", blank=True, null=True)
    country = models.CharField("Ülke", max_length=50)
    city = models.CharField("Şehir", max_length=50)
    avatar = models.ImageField("Profil Resmi", upload_to='img/avatars/', help_text="Zorunlu alan değildir.", blank=True, null=True)
    avatar_thumbnail_500x500 = ImageSpecField(source='avatar', processors=[Transpose(), ResizeToFill(500, 500)], format='WEBP', options={'quality': 80})
    avatar_thumbnail_100x100 = ImageSpecField(source='avatar', processors=[Transpose(), ResizeToFill(100, 100)], format='WEBP', options={'quality': 80})
    profession_title = models.CharField("Başlık/Uzmanlık Alanı", help_text="Ör: Django Geliştirici", max_length=200)
    skills = models.ManyToManyField(Skill, verbose_name="Beceri Adı", related_name="profiles")
    short_resume = models.TextField("Kısa Özgeçmiş", max_length=500, help_text="Kısa özgeçmiş alanı zorunlu değildir.", blank=True, null=True)
    cv_file = models.FileField("CV", upload_to='cv_files/', help_text='Desteklenen Dosya Formatı: pdf, doc, docx', blank=True, null=True,
                               validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])
    slug = models.SlugField("Slug", help_text="Bu alan otomatik olarak oluşturulmaktadır.", max_length=60, unique=True, allow_unicode=True)
    updated = models.DateTimeField("Güncellenme Tarihi", auto_now=True)
    date_joined = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.pk) + "-" + str(self.first_name) + "-" + str(self.last_name))
        super(JobSeeker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:jobseeker-detail', args=[self.slug])

    class Meta:
        verbose_name_plural = "Kullanıcılar"
        verbose_name = "Kullanıcı"
        ordering = ("-date_joined",)
