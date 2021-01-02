from django.contrib.auth import get_user_model
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from core.models import Appointment

from ..utils import send_welcome_email
from .index import DashboardView

User = get_user_model()


class DoctorCreateView(DashboardView, CreateView):
    model = User
    template_name = 'dashboard/users/doctors/add.html'
    fields = ('first_name', 'last_name', 'email',
              'phone_number', 'gender', 'department', 'id_no', 'staff_id', )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        random_password = get_random_string()
        user = form.save(commit=False)
        user.email = form.instance.email.lower()
        user.username = user.email
        user.set_password(random_password)
        user.role = 'doctor'
        user.save()

        send_welcome_email(user, random_password, self.request)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:doctors:doctor_details', kwargs={'pk': self.object.pk})


class DoctorListView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/users/doctors/list.html'
    queryset = User.objects.filter(role='doctor')


class DoctorDetailView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/doctors/details.html'

    def get_context_data(self, **kwargs):
        user_id = self.object.id
        user = User.objects.get(id=user_id)
        context = super().get_context_data(**kwargs)
        context["all_appointments"] = Appointment.objects.filter(
            doctor=user_id)
        context["pending_appointments"] = Appointment.objects.filter(
            doctor=user_id, status='pending')
        context["confirmed_appointments"] = Appointment.objects.filter(
            doctor=user_id, status='confirmed')
        context["declined_appointments"] = Appointment.objects.filter(
            doctor=user_id, status='declined')
        context["events_attending"] = user.events_attending.all().order_by('-pk')
        return context
