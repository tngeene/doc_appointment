from core.models import Appointment, Event
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from rest_framework.views import APIView
from users.models import Department
from rest_framework.response import Response
from core.mixins import CSRFExemptMixin

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


class EventDetailPage(DetailView):
    template_name = 'main/events/details.html'
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all().exclude(id=self.object.id)[0:6]
        return context


class BookEventAttendanceAPIView(APIView):
    authentication_classes = (CSRFExemptMixin, )
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        action = data['action']
        event = get_object_or_404(Event, id=data['event'])

        if action == 'attending':
            event.attendees.add(user)
        else:
            event.attendees.remove(user)
        event.save()

        return Response({'detail': 'Event succesfully update'})
