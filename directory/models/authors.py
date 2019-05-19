from django.db import models
from .researcher import Researcher
from .project import Project


class Authors(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    researcher = models.ForeignKey(Researcher, on_delete=models.DO_NOTHING)
    order = models.PositiveIntegerField();
