from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

    def __str__(self):
        return self.name

