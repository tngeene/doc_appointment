from allauth.account.views import LoginView
import django
from core.mixins import CSRFExemptMixin
from django.contrib.auth import get_user_model, logout, authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.views.generic import FormView, UpdateView
from .models import Department
from .forms import PatientSignUpForm
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

def register_redirect(request):
    messages.success(request, "Account registration successful")
    return redirect('home:my_profile', pk=request.user.pk)

class RegisterUserView(UpdateView):
    def get_success_url(self):
        return reverse_lazy('register_redirect')

class SignUpView(FormView):
    template_name = 'account/signup.html'
    form_class = PatientSignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['email'].lower()
        raw_password = data['password1']

        user = User.objects.create_user(
            username=username,
            email=data['email'],
            password=raw_password
        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.gender = data['gender']
        user.role = 'patient'
        user.save()

        auth_user = authenticate(username=username, password=raw_password)
        login(self.request, auth_user)

        return super(SignUpView, self).form_valid(form)

    def get_success_url(self):
        user = self.request.user
        if user.role == 'patient':
            return reverse_lazy('home:my_profile')
