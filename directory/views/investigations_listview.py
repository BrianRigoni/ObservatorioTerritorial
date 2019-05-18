from django.http import request
from django.shortcuts import render
from directory.models import Investigation
from django.views.generic import ListView


class InvestigationsListView(ListView):
    template_name = 'investigations-list.html'
    model = Investigation

    def get(self, request, *args, **kwargs):
        investigations = Investigation.objects.all()
        context = {'investigations': investigations}
        return render(request, self.template_name, context=context)


