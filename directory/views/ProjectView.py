from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import render
from django.http import request
from directory.models import Project


class ProjectsListView(ListView):
    template_name = 'projects/projects-list.html'
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        context_dict= {'projects': projects}
        return render(request, self.template_name, context=context_dict)


class ProjectCreateView(CreateView):
    template_name = 'projects/project-form.html'
    success_url = 'projects/project-list.html'
    model = Project
    fields = ('name', 'description', 'background', 'responsible')


class ProjectDetailView(DetailView):
    template_name = 'projects/project-detail.html'
    model = Project

    def get_object(self):
        project = super().get_object()
        return project
