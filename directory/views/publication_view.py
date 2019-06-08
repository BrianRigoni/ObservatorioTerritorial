from django.views.generic import CreateView, ListView, View
from directory.models import Publication, Author, Researcher
from django.shortcuts import render


class PublicationCreateView(CreateView):
    model = Publication
    template_name = 'publications/publication-create.html'
    fields = ['name', 'date', 'genre', 'document', 'project']

    def get(self, request, *args, **kwargs):
        researchers = Researcher.objects.all()
        context_dict = {'researchers': researchers}
        return render(request, self.template_name, context=context_dict)


class PublicationsListView(ListView):
    model = Publication
    template_name = 'publications/publication-list.html'

    def get(self, request, *args, **kwargs):
        publications = Publication.objects.all()
        context_dict = {'publications': publications}
        return render(request, self.template_name, context=context_dict)

    def post(self, request, *args, **kwargs):
        pass # TODO sobrescribir el metodo post para crear los registros de los autores con la publicacion


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
