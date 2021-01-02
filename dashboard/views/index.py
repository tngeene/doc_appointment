from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from core.models import Appointment, Event
from users.models import Department
User = get_user_model()

class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == 'admin':
            return True
        return False

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        appointments = Appointment.objects.all()
        doctors = User.objects.filter(role='doctor')
        events = Event.objects.all()
        patients = User.objects.filter(role='patient')
        staff = User.objects.filter(role='staff')
        context = super().get_context_data(**kwargs)
        context["appointments_count"] = appointments.count()
        context["events_count"] = events.count()
        context["doctors_count"] = doctors.count()
        context["patients_count"] = patients.count()
        context["staff_count"] = staff.count()
        context["recent_appointments"] = appointments.order_by('-pk')[:10]
        context["recent_events"] = events.order_by('-pk')[:10]
        context["recent_staff"] = staff.order_by('-pk')[:10]
        context["recent_doctors"] = doctors.order_by('-pk')[:10]
        context["recent_patients"] = patients.order_by('-pk')[:10]
        return context


class UserConfirmSuspendView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'
