from core.models import Appointment, Event
from django.contrib.auth import get_user_model
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, DetailView, ListView

from ..utils import send_welcome_email
from ..views.index import DashboardView

User = get_user_model()


class PatientCreateView(DashboardView, CreateView):
    model = User
    template_name = 'dashboard/users/patients/add.html'
    fields = ('first_name', 'last_name', 'email',
              'phone_number', 'gender', 'id_no',)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        random_password = get_random_string()
        user = form.save(commit=False)
        user.email = form.instance.email.lower()
        user.username = user.email
        user.set_password(random_password)
        user.role = 'patient'
        user.save()

        send_welcome_email(user, random_password, self.request)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:patients:patient_details', kwargs={'pk': self.object.pk})


class PatientListView(DashboardView, ListView):
    model = User
    template_name = 'dashboard/users/patients/list.html'
    context_object_name = 'users'
    queryset = User.objects.filter(role='patient')


class PatientDetailView(DashboardView, DetailView):
    model = User
    template_name = 'dashboard/users/patients/details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        user_id = self.object.id
        user = User.objects.get(id=user_id)
        context = super().get_context_data(**kwargs)

        context["all_appointments"] = Appointment.objects.filter(
            patient=user_id)
        context["pending_appointments"] = Appointment.objects.filter(
            patient=user_id, status='pending')
        context["confirmed_appointments"] = Appointment.objects.filter(
            patient=user_id, status='confirmed')
        context["declined_appointments"] = Appointment.objects.filter(
            patient=user_id, status='declined')
        context["events_attending"] = user.events_attending.all().order_by('-pk')
        return context
