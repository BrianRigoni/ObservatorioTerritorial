from django.contrib.auth import login, authenticate, logout
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from directory.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from directory.models import Researcher


class SignIn(FormView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('Home')
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        return super(SignIn, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(SignIn, self).form_valid(form)


class SignUp(CreateView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('Home')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = SignUpForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            names = form.cleaned_data.get('names')
            surnames = form.cleaned_data.get('surnames')
            user = User.objects.create_user(username, email, raw_password)
            # asi como se crea el usuario, este es un investigador
            investigator = Researcher.objects.create(names=names, surnames=surnames, email=email, user= user)
            investigator.save()
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home')
        else:
            return self.form_invalid(form)

