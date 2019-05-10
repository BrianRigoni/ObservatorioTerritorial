from django.db import models
from .institute import Institute


class University(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

