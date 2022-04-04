from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    is_jobseeker = models.BooleanField('Kullanıcı mı?', default=False)
    is_recruiter = models.BooleanField('IK Uzmanı mı?', default=False)

    class Meta:
        verbose_name_plural = "Profiller"
        verbose_name = "Profil"

