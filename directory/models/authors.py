from django.db import models
from .researcher import Researcher
from .project import Project


class Authors(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    researcher = models.ForeignKey(Researcher, on_delete=models.DO_NOTHING)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.project + self.researcher + self.order