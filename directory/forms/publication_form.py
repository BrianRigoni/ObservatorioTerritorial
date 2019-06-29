from django import forms
from directory.models import Publication 


class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication 
        fields = ('name', 'date', 'genre', 'document', 'authors', 'project', 'created_by')

class PublicationUpdateForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'date', 'genre', 'authors', 'project', 'created_by')
