from django.urls import path
from directory.views import HomeView, InvestigationsListView, InvestigationDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('investigaciones/', InvestigationsListView.as_view(), name="Investigations-List"),
    path('investigaciones/<int:pk>/', InvestigationDetailView.as_view(), name="Investigation-Detail")
]