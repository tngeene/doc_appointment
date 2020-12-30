from django.urls import path

from ..views.patients import  PatientCreateView,PatientDetailView, PatientListView

app_name = "patients"

urlpatterns = [
    path('all/', PatientListView.as_view(), name='patients_list'),
    path('add/', PatientCreateView.as_view(), name='patient_add'),
    path('<int:pk>/details/', PatientDetailView.as_view(), name='patient_details'),
]