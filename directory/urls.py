from django.conf import settings
from django.urls import path
from django.contrib import admin
from directory.views import (SignInView, SignUpView, LogoutView, 
    LockscreenView, ProfileView, HomeView, 
    ProjectCreate, ProjectDetail, ProjectUpdate, ProjectList, ProjectDownload, ProjectDelete,
    PublicationList, PublicationCreate, PublicationUpdate, PublicationDelete)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',                                  HomeView.as_view(),          name="Home"),
   
    path('registro/',                         SignUpView.as_view(),        name="SignUp"),
    path('ingreso/',                          SignInView.as_view(),        name='SignIn'),
    path('logout/',                           LogoutView.as_view(),        name='Logout'),
    path('reingreso/',                        LockscreenView.as_view(),    name='Lockscreen'),
    path('perfil/',                           ProfileView.as_view(),       name='Profile'),

    path('investigaciones/',                  ProjectList.as_view(),       name="project_list"),
    path('nueva_investigacion/',              ProjectCreate.as_view(),     name="project_create"),
    path('modificar_investigacion/<int:pk>/', ProjectUpdate.as_view(),     name="project_update"),
    path('eliminar_publicacion/<int:pk>/',    ProjectDelete.as_view(),     name="project_delete"),
    path('investigaciones/<int:pk>/',         ProjectDetail.as_view(),     name="project_detail"),
    path('investigacionespdf/<int:pk>',       ProjectDownload.as_view(),   name="Project-Info-Download"),
    
    path('publicaciones/',                    PublicationList.as_view(),   name="publication_list"),
    path('nueva_publicacion/',                PublicationCreate.as_view(), name="publication_create"),
    path('modificar_publicacion/<int:pk>/',   PublicationUpdate.as_view(), name="publication_update"),
    path('eliminar_publicacion/<int:pk>/',    PublicationDelete.as_view(), name="publication_delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)