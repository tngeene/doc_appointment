from django.urls import path
from ..views.index import DashboardTemplateView

app_name = "index"

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name="index")
]