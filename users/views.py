from allauth.account.views import LoginView
from core.mixins import CSRFExemptMixin
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
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
        if 'department' in self.request.query_params and self.request.query_params.get('department'):
            department_id = self.request.query_params.get('department')
            departmental_doctors = User.objects.filter(
                department_id=department_id, role='doctor', is_available=True).order_by('first_name')
            return departmental_doctors
        return super().get_queryset()


class DepartmentListAPIView(CSRFExemptMixin, ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]
    queryset = Department.objects.all()


def logout_user(request):
    logout(request)
    return redirect('home:homepage')


def login_redirect(request):
    if request.user.role == 'admin':
        return redirect('dashboard:index:index')
    else:
        return redirect('home:homepage')


class LoginUserView(LoginView):
    def get_success_url(self):
        return reverse_lazy('login_redirect')
