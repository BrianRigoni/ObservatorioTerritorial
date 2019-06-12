from django.contrib.auth.mixins import LoginRequiredMixin
from directory.models import Publication
from django.views.generic import CreateView, ListView, View
from directory.models import Publication, Author, Researcher, Genre, Project
from django.shortcuts import render


class PublicationCreateView(LoginRequiredMixin, CreateView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publication-create.html'
    fields = ['name', 'date', 'genre', 'document', 'project']

    def get(self, request, *args, **kwargs):
        researchers = Researcher.objects.all()
        genres = Genre.objects.all()
        projects = Project.objects.all() # luego filtrar solo por las que participa el usuario
        context_dict = {'researchers': researchers, 'genres': genres, 'projects': projects}
        return render(request, self.template_name, context=context_dict)


class PublicationsListView(LoginRequiredMixin, ListView):
    login_url = 'SignIn'
    model = Publication
    template_name = 'publications/publication-list.html'

    def get(self, request, *args, **kwargs):
        publications = Publication.objects.all()
        context_dict = {'publications': publications}
        return render(request, self.template_name, context=context_dict)


class PublicationDownloadView(View):
    pass 
    # def download(request, path):
    # file_path = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
    # raise Http404
