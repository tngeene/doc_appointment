from django.urls import path

from ..views.doctors import DoctorCreateView, DoctorDetailView, DoctorListView

app_name = "doctors"

urlpatterns = [
    path('all/', DoctorListView.as_view(), name='doctors_list'),
    path('add/', DoctorCreateView.as_view(), name='doctor_add'),
    path('<int:pk>/details/', DoctorDetailView.as_view(), name='doctor_details'),
]