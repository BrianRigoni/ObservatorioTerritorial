from django.contrib import admin
from .models import Institution, Project, Publication, Researcher, Author, Genre
# Register your models here.

admin.site.register(Institution)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Researcher)
admin.site.register(Author)
admin.site.register(Genre)
