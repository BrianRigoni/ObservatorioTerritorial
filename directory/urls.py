from django.urls import path
from django.contrib import admin
from directory.views import SignUpCreateView, SignInFormView, HomeView, ProjectsListView, ProjectDetailView, \
    ProjectCreateView, PublicationsListView, PublicationCreateView


urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', SignUpCreateView.as_view(), name="SignUp"),
    path('iniciodesesion/',  SignInFormView.as_view(), name='SignIn'),
    path('investigaciones/', ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectDetailView.as_view(), name="Project-Detail"),
    path('investigaciones/nueva', ProjectCreateView.as_view(), name="Project-Create"),
    path('publicaciones/', PublicationsListView.as_view(), name="Publication-List"),
    path('publicaciones/nueva', PublicationCreateView.as_view(), name="Publication-Create"),
]