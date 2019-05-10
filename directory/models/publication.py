from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date = models.CharField(max_length=100, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.name
