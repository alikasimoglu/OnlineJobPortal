from django.db import models


class Skill(models.Model):
    skill_name = models.CharField("Beceri Adı", max_length=100)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = "Beceriler"
        verbose_name = "Beceri"
        ordering = ("skill_name", )
