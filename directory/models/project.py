from django.db import models
from .researcher import Researcher


class Project(models.Model):
    name = models.CharField(max_length= 200, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    background = models.TextField(max_length=1000, null=True)
    responsible = models.ForeignKey(Researcher, on_delete=models.DO_NOTHING, related_name='responsability')
    researchers = models.ManyToManyField(Researcher, through='Author')

    class Meta:
        verbose_name = "Investigación"
        verbose_name_plural = "Investigaciones"

    def __str__(self):
        return self.name
