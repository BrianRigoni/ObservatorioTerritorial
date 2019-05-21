from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render


class SignInFormView(FormView):
    template_name = 'accounts/signin.html'
    success_url = reverse_lazy('Home')
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        return super(SignInFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(SignInFormView, self).form_valid(form)
