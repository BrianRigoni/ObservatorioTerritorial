from django import forms
from directory.models import Publication 


class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication 
        fields = ('name', 'date', 'genre', 'document', 'authors', 'project')

class PublicationUpdateForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'date', 'genre', 'authors', 'project')
