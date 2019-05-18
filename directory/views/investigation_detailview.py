from django.http import request
from django.shortcuts import render
from django.views.generic import DetailView
from directory.models import Investigation


class InvestigationDetailView(DetailView):
    model = Investigation
    template_name = 'investigation-detail.html'

    def get_object(self):
        investigation = super().get_object()
        return investigation
