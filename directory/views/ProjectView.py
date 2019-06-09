from django.http import request
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from directory.models import Project, Researcher


class ProjectsListView(LoginRequiredMixin, ListView):
    login_url = 'SignIn'
    template_name = 'projects/project-list.html'
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        context_dict= {'projects': projects}
        return render(request, self.template_name, context=context_dict)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    login_url = 'SignIn'
    template_name = 'projects/project-form.html'
    success_url = 'projects/project-list.html'
    model = Project
    fields = ('name', 'description', 'background', 'responsible')

class ProjectDetailView(LoginRequiredMixin, DetailView):
    login_url = 'SignIn'
    template_name = 'projects/project-detail.html'
    model = Project

    def get_object(self):
        project = super().get_object()
        return project
