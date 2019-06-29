from django.db import models
from .researcher import Researcher
from .publication import Publication


class Author(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='authorPublication')
    researcher  = models.ForeignKey(Researcher, on_delete=models.CASCADE, related_name='authorResearcher')
    order       = models.PositiveIntegerField()

    class Meta:
        verbose_name        = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.order} | {self.researcher}"
