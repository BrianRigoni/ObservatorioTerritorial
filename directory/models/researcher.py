from django.db import models
from django.contrib.auth.models import User
from .institution import Institution

class Researcher(models.Model):
    user            = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    surnames        = models.CharField(max_length=100, null=False, blank=False)
    names           = models.CharField(max_length=100, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.png')
    institution     = models.ForeignKey(Institution, null=True, blank=True, on_delete=models.DO_NOTHING)
    occupation      = models.CharField(max_length=100, null=True, blank=True)
    location        = models.CharField(max_length=100, null=True, blank=True)
    education       = models.TextField(max_length=200, null=True, blank=True)
    skills          = models.TextField(max_length=200, null=True, blank=True)
    notes           = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name        = "Investigador"
        verbose_name_plural = "Investigadores"

    def __str__(self):
        return f"{self.surnames}, {self.names}"



