from django.contrib.auth.mixins import LoginRequiredMixin
from directory.models import Publication
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from directory.models import Publication, Author, Researcher, Genre, Project
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from directory.forms import PublicationForm, PublicationUpdateForm
from django.contrib.auth.models import User

class PublicationList(LoginRequiredMixin, ListView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publications.html'
    context_object_name = 'publications'


class PublicationCreate(LoginRequiredMixin, CreateView):
    login_url = 'SignIn'
    template_name = 'publications/publication-create.html'
    form_class = PublicationForm
    success_url = reverse_lazy('publication_list')

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
            name          = form.cleaned_data.get('name')
            date          = form.cleaned_data.get('date')
            genre         = form.cleaned_data.get('genre')
            document      = form.cleaned_data.get('document')
            project       = form.cleaned_data.get('project')
            created_by    = form.cleaned_data.get('created_by')

            publication = Publication.objects.create(name=name, date=date, genre=genre, document=document, project=project, created_by=created_by)
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
    template_name = 'publications/publication-update.html'
    form_class = PublicationUpdateForm
    success_url = reverse_lazy('publication_list')

    def get(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        researchers = Researcher.objects.all()
        genres      = Genre.objects.all()
        projects    = Project.objects.all()
        context_dict = {'publication':publication, 'researchers': researchers, 'genres': genres, 'projects': projects}
        return render(request, self.template_name, context=context_dict)

    def post(self, request, pk):
        form    = PublicationUpdateForm(request.POST, request.FILES)
        authors = request.POST.getlist('authors')

        if form.is_valid():
            name          = form.cleaned_data.get('name')
            date          = form.cleaned_data.get('date')
            genre         = form.cleaned_data.get('genre')
            project       = form.cleaned_data.get('project')
            created_by    = User.objects.get(pk=form.cleaned_data.get('created_by'))
            publication             = Publication.objects.get(pk=pk)
            publication.name        = name
            publication.date        = date
            publication.genre       = genre
            publication.project     = project
            publication.created_by  = created_by
            publication.authors.clear()

            i = 1
            for author in authors:
                researcher = Researcher.objects.get(pk=author)
                publication.authors.add(researcher, through_defaults={'order': i})
                i += 1

            publication.save()
            return redirect('publication_list')
        else:
            form = PublicationForm()
        return render(request, self.template_name, {'form': form})


class PublicationDelete(LoginRequiredMixin, DeleteView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publication-delete.html'
    success_url = reverse_lazy('publication_list')
