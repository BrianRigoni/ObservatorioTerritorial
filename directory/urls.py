from django.urls import path
from directory.views import HomeView, ProjectsListView, ProjectDetailView, SignUpFormView, SignInFormView


urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('registro/', SignUpFormView.as_view(), name="SignUp"),
    path('iniciodesesion/',  SignInFormView.as_view(), name='SignIn'),
    path('investigaciones/', ProjectsListView.as_view(), name="Projects-List"),
    path('investigaciones/<int:pk>/', ProjectDetailView.as_view(), name="Project-Detail")
]