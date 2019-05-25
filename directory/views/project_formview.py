from django.views.generic import FormView
from directory.forms import ProjectForm
from django.shortcuts import render


class ProjectFormView(FormView):
    form_class = ProjectForm
    template_name = 'projects/project-form.html'

    def get(self, request, *args, **kwargs):
        form = ProjectForm()
        context_dict = {'form': form}
        return render(request, self.template_name, context=context_dict)
