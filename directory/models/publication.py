from django.db import models
from .genre import Genre
from .project import Project
from .author import Author


class Publication(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date = models.CharField(max_length=100, null=False, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    document = models.FileField(upload_to='directory/publications_files')
    authors = models.ManyToManyField(Author)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.name
