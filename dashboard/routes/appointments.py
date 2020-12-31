from django.urls import path
from ..views.appoinments import AppointmentListView, AppointmentDetailView

app_name = "appointments"

urlpatterns = [
    path('all/', AppointmentListView.as_view(), name="appointments_list"),
    path('<int:pk>/details', AppointmentDetailView.as_view(), name="appointment_details"),
]