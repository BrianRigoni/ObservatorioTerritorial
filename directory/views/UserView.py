from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.base import RedirectView, TemplateView 
from django.views.generic.detail import DetailView

from directory.forms import SignUpForm, ProfileUpdateForm
from directory.models import Researcher, Institution

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

class SignInView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next',None)
        if next_url:
            return next_url
        else:
            return reverse('Home')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()

        return super(SignInView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            print("Cookies habilitadas!")
            """ response.set_cookie('username', user.username) """
        
        login(self.request, user) 
        self.request.session.set_expiry(300)
        return super(SignInView, self).form_valid(form)

    """ def render_to_response(self, context, **response_kwargs):
        response = super(LoginView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('', 'title')
        return response """


class SignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('Home')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            names = form.cleaned_data.get('names')
            surnames = form.cleaned_data.get('surnames')
            user = User.objects.create_user(username, email, raw_password)
            investigator = Researcher.objects.create(names=names, surnames=surnames, user= user)
            investigator.save()
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('Home')
        else:
            return self.form_invalid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = 'SignIn'
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "accounts/profile.html"

    def get_object(self):
        object = get_object_or_404(User, username=self.kwargs.get("username"))
        researcher = Researcher.objects.get(user=object)

        return researcher

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'SignIn'
    model = Researcher
    template_name = 'accounts/profile-update.html'
    form_class = ProfileUpdateForm
    
    def get(self, request, pk):
        researcher = Researcher.objects.get(pk=pk)
        institutions = Institution.objects.all()

        context_dict = {'researcher':researcher, 'institutions': institutions}
        return render(request, self.template_name, context=context_dict)

    def post(self, request, pk):
        form = ProfileUpdateForm(request.POST)

        if form.is_valid():
            researcher  = Researcher.objects.get(pk=pk)

            researcher.names       = form.cleaned_data.get('names')
            researcher.surnames    = form.cleaned_data.get('surnames')
            researcher.institution = form.cleaned_data.get('institution')
            researcher.occupation  = form.cleaned_data.get('occupation')
            researcher.user.email  = form.cleaned_data.get('email')
            researcher.location    = form.cleaned_data.get('location')
            researcher.education   = form.cleaned_data.get('education')
            researcher.skills      = form.cleaned_data.get('skills')
            researcher.notes       = form.cleaned_data.get('notes')

            researcher.save()
            return redirect('Home')
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    pattern_name = "Home"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LockscreenView(TemplateView):
    template_name = "accounts/lockscreen.html"
