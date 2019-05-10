from django.db import models
from django.contrib.auth.models import User
from .institute import Institute

class Researcher(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    surnames = models.CharField(max_length=100, null=False, blank=False)
    names = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    institute = models.ForeignKey(Institute, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.surnames}, {self.names}"



