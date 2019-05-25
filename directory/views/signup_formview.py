from django.contrib.auth import login, authenticate, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from directory.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class SignUpFormView(FormView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('Home')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

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
            user = User.objects.create_user(username, email, raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home')
        else:
            return self.form_invalid(form)

