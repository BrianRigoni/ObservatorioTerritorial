from django.urls import path
from django.contrib import admin
from directory.views import SignUpFormView, SignInFormView, HomeView, ProjectsListView, ProjectDetailView, \
    ProjectFormView


urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', SignUpFormView.as_view(), name="SignUp"),
    path('iniciodesesion/',  SignInFormView.as_view(), name='SignIn'),
    path('investigaciones/', ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectDetailView.as_view(), name="Project-Detail"),
    path('investigaciones/nueva', ProjectFormView.as_view(), name="Project-Form")
]