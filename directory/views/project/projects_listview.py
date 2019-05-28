from django.http import request
from django.shortcuts import render
from directory.models import Project
from django.views.generic import ListView


class ProjectsListView(ListView):
    template_name = 'projects/projects-list.html'
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        context_dict= {'projects': projects}
        return render(request, self.template_name, context=context_dict)


