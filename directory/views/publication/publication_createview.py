from django.views.generic import CreateView
from directory.models import Publication


class PublicationCreateView(CreateView):
    model = Publication
    template_name = 'publications/publication-create.html'
    fields = ['name', 'date', 'genre', 'document', 'project']

