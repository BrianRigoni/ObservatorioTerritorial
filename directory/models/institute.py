from django.db import models
from .university import University


class Institute(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING, related_name='institute')

    class Meta:
        verbose_name = "Instituto"
        verbose_name_plural = "Institutos"

    def __str__(self):
        return self.name
