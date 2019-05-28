from django.views.generic import CreateView
from django.shortcuts import render
from directory.models import Project


class ProjectCreateView(CreateView):
    template_name = 'projects/project-form.html'
    model = Project
    success_url = 'projects/project-list.html'
    fields = ('name', 'description', 'background', 'responsible')
