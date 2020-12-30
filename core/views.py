from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import CSRFExemptMixin
from .models import Appointment
from .serializers import AppointmentSerializer
from django.utils.timezone import now


# Create your views here.
class AppointMentCreateAPIView(APIView):
    authentication_classes = (CSRFExemptMixin, )
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):

        user = request.user
        data = request.data

        appointment = Appointment.objects.create(department_id=data['department'], doctor_id=data['doctor'],date=now(),message=data['message'])

        if user.is_anonymous == False:
            appointment.email = user.email
            appointment.phone = user.phone_number
            appointment.name = user.get_full_name()
            appointment.patient = user
        else:
            appointment.phone = data['phone']
            appointment.email = data['email']
            appointment.name = data['name']

        appointment.save()
        serializer = self.serializer_class(appointment)
        return Response(serializer.data)
            
