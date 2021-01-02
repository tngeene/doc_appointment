from core.models import Appointment
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from users.models import Department

User = get_user_model()


# index view
class HomePageTemplateView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = User.objects.filter(role='doctor')
        doctors_count = doctors.count()
        doctors = doctors[0:5]
        context['departments'] = Department.objects.all()
        context['doctors'] = doctors
        context['doctors_count'] = doctors_count
        return context

# user Profile page


class UserProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context["all_appointments"] = Appointment.objects.filter(
            patient=user)
        context["pending_appointments"] = Appointment.objects.filter(
            patient=user, status='pending')
        context["confirmed_appointments"] = Appointment.objects.filter(
            patient=user, status='confirmed')
        context["declined_appointments"] = Appointment.objects.filter(
            patient=user, status='declined')
        context["events_attending"] = user.events_attending.all().order_by('-pk')
        return context
