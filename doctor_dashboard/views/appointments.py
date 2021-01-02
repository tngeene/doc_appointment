from django.views.generic import ListView, DetailView
from core.models import Appointment
from .index import DashboardView

class AppointmentListView(DashboardView, ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'doctor-dashboard/appointments/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["all_appointments"] = user.appointments_requested.all().order_by("-pk")
        context["confirmed_appointments"] = user.appointments_requested.filter(status="confirmed").order_by("-pk")
        context["pending_appointments"] = user.appointments_requested.filter(status="pending").order_by("-pk")
        context["declined_appointments"] = user.appointments_requested.filter(status="declined").order_by("-pk")
        return context


class AppointmentDetailView(DashboardView, DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'doctor-dashboard/appointments/details.html'