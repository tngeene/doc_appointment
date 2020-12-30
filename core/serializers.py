from rest_framework.serializers import ModelSerializer
from .models import Appointment

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ('is_confirmed','confirmed_by',)