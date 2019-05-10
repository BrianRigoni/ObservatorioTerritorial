from django.db import models
from .researcher import Researcher
from .publication import Publication


class Investigation(models.Model):
    name = models.CharField(max_length= 200, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    responsible = models.ForeignKey(Researcher, on_delete=models.DO_NOTHING, related_name='responsability')
    researchers = models.ManyToManyField(Researcher, related_name='investigation')
    publications = models.ForeignKey(Publication, on_delete=models.DO_NOTHING)
