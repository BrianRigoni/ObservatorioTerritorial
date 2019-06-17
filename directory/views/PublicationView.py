from django.contrib.auth.mixins import LoginRequiredMixin
from directory.models import Publication
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from directory.models import Publication, Author, Researcher, Genre, Project
from django.shortcuts import render, redirect
from directory.forms import PublicationForm


class PublicationList(LoginRequiredMixin, ListView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publications.html'
    context_object_name = 'publications'

    def get(self, request, *args, **kwargs):
        researchers = Researcher.objects.all()
        genres      = Genre.objects.all()
        projects    = Project.objects.all() # luego filtrar solo por las que participa el usuario
        publications = Publication.objects.all()

        context_dict = {'researchers': researchers, 'genres': genres, 
                        'projects': projects, 'publications': publications}
        return render(request, self.template_name, context=context_dict)


class PublicationCreate(LoginRequiredMixin, CreateView):
    login_url = 'SignIn'
    template_name = 'publications/publication.html'
    form_class = PublicationForm
    success_url = 'publication_list'

    def get(self, request, *args, **kwargs):
        researchers = Researcher.objects.all()
        genres      = Genre.objects.all()
        projects    = Project.objects.all() # luego filtrar solo por las que participa el usuario

        context_dict = {'researchers': researchers, 'genres': genres, 'projects': projects}
        return render(request, self.template_name, context=context_dict)

    def post(self, request, *args, **kwargs):
        form    = PublicationForm(request.POST, request.FILES)
        authors = request.POST.getlist('authors')

        if form.is_valid():
            name     = form.cleaned_data.get('name')
            date     = form.cleaned_data.get('date')
            genre    = form.cleaned_data.get('genre')
            document = form.cleaned_data.get('document')
            project  = form.cleaned_data.get('project')

            publication = Publication.objects.create(name=name, date=date, genre=genre, document=document, project=project)

            i = 1
            for author in authors:
                researcher = Researcher.objects.get(pk=author)
                publication.authors.add(researcher, through_defaults={'order': i})
                i += 1
            
            return redirect('publication_list')
        else:
            form = PublicationForm()
        return render(request, self.template_name, {'form': form})


class PublicationUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publication.html'
    form_class = PublicationForm
    success_url = 'publication_list'


""" class PublicationDelete(LoginRequiredMixin, DeleteView):
    login_url = 'SignIn'
    model = Publication """
