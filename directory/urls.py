from django.conf import settings
from django.urls import path
from django.contrib import admin
from directory.views import (SignInView, SignUpView, LogoutView, 
    LockscreenView, ProfileView, HomeView, 
    ProjectCreateView, ProjectDetailView, ProjectsListView, ProjectDownloadView,
    PublicationsListView, PublicationCreateView, PublicationDeleteView, PublicationUpdateView)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', SignUpView.as_view(), name="SignUp"),
    path('ingreso/',  SignInView.as_view(), name='SignIn'),
    path('logout/',  LogoutView.as_view(), name='Logout'),
    path('reingreso/',  LockscreenView.as_view(), name='Lockscreen'),
    path('perfil/',  ProfileView.as_view(), name='Profile'),
    path('investigaciones/', ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectDetailView.as_view(), name="Project-Detail"),
    path('investigacionespdf/<int:pk>', ProjectDownloadView.as_view(), name="Project-Info-Download"),
    path('publicaciones/', PublicationsListView.as_view(), name="Publication-List"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)