from django import forms
from directory.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ('name', 'description', 'background', 'responsible', 'members')
