from django.http import request
from django.shortcuts import render
from django.views.generic import DetailView
from directory.models import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project-detail.html'

    def get_object(self):
        project = super().get_object()
        return project
