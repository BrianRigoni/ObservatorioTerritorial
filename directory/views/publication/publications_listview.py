from django.views.generic import ListView
from directory.models import Publication
from django.shortcuts import render


class PublicationsListView(ListView):
    model = Publication
    template_name = 'publications/publication-list.html'

    def get(self, request, *args, **kwargs):
        publications = Publication.objects.all()
        context_dict = {'publications': publications}
        return render(request, self.template_name, context=context_dict)


