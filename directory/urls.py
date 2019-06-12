from django.urls import path
from django.contrib import admin
from directory.views import (SignIn, SignUp, ProfileView, HomeView, ProjectCreateView, 
ProjectDetailView, ProjectsListView, PublicationsListView, PublicationCreateView)
from directory.views.UserView import logout_view

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', SignUp.as_view(), name="SignUp"),
    path('ingreso/',  SignIn.as_view(), name='SignIn'),
    path('logout/',  logout_view, name='Logout'),
    path('perfil/',  ProfileView.as_view(), name='Profile'),
    path('investigaciones/', ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectDetailView.as_view(), name="Project-Detail"),
    path('investigaciones/nueva', ProjectCreateView.as_view(), name="Project-Create"),
    path('publicaciones/', PublicationsListView.as_view(), name="Publication-List"),
    path('publicaciones/nueva', PublicationCreateView.as_view(), name="Publication-Create"),
]