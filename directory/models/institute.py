from django.db import models
from .university import University


class Institute(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
