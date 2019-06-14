from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return self.name
