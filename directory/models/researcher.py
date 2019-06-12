from django.db import models
from django.contrib.auth.models import User
from .institute import Institute
from django.db.models.signals import post_save
from django.dispatch import receiver

class Researcher(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    surnames = models.CharField(max_length=100, null=False, blank=False)
    names = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    institute = models.ForeignKey(Institute, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Investigador"
        verbose_name_plural = "Investigadores"

    def __str__(self):
        return f"{self.surnames}, {self.names}"



