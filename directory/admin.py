from django.contrib import admin
from .models import Institute, Investigation, Publication, Researcher, University
# Register your models here.

admin.site.register(Institute)
admin.site.register(Investigation)
admin.site.register(Publication)
admin.site.register(Researcher)
admin.site.register(University)
