from django.views.generic import CreateView
from django.shortcuts import render
from directory.models import Project


class ProjectCreateView(CreateView):
    template_name = 'projects/project-form.html'
    success_url = 'projects/project-list.html'
    model = Project
    fields = ('name', 'description', 'background', 'responsible')
