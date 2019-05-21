from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.urls import reverse_lazy
from directory.forms import SignUpForm
from django.shortcuts import render, redirect


class SignUpFormView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('SignIn')

    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                # login(request, user)
                # return redirect('Home')
                return redirect('SignIn')
        else:
            form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})
