from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .mixins import CSRFExemptMixin
from .models import Appointment
from .serializers import AppointmentSerializer


# Create your views here.
class AppointMentCreateAPIView(CSRFExemptMixin, CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny, ]
