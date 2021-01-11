from rest_framework.serializers import ModelSerializer
from .models import Appointment

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ('confirmed_by',)