from core.utils import (mark_appointment_as_confirmed,
                        mark_appointment_as_declined)
from django.urls import path

from ..views.appointments import AppointmentDetailView, AppointmentListView

app_name = "appointments"

urlpatterns = [
    path('all/', AppointmentListView.as_view(), name="appointments_list"),
    path('<int:pk>/details', AppointmentDetailView.as_view(), name="appointment_details"),
    path('<int:pk>/mark-confirmed', mark_appointment_as_confirmed, name="appointment_mark_as_confirmed_action"),
    path('<int:pk>/mark-declined', mark_appointment_as_declined, name="appointment_mark_as_declined_action"),
]
