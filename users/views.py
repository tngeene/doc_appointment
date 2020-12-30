from core.mixins import CSRFExemptMixin
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Department
from .serializers import DepartmentSerializer, UserSerializer

User = get_user_model()

# Create your views here.


class DoctorListAPIView(CSRFExemptMixin, ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.filter(role='doctor', is_available=True)

    def get_queryset(self):
        if 'department' in self.request.query_params:
            department_id = self.request.query_params.get('department')
            departmental_doctors = User.objects.filter(
                department_id=department_id, role='doctor', is_available=True).order_by('first_name')
            return departmental_doctors
        return super().get_queryset()

class DepartmentListAPIView(CSRFExemptMixin, ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]
    queryset = Department.objects.all()