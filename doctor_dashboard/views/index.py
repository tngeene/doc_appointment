from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from core.models import Appointment, Event
from users.models import Department
User = get_user_model()

class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if  user.role == 'doctor':
            return True
        return False

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'doctor-dashboard/index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        appointments = Appointment.objects.filter(doctor=user)
        context = super().get_context_data(**kwargs)
        context["appointments_count"] = appointments.count()
        context["pending_appointments_count"] = appointments.filter(status='pending').count()
        context["declined_appointments_count"] = appointments.filter(status='declined').count()
        context["confirmed_appointments_count"] = appointments.filter(status='confirmed').count()
        context["events_count"] = user.events_attending.count()
        context["recent_appointments"] = appointments.order_by('-pk')[:10]
        context["recent_events"] = user.events_attending.order_by('-pk')[:10]
        return context



