from django.contrib import admin
from .models import Institute, Project, Publication, Researcher, University, Authors, Genre
# Register your models here.

admin.site.register(Institute)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Researcher)
admin.site.register(University)
admin.site.register(Authors)
admin.site.register(Genre)
