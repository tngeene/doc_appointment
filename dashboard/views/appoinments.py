from django.views.generic import ListView, UpdateView, DetailView
from core.models import Appointment

from .index import DashboardView

class AppointmentListView(DashboardView, ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'dashboard/appointments/list.html'


class AppointmentDetailView(DashboardView, DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'dashboard/appointments/details.html'