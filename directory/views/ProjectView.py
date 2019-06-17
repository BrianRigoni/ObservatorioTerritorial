from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View

from directory.models import Project, Researcher, Publication
from directory.forms.project_form import ProjectForm

from reportlab.pdfgen import canvas 
from io import BytesIO 


class ProjectList(LoginRequiredMixin, ListView):
    login_url = 'SignIn'
    template_name = 'projects/projects.html'
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        
        context_dict= {'projects': projects}
        return render(request, self.template_name, context=context_dict)


class ProjectCreate(LoginRequiredMixin, CreateView):
    login_url = 'SignIn'
    template_name = 'projects/project.html'
    form_class = ProjectForm
    success_url = 'project_list'

    def get(self, request, *args, **kwargs):
        researchers = Researcher.objects.all()
        
        context_dict= {'researchers': researchers}
        return render(request, self.template_name, context=context_dict)
    
    def post(self, request, *args, **kwargs):
        form    = ProjectForm(request.POST)
        members = request.POST.getlist('members')

        if form.is_valid():
            name     = form.cleaned_data.get('name')
            desc     = form.cleaned_data.get('description')
            backg    = form.cleaned_data.get('background')
            resp     = form.cleaned_data.get('responsible')

            project = Project.objects.create(name=name, description=desc, background=backg, responsible=resp)

            for memb in members:
                researcher = Researcher.objects.get(pk=memb)
                project.members.add(researcher)
            
            return redirect('project_list')
        else:
            form = ProjectForm()
        return render(request, self.template_name, {'form': form})

class ProjectDetail(LoginRequiredMixin, DetailView):
    login_url = 'SignIn'
    template_name = 'projects/project-detail.html'
    model = Project

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        publications = Publication.objects.filter(project=project)
        
        context_dict = {'project': project, 'publications': publications}
        return render(request, self.template_name, context=context_dict)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'SignIn'
    model = Project
    template_name = 'projects/project.html'
    form_class = ProjectForm
    success_url = 'project_list'


class ProjectDownload(LoginRequiredMixin, View):
    login_url = 'SignIn'

    def get(self, request, pk):
        project = Project.objects.get(pk=pk) # obtengo la publicacion sobre la cual se quiere descargar el pdf de la info
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{project.name}-autogenerado.pdf"'
        buffer = BytesIO()
        project_pdf = canvas.Canvas(buffer)
        project_pdf.setFont('Helvetica', 16)
        project_pdf.drawString(230, 1000, project.name) # titulo del pdf 
        project_pdf.setFont('Helvetica', 14) # cambio de fuente para el resto del pdf
        # subtitulos con la fuente helvetica 14  
        project_pdf.drawString(230, 960, "Antecedentes de la linea")
        project_pdf.drawString(230, 660, "Resumen de la linea")
        project_pdf.drawString(230, 460, "Miembros")
        # contenido de los subtitulos
        project_pdf.setFont('Helvetica', 12)
        # antecedentes
        project_pdf.drawString(150, 950, project.background)
        # resumen 
        project_pdf.drawString(150, 650, project.description)
        # miembros
        # y_members = 450
        # for researcher in project.researchers.all():
        #     project_pdf.drawString(150, y_members, researcher)
        #     y_members -= 15

        project_pdf.showPage()
        project_pdf.save()
        project_pdf = buffer.getvalue()
        buffer.close()
        response.write(project_pdf)
        return response







