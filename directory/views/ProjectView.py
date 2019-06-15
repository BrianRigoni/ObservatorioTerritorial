from django.http import request, HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, View
from directory.models import Project, Researcher, Publication


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

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        publications = Publication.objects.filter(project=project)
        context_dict = {'project': project, 'publications': publications}
        return render(request, self.template_name, context=context_dict)


from reportlab.pdfgen import canvas 
from io import BytesIO 


class ProjectDownloadView(LoginRequiredMixin, View):
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







