from django.db import models
from .genre import Genre
from .project import Project
from .researcher import Researcher
from django.contrib.auth.models import User

class Publication(models.Model):
    name     = models.CharField(max_length=100, null=False, blank=False)
    date     = models.CharField(max_length=100, null=False, blank=False)
    genre    = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    document = models.FileField(upload_to='publicaciones')
    authors  = models.ManyToManyField(Researcher, through='Author', related_name='publicationAuthor')
    project  = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name='publicationProject')
    created_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name        = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.name
