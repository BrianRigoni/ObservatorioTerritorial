from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View

from directory.models import Project, Researcher, Publication
from directory.forms.project_form import ProjectForm

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
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

    def validate_project_data(self, value):
        if value:
            return value
        return "Sin información."

    def generate_pdf(self, project):
        pass

    def get(self, request, pk):
        # obtengo la publicacion sobre la cual se quiere descargar el pdf de la info
        project = Project.objects.get(pk=pk)
        publications = Publication.objects.filter(project=project)  # obtengo las publicaciones de la investigacion
        # declaro el tipo de contenido del response
        pdf_name = f'{project.name}-autogenerado.pdf'
        response = HttpResponse(content_type='application/pdf')
        # nombre del archivo que va a ser devuelto
        response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
        # documento
        buffer = BytesIO()
        pdf_doc = SimpleDocTemplate(buffer, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        # variables de la investigacion
        background = self.validate_project_data(project.background)
        description = self.validate_project_data(project.description)
        # members y publications son querysets, se evaluan luego para un for
        doc_content = []
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        normal_style = styles["Normal"]

        # secciones del pdf

        # titulo
        title = Paragraph(f'<font size="24">{project.name}</font>', title_style)
        doc_content.append(title)
        doc_content.append(Spacer(1, .7 * inch))

        # antecedentes de la linea
        background_subt = Paragraph('<font size="20">Antecedentes de la Línea</font>', title_style)
        doc_content.append(background_subt)
        background_text = Paragraph(f'<font size="14">{background}</font>', normal_style)
        doc_content.append(background_text)
        doc_content.append(Spacer(1, .5 * inch))

        # resumen de la linea
        description_subt = Paragraph('<font size="20">Resumen de la Línea</font>', title_style)
        doc_content.append(description_subt)
        description_text = Paragraph(f'<font size="14">{description}</font>', normal_style)
        doc_content.append(description_text)
        doc_content.append(Spacer(1, .5 * inch))

        # miembros
        members_subt = Paragraph('<font size="20">Miembros</font>', title_style)
        doc_content.append(members_subt)
        if project.researchers:
            for researcher in project.researchers.all():
                member_text = Paragraph(f'<font size="14"> - {researcher}</font>', normal_style)
                doc_content.append(member_text)
                doc_content.append(Spacer(1, .2 * inch))

        else:
            member_text = Paragraph('<font size="14"> No hay información de los miembros.</font>', normal_style)
            doc_content.append(member_text, normal_style)

        doc_content.append(Spacer(1, .5 * inch))

        # publicaciones
        publications_subt = Paragraph('<font size="20">Publicaciones</font>', title_style)
        doc_content.append(publications_subt)
        if publications:
            for publication in publications:
                publication_text = Paragraph(f'<font size="14"> - { publication }</font>', normal_style)
                doc_content.append(publication_text)
                doc_content.append(Spacer(1, .2 * inch))
        else:
            publication_text = Paragraph('<font size="14"> Sin publicaciones.</font>', normal_style)
            doc_content.append(publication_text)

        doc_content.append(Spacer(1, .5 * inch))

        # contenido del pdf finalizado, se devuelve al usuario
        pdf_doc.build(doc_content)
        response.write(buffer.getvalue())
        buffer.close()
        return response








