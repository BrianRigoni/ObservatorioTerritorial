from django.urls import path
from django.contrib import admin
from directory.views import HomeView, PublicationsListView, PublicationCreateView
from directory.views import ProjectView
from directory.views import UserView

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', UserView.SignUp.as_view(), name="SignUp"),
    path('ingreso/',  UserView.SignIn.as_view(), name='SignIn'),
    path('investigaciones/', ProjectView.ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectView.ProjectDetailView.as_view(), name="Project-Detail"),
    path('investigaciones/nueva', ProjectView.ProjectCreateView.as_view(), name="Project-Create"),
    path('publicaciones/', PublicationsListView.as_view(), name="Publication-List"),
    path('publicaciones/nueva', PublicationCreateView.as_view(), name="Publication-Create"),
]