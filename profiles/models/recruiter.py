from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose
from django.utils.text import slugify
from django.urls import reverse


class Recruiter(models.Model):
    is_active = models.BooleanField("Durum (Aktif/Pasif)", default=True)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Kullanıcı", primary_key=True)
    email = models.EmailField("Email Adresi", unique=True)
    first_name = models.CharField("İsim", max_length=50)
    last_name = models.CharField("Soyisim", max_length=50)
    phone = models.CharField("Telefon", max_length=15)
    country = models.CharField("Ülke", max_length=50)
    avatar = models.ImageField("Profil Resmi", upload_to='img/avatars/', help_text="Zorunlu alan değildir.", blank=True, null=True)
    avatar_thumbnail_500x500 = ImageSpecField(source='avatar', processors=[Transpose(), ResizeToFill(500, 500)], format='WEBP', options={'quality': 80})
    avatar_thumbnail_100x100 = ImageSpecField(source='avatar', processors=[Transpose(), ResizeToFill(100, 100)], format='WEBP', options={'quality': 80})
    profession_title = models.CharField("Başlık/Uzmanlık Alanı", help_text="Ör: İnsan Kaynakları Uzmanı", max_length=200)
    company = models.CharField("Firma", max_length=100)
    slug = models.SlugField("Slug", help_text="Bu alan otomatik olarak oluşturulmaktadır.", max_length=60, unique=True)
    updated = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + self.last_name)
        super(Recruiter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:recruiter', args=[self.slug])

    class Meta:
        verbose_name_plural = "İK Uzmanları"
        verbose_name = "İK Uzmanı"
        ordering = ("-date_joined",)
